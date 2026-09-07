# API de exemplo — Node + TypeScript + Express

CRUD simples de usuários, sem banco (dados em memória), pra você focar no
fluxo request → controller → model → response.

## Rodar

```bash
npm install
cp .env.example .env
npm run dev
```

Abra `http://localhost:3000` → vê o front (HTML puro chamando a API).
Abra `http://localhost:3000/users` → vê o JSON puro.

## Testar

```bash
npm test
```

## Endpoints

| Método | Rota | O que faz |
|---|---|---|
| GET | `/users` | lista todos |
| GET | `/users/:id` | busca um |
| POST | `/users` | cria (body: `{ "name": "...", "email": "..." }`) |

## Estrutura

```
src/
  config/     → lê .env
  routes/     → URL → controller
  controllers/→ lógica da requisição
  models/     → dados
  views/      → front estático (HTML)
  tests/      → testes unitários
  app.ts      → monta o Express
  server.ts   → sobe o servidor
```
