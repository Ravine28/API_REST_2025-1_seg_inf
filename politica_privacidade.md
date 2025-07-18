# Política de Privacidade
## Esta aplicação respeita a Lei Geral de Proteção de Dados (LGPD), assegurando os seguintes princípios:

Apenas os dados necessários são coletados: nome, e-mail e CPF

Coletamos os seguintes dados:
- Nome completo
- E-mail
- CPF (anonimizado)
- Senha (criptografada)

Finalidade:
- Cadastro para agendamento de consultas com profissionais às necessidades neurodivergentes.
-   Nome para identificaççao social;
-   e-mail para login e notificaçoes/contato;
-   CPF para identificação única por cadastro;

Armazenamento:
- Os dados são armazenados temporariamente em memória. Não são persistidos em banco de dados para esta simulação.

Proteção:
- Senhas são armazenadas em formato criptografado (hash SHA-256).
- A API funciona via HTTPS.

Direitos do titular:
- A qualquer momento, o titular pode solicitar a exclusão ou anonimização dos dados via endpoints:
  - DELETE /usuarios/{id}
  - POST /usuarios/{id}/anonimizar


O CPF é imediatamente anonimizado por hash (não é armazenado em formato legível)

Os dados não são utilizados para nenhum fim comercial ou compartilhados com terceiros

O titular pode solicitar a exclusão completa dos dados via rota DELETE

A aplicação é de uso acadêmico e não opera com dados reais em produção

Não há rastreamento, cookies ou coleta invisível de dados

A proteção dos dados é feita por boas práticas de desenvolvimento seguro

A aplicação pode ser desativada a qualquer momento sem retenção de dados
