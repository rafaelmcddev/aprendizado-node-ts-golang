# 03. Fluxo da requisição

```
Cliente (browser/curl)
   │  GET /users/1
   ▼
run.py                     → chama create_app() e sobe o servidor
   ▼
app/__init__.py            → create_app() monta a aplicação, registra Blueprints
   ▼
app/routes/user.py         → decide qual função chamar pela rota batida
   ▼
função show()               → chama o model, monta a resposta
   ▼
app/models/user.py         → "banco" (lista em memória)
   ▼
Flask serializa com jsonify() — você chama na mão, não é automático
   ▼
Cliente recebe o JSON
```

Diferença chave pro Django: sem middleware pesado por padrão, sem ORM
rodando escondido. É o fluxo mais "cru" das 4 linguagens/frameworks deste
repositório — bom pra entender o mecanismo puro de request→response.
