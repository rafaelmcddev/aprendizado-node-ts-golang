# Testando no Postman

[`aprendizado-backend.postman_collection.json`](./aprendizado-backend.postman_collection.json)
tem as 3 requisições (listar, buscar por id, criar) das 4 stacks já
prontas.

## Como importar

1. Postman → **Import** (canto superior esquerdo)
2. Arraste o arquivo `aprendizado-backend.postman_collection.json`
3. Vai aparecer uma collection com 4 pastas: Node + TS, Go, FastAPI, Flask

## Como usar

Suba **uma stack por vez** (elas usam a mesma porta por padrão — Node,
Go e Flask na `3000`, FastAPI na `8000`):

```bash
# Node
cd node-ts/api-exemplo && npm install && npm run dev

# Go
cd golang/api-exemplo && go run main.go

# FastAPI
cd fastapi/api-exemplo && pip install -r requirements.txt && uvicorn app.main:app --reload

# Flask
cd flask/api-exemplo && pip install -r requirements.txt && python run.py
```

Depois é só chamar as requisições da pasta correspondente no Postman.

## Sem Postman? Também dá pra testar com `curl`

```bash
curl http://localhost:3000/users
curl http://localhost:3000/users/1
curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d '{"name":"Grace Hopper","email":"grace@example.com"}'
```

(troque a porta pra `8000` se for testar a FastAPI)

## FastAPI já vem com um "Postman" embutido

Rodando a FastAPI, abra `http://localhost:8000/docs` — é uma UI Swagger
que testa a API direto no navegador, sem precisar de Postman nem `curl`.
