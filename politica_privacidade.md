# Política de Privacidade

Coletamos os seguintes dados:
- Nome completo
- Nome social (opcional)
- E-mail
- Data de nascimento
- Gênero (opcional)
- Senha (criptografada)

Finalidade:
- Cadastro para agendamento de consultas com profissionais sensíveis às necessidades neurodivergentes.

Armazenamento:
- Os dados são armazenados temporariamente em memória. Não são persistidos em banco de dados para esta simulação.

Proteção:
- Senhas são armazenadas em formato criptografado (hash SHA-256).
- A API funciona via HTTPS.

Direitos do titular:
- A qualquer momento, o titular pode solicitar a exclusão ou anonimização dos dados via endpoints:
  - DELETE /usuarios/{id}
  - POST /usuarios/{id}/anonimizar