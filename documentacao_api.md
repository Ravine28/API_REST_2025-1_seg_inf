# Documentação da API - LGPD por Design

## Contexto
Sistema fictício de cadastro para agendamento de serviços para pessoas neurodivergentes. A API respeita os princípios da LGPD desde sua concepção.

---

## Endpoints

### POST /usuarios
Cria um novo usuário.

**Campos obrigatórios:**
- nome_completo (string)
- email (string)
- nascimento (string)
- senha (string)

**Campos opcionais:**
- nome_social (string)
- genero (string)

ex.:
curl -X POST http://localhost:5000/usuarios -H "Content-Type: application/json" -d '{
  "nome_completo": "João da Silva",
  "nome_social": "Joana",
  "email": "joana@email.com",
  "nascimento": "1990-01-01",
  "genero": "não-binário",
  "senha": "minhasenha123"
}'

---

### GET /usuarios/<id>
Retorna os dados do usuário sem a senha.

ex.:
Ver usuário com ID 1
curl http://localhost:5000/usuarios/1

---

### DELETE /usuarios/<id>
Exclui um usuário permanentemente.

ex.: 
Excluir usuário com ID 1
curl -X DELETE http://localhost:5000/usuarios/1

---

### POST /usuarios/<id>/anonimizar
Remove dados pessoais, substituindo-os por valores genéricos ou nulos.

ex.: 
Anonimizar usuário com ID 1
curl -X POST http://localhost:5000/usuarios/1/anonimizar

---

### GET /politica-privacidade
Retorna um resumo da política de privacidade da aplicação.

ex.: 
Ver política de privacidade
curl http://localhost:5000/politica-privacidade

---

## Segurança
- Senhas criptografadas com SHA-256.
- HTTPS recomendado para produção.