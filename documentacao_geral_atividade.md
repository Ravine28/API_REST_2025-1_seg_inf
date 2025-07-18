# Objetivo
Esta API REST foi desenvolvida como um exemplo de aplicação prática da Lei Geral de Proteção de Dados (LGPD), oferecendo rotas para cadastro, consulta, exclusão e anonimização dos dados de usuários.

# Conceitos de LGPD implementados
Coleta de dados pessoais previamnete planejada e justificada
    Rota POST /usuarios recebe nome, e-mail e CPF
---
Consentimento
    Presume-se consentimento no envio de dados (caso houvesse uma versão front-end, um checkbox seria implementado)
---
Minimização de dados
    Apenas dados essenciais são coletados
---
Segurança e integridade	
    CPF é DIRETAMENTE armazenado em formato hash (SHA-256)
---
Direito de exclusão	
    Rota:
        DELETE /usuarios/<id>
---
Direito de anonimização	
    Rota (neste caso, anonimizo somente o cpf_hash):
        POST /usuarios/<id>/anonimizar
---
Transparência	
    Rota: 
        GET /politica_privacidade apresenta as diretrizes


# Endpoints da API
Criar usuário
- Método:
    - POST
-    Rota: 
        /usuarios

Descrição: Cadastra um novo usuário. O CPF é automaticamente convertido para hash.

---
Consultar usuário
    Método: 
        GET

    Rota: 
        /usuarios/<id>

Descrição: Retorna os dados do usuário com o id que foi informado (em hash).

---
Anonimizar usuário
    Método: 
        POST

    Rota: 
        /usuarios/<id>/anonimizar

Descrição: Substitui o hash do CPF do usuário pelo valor "ANONIMIZADO".

---
Excluir usuário
    Método: 
        DELETE

    Rota: 
        /usuarios/<id>

Descrição: Remove completamente o usuário da memória da aplicação.

---

# Armazenamento de dados
Atualmente, os dados são mantidos em memória (lista Python), quando desligado dispositivo, todos os dados se perdem. Em uma aplicação real, seria necessário:
    Armazenamento persistente (banco de dados seguro);
    Criptografia em repouso (hash) e em trânsito (http);

# Boas práticas LGPD aplicadas
 CPF não é armazenado em texto puro — é convertido em hash via SHA-256
 A anonimização substitui o hash por "ANONIMIZADO"
 A exclusão remove completamente os dados da lista em memória
 A política de privacidade está visível ao usuário via rota pública (removi do código uma vez que me limitei ao terminal, porém há um arquivo .md com as políticas de privacidade neste repositório)
