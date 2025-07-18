(.venv) @Ravine28 ➜ /workspaces/API_REST_2025-1_seg_inf (main) $ curl -X POST http://127.0.0.1:5000/usuarios -H "Content-Type: application/json" -d '{"nome": "Maria", "email": "maria@email.com", "cpf": "12345678900"}'



# {"cpf_hash":"a8476735b37a541a38402a2e7037c79e2d217fe9780e5e34347156ef61eff42b","email":"maria@email.com","id":"35f4017b-e4f3-4fb0-9135-b8d6a5854622","nome":"Maria"}