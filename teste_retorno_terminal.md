# NOVO CADASTRO DE USUÁRIO
## ENTRADA #1
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X POST http://127.0.0.1:5000/usuarios \
    -H "Content-Type: application/json" \
    -d '{"nome": "Smeagol", "email": "smeagol@email.com", "cpf": "11122233344"}'
## SAÍDA #1
{
    "cpf_hash": "ebdca3085b677490512e0078a35b8c93f5e8292845bfcab2f1aca03621c2e4f6",
    "email": "smeagol@email.com",
    "id": "4898eee9-1c9d-4e1e-8268-8219c3fcc0b7",
    "nome": "Smeagol"
}

## ENTRADA #2
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X POST http://127.0.0.1:5000/usuarios \
    -H "Content-Type: application/json" \
    -d '{"nome": "Pimenta", "email": "pimenta@email.com", "cpf": "44455566677"}'
## SAÍDA #2
{
  "cpf_hash": "f47e87f3e3ae336dce1a9d9cc3ad7348be1b755c2295e81292b8624cdfef998a",
  "email": "pimenta@email.com",
  "id": "d44c85b5-dd4e-4bb0-90fe-abfc59674417",
  "nome": "Pimenta"
}

# BUSCAR CADASTRO DE USUÁRIO (via ID)
## ENTRADA #3
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl http://127.0.0.1:5000/usuarios/d44c85b5-dd4e-4bb0-90fe-abfc59674417
## SAÍDA #3
{
  "cpf_hash": "f47e87f3e3ae336dce1a9d9cc3ad7348be1b755c2295e81292b8624cdfef998a",
  "email": "pimenta@email.com",
  "id": "d44c85b5-dd4e-4bb0-90fe-abfc59674417",
  "nome": "Pimenta"
}

# ANONIMIZAR DADOS DE USUÁRIO
## ENTRADA #4
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X POST http://127.0.0.1:5000/usuarios/d44c85b5-dd4e-4bb0-90fe-abfc59674417/anonimizar
## SAÍDA #4
{
  "cpf_hash": "ANONIMIZADO",
  "email": "pimenta@email.com",
  "id": "d44c85b5-dd4e-4bb0-90fe-abfc59674417",
  "nome": "Pimenta"
}

# EXCLUIR USUÁRIO
## ENTRADA #5
    (.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X DELETE http://127.0.0.1:5000/usuarios/4898eee9-1c9d-4e1e-8268-8219c3fcc0b7
## SAÍDA #5

## ENTRADA #6
## SAÍDA #6

## ENTRADA #7
## SAÍDA #7