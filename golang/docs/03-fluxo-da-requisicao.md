# 03. Fluxo da requisição

```
Cliente (browser/curl)
   │  GET /users/1
   ▼
main.go                    → sobe o servidor na porta
   ▼
routes/routes.go           → decide qual controller chamar
   ▼
controllers/user_controller.go → lê o request, chama o model, escreve a resposta
   ▼
models/user.go             → "banco" (slice em memória)
   ▼
controller escreve JSON na resposta (w.Write / json.NewEncoder)
   ▼
Cliente recebe o JSON
```

Mesma ideia do Node/Django/Laravel. A diferença de Go: não existe
`res.json()` mágico — você mesmo serializa com `encoding/json` e escreve
no `http.ResponseWriter`. Mais verboso, mas fica claro **exatamente** o
que está acontecendo (sem "mágica" escondida de framework).
