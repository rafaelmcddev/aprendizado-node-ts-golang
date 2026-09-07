# 09. Onde ficam os imports

Sempre em um bloco no topo do arquivo, logo depois do `package`:

```go
package controllers

import (
    "encoding/json"                        // standard library
    "net/http"                              // standard library

    "aprendizado/api-exemplo/models"        // pacote seu, dentro do módulo
)
```

Regras rápidas:
- Vem antes de tudo `package nome` — define de qual "pasta lógica" (pacote)
  o arquivo faz parte. Não precisa bater com o nome da pasta, mas é
  convenção fazer bater.
- Import sem `/` → standard library
- Import com domínio (`github.com/...`) → dependência externa
- Import com o nome do seu módulo (definido no `go.mod`) → arquivo seu

Diferente de Node/Python: **importar algo sem usar é erro de compilação**,
não warning. O Go te obriga a manter import limpo.
