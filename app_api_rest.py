from flask import Flask, request, jsonify
import uuid
from hashlib import sha256

app = Flask(__name__)

#em memória, por simplicidade
usuarios = []

#função para criar o hash do CPF
def hash_cpf(cpf):
    return sha256(cpf.encode()).hexdigest()

#página inicial (rota '/')
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'mensagem': '✅ API REST em Flask está rodando. Use /usuarios para interagir.'
    }), 200

#rota para pegar todos os usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

#rota para adicionar um novo usuário
@app.route('/usuarios', methods=['POST'])
def add_usuario():
    dados = request.get_json()
    
    #gerar um id único
    novo_usuario = {
        'id': str(uuid.uuid4()),
        'nome': dados.get('nome'),
        'email': dados.get('email'),
        'cpf_hash': hash_cpf(dados.get('cpf'))
    }

    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
