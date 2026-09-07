# 03. Fluxo da requisição (do request até a resposta)

```
Cliente (browser/Postman)
   │  GET /users/1
   ▼
server.ts        → só faz o servidor "escutar" a porta
   ▼
app.ts           → middlewares globais (json parser, cors, log)
   ▼
routes/*.ts      → decide qual controller chamar
   ▼
controllers/*.ts → pega dados da request, chama o model, monta a resposta
   ▼
models/*.ts      → "banco de dados" (aqui, um array em memória)
   ▼
controller devolve res.json(dados)
   ▼
Cliente recebe o JSON
```

Mesma lógica de Django (`urls → view → model → response`) ou Laravel
(`routes → controller → model → response`). O nome muda, o fluxo é igual.

Rode a API de exemplo e siga esse caminho com `console.log` em cada
arquivo — é o jeito mais rápido de "sentir" o fluxo.
