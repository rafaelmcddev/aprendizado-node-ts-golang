# 07. Como debugar (equivalente a `dd()` / `print()` / `raise`)

| Python/PHP | Go | Uso |
|---|---|---|
| `print()` | `fmt.Println(x)` | mostrar valor no terminal |
| `dd($var)` | `fmt.Printf("%+v\n", x); os.Exit(1)` | mostrar e parar |
| `pdb.set_trace()` | `dlv debug` (Delve) | debugger real, com breakpoint |
| `raise Exception(...)` | `panic("mensagem")` | erro fatal, aborta o programa |
| `try/except` | `if err != nil { ... }` | Go não tem exceção — todo erro é um valor retornado |

**Diferença mental importante:** em Python/PHP você lança exceção e trata
com try/catch. Em Go, função retorna `(resultado, error)` e **você checa
na mão, toda vez**:
```go
user, err := models.FindByID(id)
if err != nil {
    fmt.Println("erro:", err) // seu "print de debug"
    http.Error(w, err.Error(), 500)
    return
}
```

Isso é verboso, mas é assim mesmo — não tem exceção "escondida" saltando
camadas. `panic`/`recover` existe mas é raro, só pra erro realmente fatal.

Debugger de verdade: instale o [Delve](https://github.com/go-delve/delve)
(`go install github.com/go-delve/delve/cmd/dlv@latest`) e rode
`dlv debug ./main.go` — funciona como o `pdb`, com breakpoints.
