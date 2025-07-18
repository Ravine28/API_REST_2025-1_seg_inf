from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
usuarios = [] #lista

def buscar_usuario(usuario_id):
    return next((u for u in usuarios if u['id'] == usuario_id), None)

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    novo_usuario = {
        'id': str(uuid.uuid4()),
        'nome': dados.get('nome'),
        'email': dados.get('email'),
        'cpf': dados.get('cpf')
    }
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

@app.route('/usuarios/<usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    usuario = buscar_usuario(usuario_id)
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    dados = request.json
    usuario.update({
        'nome': dados.get('nome', usuario['nome']),
        'email': dados.get('email', usuario['email']),
        'cpf': dados.get('cpf', usuario['cpf']),
    })
    return jsonify(usuario), 200

@app.route('/usuarios/<usuario_id>', methods=['DELETE'])
def deletar_usuario(usuario_id):
    usuario = buscar_usuario(usuario_id)
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    usuarios.remove(usuario)
    return jsonify({'mensagem': 'Usuário removido'}), 200

if __name__ == '__main__':
    app.run(debug=True)
