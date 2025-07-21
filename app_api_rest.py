import json
from flask import Flask, request, jsonify
import uuid
from hashlib import sha256

app = Flask(__name__)
usuarios = [] #lista simulada de usuários

#função para gerar o hash do CPF
def hash_cpf(cpf):
    return sha256(cpf.encode()).hexdigest()

#(endpoint) rota para criar um novo usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    
    #verificação de dados obrigatórios
    if not dados.get('nome') or not dados.get('email') or not dados.get('cpf'):
        return jsonify({"error": "Dados incompletos"}), 400

    #criação do novo usuário com CPF hashado
    novo_usuario = {
        'id': str(uuid.uuid4()),
        'nome': dados.get('nome'),
        'email': dados.get('email'),
        'cpf_hash': hash_cpf(dados.get('cpf'))
}
    
    #adiciona o usuário à lista
    usuarios.append(novo_usuario)
    
    return jsonify(novo_usuario), 201

#(endpoint) rota para obter um usuário pelo ID
@app.route('/usuarios/<id>', methods=['GET'])
def obter_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return jsonify(usuario)
    
    return jsonify({"error": "Usuário não encontrado"}), 404

#(endpoint) rota para anonimizar um usuário (substituir o NOME por 'ANONIMIZADO')
@app.route('/usuarios/<id>/anonimizar-nome', methods=['POST'])
def anonimizar_nome(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuario['nome'] = 'NOME DE USUÁRIO ANONIMIZADO'
            return jsonify({"message": "Nome anonimizado com sucesso"})
    
    return jsonify({"error": "Usuário não encontrado"}), 404

# (endpoint) rota para excluir um usuário pelo ID
@app.route('/usuarios/<id>', methods=['DELETE'])
def excluir_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
    return jsonify({"message": "Usuário excluído com sucesso"})

@app.route('/')
def home():
    return """
    <h1>API LGPD - Cadastro de Usuários</h1>
    <p>Endpoints disponíveis:</p>
    <ul>
        <li><b>POST /usuarios</b> - Criar novo usuário</li>
        <li><b>GET /usuarios/&lt;id&gt;</b> - Buscar usuário</li>
        <li><b>POST /usuarios/&lt;id&gt;/anonimizar-nome</b> - Anonimizar nome</li>
        <li><b>DELETE /usuarios/&lt;id&gt;</b> - Excluir usuário</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
