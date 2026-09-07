# 06. Onde ficam os testes unitários

Convenção fixa (não é opinião de time, é regra da linguagem): arquivo
`nome_test.go` do lado do arquivo que ele testa. Ferramenta de teste já
vem embutida, sem instalar nada — equivalente a ter o `pytest` de fábrica.

```go
// models/user_test.go
package models

import "testing"

func TestFindByID(t *testing.T) {
    user, ok := FindByID("1")
    if !ok || user.Name != "Ada Lovelace" {
        t.Errorf("esperava Ada Lovelace, veio %v", user)
    }
}
```

Rodar:
```bash
go test ./...
```

Sem `describe`/`it` como no Vitest/PyTest — cada `func TestAlgumaCoisa`
é um teste. `t.Errorf` marca falha mas continua; `t.Fatalf` para na hora.
