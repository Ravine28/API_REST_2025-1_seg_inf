# NOVO CADASTRO DE USUÁRIO
## ENTRADA #1 (NO TERMINAL)
    curl -X POST http://localhost:5000/usuarios \-H "Content-Type: application/json" \-d '{"nome": "Smeagol", "email": "smeagol@email.com", "cpf": "11122233344"}'

## SAÍDA #1 (NO TERMINAL)
    {
    "cpf_hash": "ebdca3085b677490512e0078a35b8c93f5e8292845bfcab2f1aca03621c2e4f6",
    "email": "smeagol@email.com",
    "id": "cdc25141-54f0-4e1b-b5ff-977fb26c8307",
    "nome": "Smeagol"
    }

## ENTRADA #2 (NO TERMINAL)
    curl -X POST http://localhost:5000/usuarios \-H "Content-Type: application/json" \-d '{"nome": "Pimenta", "email""cpf_hash": "f47e87f3e3ae336dce1a9d9cc3ad7348be1b755c2295e81292b8624cdfef998a",
    "email": "pimenta@email.com",
    "id": "1d4daffe-bc81-4e42-8cf8-a5b7d4654c0e",
    "nome": "Pimenta": "pimenta@email.com", "cpf": "44455566677"}'

## SAÍDA #2 (NO TERMINAL)
    {
    "cpf_hash": "f47e87f3e3ae336dce1a9d9cc3ad7348be1b755c2295e81292b8624cdfef998a",
    "email": "pimenta@email.com",
    "id": "be118f3d-c0e6-449d-8475-06adb1b4f1c8",
    "nome": "Pimenta"
    }

# BUSCAR CADASTRO DE USUÁRIO (NO TERMINAL)
## ENTRADA #3
    curl http://localhost:5000/usuarios/be118f3d-c0e6-449d-8475-06adb1b4f1c8

## SAÍDA #3 (NO TERMINAL)
    {
    "cpf_hash": "f47e87f3e3ae336dce1a9d9cc3ad7348be1b755c2295e81292b8624cdfef998a",
    "email": "pimenta@email.com",
    "id": "be118f3d-c0e6-449d-8475-06adb1b4f1c8",
    "nome": "Pimenta"
    }

# ANONIMIZAR NOME DE USUÁRIO
## ENTRADA #4 (NO TERMINAL)
    curl -X POST http://localhost:5000/usuarios/cdc25141-54f0-4e1b-b5ff-977fb26c8307/anonimizar-nome

## SAÍDA #4 (NO TERMINAL)
    {
    "message": "Nome anonimizado com sucesso"
    }

# BUSCAR CADASTRO DE USUÁRIO (NO TERMINAL)
## ENTRADA #3
    curl http://localhost:5000/usuarios/cdc25141-54f0-4e1b-b5ff-977fb26c8307

## SAÍDA #3 (NO TERMINAL)
    {
    "cpf_hash": "ebdca3085b677490512e0078a35b8c93f5e8292845bfcab2f1aca03621c2e4f6",
    "email": "smeagol@email.com",
    "id": "cdc25141-54f0-4e1b-b5ff-977fb26c8307",
    "nome": "NOME DE USU\u00c1RIO ANONIMIZADO" #bugzim por ter acento
    }

# EXCLUIR USUÁRIO
## ENTRADA #5 (NO TERMINAL)
    curl -X DELETE http://localhost:5000/usuarios/cdc25141-54f0-4e1b-b5ff-977fb26c8307
    

## SAÍDA #5 (NO TERMINAL)
{
  "message": "Usu\u00e1rio exclu\u00eddo com sucesso"
} #bugzim por ter acento
