# Documentação da API - LGPD por Design

## Contexto
  Sistema fictício de cadastro para alimentação do banco de dados de pessoas usuárias de um possível sistema de serviços voltados à pessoas neurodivergentes. Dados especificamente selecionados para coleta para que haja individualização por CPF, e contato por e-mail.

### 1. Dados coletados
  1) nome (string)
  2) email (string - anonimizado via UUID (Universally Unique Identifier))
  3) CPF (criptografado via hash)

### 2. Finalidade da coleta
  Gerenciar registros de usuários na aplicação;
  Fornecer funcionalidades CRUD (Create, Read, Update, Delete);

### 3. Local de armazenamento
  Os dados são mantidos em memória (RAM) durante a execução do sistema (não persistidos em banco);
  Para ambiente real, recomenda-se armazenamento seguro com banco de dados criptografado;

### 4. Proteção dos dados
  CPF é protegido em repouso usando hash SHA-256;
  Em produção, recomenda-se execução sob HTTPS (criptografia em trânsito);
  Dados não são compartilhados com terceiros;

### 5. Direito do titular
  Pode solicitar exclusão de seus dados via requisição:
    ('/usuarios/<id>', methods=['DELETE']);
  Como os CPFs são anonimizados (hash irreversível), os dados são considerados protegidos em repouso:
    ('/usuarios/<id>/anonimizar', methods=['POST']);
      Não é possível recuperar o CPF original a partir do hash, protegendo a identidade;

### 6. Regras de acesso
  Todas as requisições são públicas (ambiente de teste)
  Para produção, recomenda-se autenticação por token e controle de papéis (admin/usuário)
    Obs.: implementação futura

---

## Endpoints

### POST /usuarios
Cria um novo usuário.

**Campos obrigatórios:**
  1) nome (string)
  2) email (string - anonimizado via UUID (Universally Unique Identifier))
  3) CPF (criptografado via hash)

  ex.:
    curl -X POST http://127.0.0.1:5000 -H "Content-Type: application/json" -d '{
      "nome_completo": "Smeagol Miguel",
      "email": "smeagol@email.com",
      "cpf": 00000000011
    }'

---

### GET /usuarios/<id>
  Retorna os dados do usuário via ID.
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

### POST /usuarios/<id>/anonimizar-nome
  Remove dados pessoais, substituindo-os por valores genéricos ou nulos.
    ex.: 
    Anonimizar usuário com ID 1
      curl -X POST http://localhost:5000/usuarios/1/anonimizar-nome

---

## Segurança
  Senhas criptografadas com SHA-256.
  HTTPS recomendado para produção.
