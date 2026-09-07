# 18. Próximos passos (depois de entender este exemplo)

Mesma lógica do doc equivalente das outras stacks: aqui vai só o mapa,
sem se aprofundar agora.

## 1. Banco de dados de verdade

Troque a slice em memória (`models/user.go`) por um banco real. Duas
direções comuns:
- **`database/sql` + driver puro** (ex: `lib/pq` pra Postgres) — mais
  verboso, mais controle, mais "Go idiomático"
- **GORM** — ORM completo, mais parecido com o que você já usa em Django

Migrations: veja o [doc 11](./11-migrations.md) (golang-migrate).

## 2. Autenticação

Padrão comum: **JWT**. Lib mais usada: `golang-jwt/jwt`. Mesmo fluxo das
outras stacks — token no header `Authorization: Bearer <token>`.

## 3. Validação mais robusta

Este projeto valida na mão (`if name == "" || email == ""`). Em projeto
maior, lib como `go-playground/validator` permite declarar regra via tag
no struct:
```go
type UserCreate struct {
    Name  string `validate:"required"`
    Email string `validate:"required,email"`
}
```

## 4. Logs estruturados

Veja o [doc 15](./15-comecando-do-zero.md) — em produção, troque
`log.Println` solto por uma lib tipo `slog` (já vem na standard library
desde o Go 1.21) ou `zerolog`, que geram log em JSON com nível
(info/warning/error).

## 5. Deploy

Vantagem real de Go: `go build` gera **um único binário**, sem precisar
de runtime instalado no servidor (diferente de Node/Python, que
precisam do interpretador/runtime lá). Isso torna o deploy mais simples
— um Dockerfile de poucas linhas, ou até só copiar o binário pro
servidor.

## Resumindo

Nenhum desses é obrigatório pra "aprender Go" — são os próximos degraus
depois que rota → controller → model → resposta já estiver automático.
