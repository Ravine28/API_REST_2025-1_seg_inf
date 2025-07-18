from flask import Flask, request, jsonify
import uuid
from hashlib import sha256

app = Flask(__name__)

#lista simulada de usuários
usuarios = []

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

#(endpoint) rota para anonimizar um usuário (substituir o CPF por 'ANONIMIZADO')
@app.route('/usuarios/<id>/anonimizar', methods=['POST'])
def anonimizar_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuario['cpf_hash'] = 'ANONIMIZADO'
            return jsonify(usuario)
    
    return jsonify({"error": "Usuário não encontrado"}), 404

#(endpoint) rota para excluir um usuário pelo ID
@app.route('/usuarios/<id>', methods=['DELETE'])
def excluir_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
    return jsonify({"message": "Usuário excluído com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
