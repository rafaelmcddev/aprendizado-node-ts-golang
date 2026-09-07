# 04. Como o backend "fala" com o front

Mesma regra de sempre: o backend não chama o front, o front chama o
backend via HTTP.

Em Go, o backend pode:

**1. Só responder JSON** (mais comum, front é outro projeto — React, etc)
```go
json.NewEncoder(w).Encode(users)
```

**2. Servir arquivo estático** (HTML puro, tipo este projeto)
```go
mux.Handle("/", http.FileServer(http.Dir("./views")))
```

O `api-exemplo/` faz os dois: serve `views/index.html`, que tem um
`<script>` chamando `fetch('/users')` — o front pedindo dado pro backend,
nunca o contrário.

Veja [`api-exemplo/views/index.html`](../api-exemplo/views/index.html).
