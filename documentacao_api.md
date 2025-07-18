# Documentação da API - LGPD por Design

## Contexto
Sistema fictício de cadastro para agendamento de serviços para pessoas neurodivergentes. A API respeita os princípios da LGPD desde sua concepção.

### 1. Dados coletados
nome (string)

email (string)

CPF (criptografado via hash)

senha (string)

### 2. Finalidade da coleta
Gerenciar registros de usuários na aplicação

Fornecer funcionalidades CRUD (Create, Read, Update, Delete)

Armazenamento local em memória (educacional/teste)

### 3. Local de armazenamento
Os dados são mantidos em memória (RAM) durante a execução do sistema (não persistidos em banco)

Para ambiente real, recomenda-se armazenamento seguro com banco de dados criptografado

### 4. Proteção dos dados
CPF é protegido em repouso usando hash SHA-256

Em produção, recomenda-se execução sob HTTPS (criptografia em trânsito)

Dados não são compartilhados com terceiros

### 5. Direito do titular
Pode solicitar exclusão de seus dados via requisição DELETE na rota /usuarios/<id>

Como os CPFs são anonimizados (hash irreversível), os dados são considerados protegidos em repouso

Não é possível recuperar o CPF original a partir do hash, protegendo a identidade

### 6. Regras de acesso
Todas as requisições são públicas (ambiente de teste)

Para produção, recomenda-se autenticação por token e controle de papéis (admin/usuário)

---

## Endpoints

### POST /usuarios
Cria um novo usuário.

**Campos obrigatórios:**
- nome_completo (string)
- email (string)
- cpf (criptografado via hash)
- senha (string)

ex.:
curl -X POST http://localhost:5000/usuarios -H "Content-Type: application/json" -d '{
  "nome_completo": "João da Silva",
  "email": "joana@email.com",
  "cpf": 00000000011
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
