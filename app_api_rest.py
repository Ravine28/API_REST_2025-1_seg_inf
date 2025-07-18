from flask import Flask, request, jsonify
from hashlib import sha256
import uuid

app = Flask(__name__)
usuarios = []

#função para aplicar hash ao CPF (criptografia em repouso)
def hash_cpf(cpf):
    return sha256(cpf.encode()).hexdigest()

#função para buscar usuário por ID
def buscar_usuario(usuario_id):
    return next((u for u in usuarios if u['id'] == usuario_id), None)


#(endpoint)rota GET: listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

#(endpoint)rota POST: criar novo usuário com hash no CPF
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    novo_usuario = {
        'id': str(uuid.uuid4()),
        'nome': dados.get('nome'),
        'email': dados.get('email'),
        'cpf_hash': hash_cpf(dados.get('cpf'))
    }
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

#(endpoint) rota PUT: atualizar usuário existente
@app.route('/usuarios/<usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    usuario = buscar_usuario(usuario_id)
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    dados = request.json
    usuario.update({
        'nome': dados.get('nome', usuario['nome']),
        'email': dados.get('email', usuario['email']),
        'cpf_hash': hash_cpf(dados.get('cpf')) if dados.get('cpf') else usuario['cpf_hash']
    })
    return jsonify(usuario), 200

#(endpoint) rota DELETE: excluir usuário
@app.route('/usuarios/<usuario_id>', methods=['DELETE'])
def deletar_usuario(usuario_id):
    usuario = buscar_usuario(usuario_id)
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    usuarios.remove(usuario)
    return jsonify({'mensagem': 'Usuário removido'}), 200

#executar API
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

