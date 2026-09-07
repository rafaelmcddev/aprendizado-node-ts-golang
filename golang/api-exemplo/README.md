# API de exemplo — Go

CRUD simples de usuários, sem banco (dados em memória), só com a standard
library (`net/http`) — zero dependência externa.

## Rodar

```bash
go run main.go
```

Abra `http://localhost:3000` → vê o front (HTML puro chamando a API).
Abra `http://localhost:3000/users` → vê o JSON puro.

Pra mudar a porta: `PORT=4000 go run main.go`.

## Testar

```bash
go test ./...
```

> Também dá pra testar pelo Postman: collection pronta em [`/postman`](../../postman).

## Endpoints

| Método | Rota | O que faz |
|---|---|---|
| GET | `/users` | lista todos |
| GET | `/users/{id}` | busca um |
| POST | `/users` | cria (body: `{ "name": "...", "email": "..." }`) |

## Estrutura

```
config/      → lê variáveis de ambiente
routes/      → URL → controller
controllers/ → lógica da requisição
models/      → dados + testes (user_test.go)
views/       → front estático (HTML)
main.go      → sobe o servidor
```
