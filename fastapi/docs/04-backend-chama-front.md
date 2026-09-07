# 04. Como o backend "fala" com o front

Mesma regra sempre: o backend não chama o front, o front chama o backend.

FastAPI é **API-first** — diferente do Django, ele não vem com template
engine "oficial". Na prática:

**1. Front separado (o uso mais comum de FastAPI)**
Front é outro projeto (React, etc), chama via `fetch`. FastAPI só devolve
JSON.

**2. Servir HTML estático** (se quiser, dá, mas não é o forte do FastAPI)
```python
app.mount("/", StaticFiles(directory="app/views", html=True))
```

O `api-exemplo/` serve um HTML simples em `/` que faz `fetch('/users')`
pra você ver o front pedindo dado — igual ao padrão que você já viu no
`node-ts/` e no `golang/`.

Bônus do FastAPI: `/docs` já vem pronto com uma UI (Swagger) que testa a
API sem precisar de front nenhum — ótimo pra debugar rota isolada.
