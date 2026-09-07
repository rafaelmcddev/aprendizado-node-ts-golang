# 05. Model / View / Controller

| Camada | Pasta | Faz o quê |
|---|---|---|
| Model | `models/` | struct + regra de negócio |
| Controller | `controllers/` | recebe request, chama model, escreve resposta |
| View | `views/` | HTML estático servido pro navegador |

```go
// controllers/user_controller.go
func Show(w http.ResponseWriter, r *http.Request) {
    id := r.PathValue("id")
    user, ok := models.FindByID(id) // Model
    if !ok {
        http.Error(w, "não encontrado", http.StatusNotFound)
        return
    }
    json.NewEncoder(w).Encode(user) // resposta (sem template de View aqui)
}
```

Go também não impõe estrutura de pastas — é convenção do time. Frameworks
maiores (Gin, Echo, Fiber) existem, mas este projeto usa só `net/http`
pra você entender o mecanismo antes de aprender o "atalho" do framework.
