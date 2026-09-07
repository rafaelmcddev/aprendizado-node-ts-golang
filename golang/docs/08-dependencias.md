# 08. Como instalar e usar dependências

Gerenciador: **go mod** (vem com o Go), equivalente ao `pip`/`composer`.

```bash
go mod init aprendizado/api-exemplo   # cria o go.mod (1x, no começo do projeto)
go get github.com/gorilla/mux         # instala e grava no go.mod
go mod tidy                           # limpa dependências não usadas + baixa as que faltam
```

Onde fica instalado: cache global em `$GOPATH/pkg/mod` (não fica uma pasta
tipo `node_modules` dentro do projeto — mais parecido com como o pip
instala globalmente, mas versionado por projeto via `go.mod`).

**Como usar depois de instalar:**
```go
import (
    "net/http"                  // standard library, sempre disponível
    "github.com/gorilla/mux"    // dependência externa, precisa do go get
)
```

Este `api-exemplo/` usa **zero dependência externa** de propósito — só
`net/http` da standard library, que já resolve roteamento, servidor e
JSON sem instalar nada. Isso também é uma escolha comum em produção: o
ecossistema padrão do Go é grande o suficiente pra muita coisa.
