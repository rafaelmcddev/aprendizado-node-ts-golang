# 03. Fluxo da requisição

```
Cliente (browser/curl)
   │  GET /users/1
   ▼
app/main.py               → instancia o FastAPI, registra os routers
   ▼
app/routers/user.py       → decide qual função chamar pela rota batida
   ▼
FastAPI valida o parâmetro (id: int) automaticamente, antes até
de entrar na função — se mandar "abc" no lugar de um número, nem
chega no seu código, já retorna 422 sozinho
   ▼
função show()              → chama o "model", monta a resposta
   ▼
app/models/user.py        → "banco" (lista em memória)
   ▼
FastAPI serializa o retorno pra JSON sozinho (não precisa `json.dumps`)
   ▼
Cliente recebe o JSON
```

Diferença chave pro Django: o Django tem middleware pesado, ORM, etc,
rodando no meio. O FastAPI é mais direto — poucas camadas entre a rota e
sua função. A validação automática (tipo `id: int`) é o maior "mágico"
dele, e some se você tirar a tipagem.
