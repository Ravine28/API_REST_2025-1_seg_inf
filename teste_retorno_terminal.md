# NOVO CADASTRO DE USUÁRIO
## ENTRADA #1
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X POST http://localhost:5000/usuarios \
    -H "Content-Type: application/json" \
    -d '{"nome": "Smeagol", "email": "smeagol@email.com", "cpf": "11122233344"}'
## SAÍDA #1
{
    "cpf_hash": "ebdca3085b677490512e0078a35b8c93f5e8292845bfcab2f1aca03621c2e4f6",
    "email": "smeagol@email.com",
    "id": "8e447a29-3581-4dd0-8b71-7722f078b084",
    "nome": "Smeagol"
}

## ENTRADA #2
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X POST http://localhost:5000/usuarios \
    -H "Content-Type: application/json" \
    -d '{"nome": "Pimenta", "email": "pimenta@email.com", "cpf": "44455566677"}'
## SAÍDA #2
{
  "cpf_hash": "f47e87f3e3ae336dce1a9d9cc3ad7348be1b755c2295e81292b8624cdfef998a",
  "email": "pimenta@email.com",
  "id": "1d4daffe-bc81-4e42-8cf8-a5b7d4654c0e",
  "nome": "Pimenta"
}

# BUSCAR CADASTRO DE USUÁRIO (via ID)
## ENTRADA #3
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl http://localhost:5000/usuarios/1d4daffe-bc81-4e42-8cf8-a5b7d4654c0e
## SAÍDA #3
{
  "cpf_hash": "f47e87f3e3ae336dce1a9d9cc3ad7348be1b755c2295e81292b8624cdfef998a",
  "email": "pimenta@email.com",
  "id": "1d4daffe-bc81-4e42-8cf8-a5b7d4654c0e",
  "nome": "Pimenta"
}

# ANONIMIZAR DADOS DE USUÁRIO
## ENTRADA #4
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X POST http://localhost:5000/usuarios/8e447a29-3581-4dd0-8b71-7722f078b084/anonimizar
## SAÍDA #4
{
  "cpf_hash": "ANONIMIZADO",
  "email": "pimenta@email.com",
  "id": "1d4daffe-bc81-4e42-8cf8-a5b7d4654c0e",
  "nome": "Pimenta"
}

# EXCLUIR USUÁRIO
## ENTRADA #5
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X DELETE http://localhost:5000/usuarios/usuarios/8e447a29-3581-4dd0-8b71-7722f078b084
## SAÍDA #5
    {"message": "Usuário excluído com sucesso"}
