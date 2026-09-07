# 02. Rota → qual arquivo é chamado

Igual Node/Express: você declara a rota na mão. Desde o Go 1.22 o
`net/http` já suporta padrões com método e parâmetro (`GET /users/{id}`)
sem precisar de framework.

```go
// routes/routes.go
mux.HandleFunc("GET /users/{id}", controllers.Show)
```

Caminho até achar o código:

1. `main.go` → sobe o servidor, chama `routes.New()`
2. `routes/routes.go` → registra `GET /users/{id}` → `controllers.Show`
3. `controllers/user_controller.go` → função `Show` executa

Mesmo padrão do Node (`server → routes → controller`), só que aqui tudo é
função, não tem classe.

Veja o real em [`api-exemplo/routes/routes.go`](../api-exemplo/routes/routes.go).
