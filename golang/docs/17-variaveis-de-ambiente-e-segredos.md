# 17. Variáveis de ambiente e segredos

Mesma regra de ouro de sempre: **segredo nunca vai pro código, nunca vai
pro Git.**

## O que é "segredo"

Senha de banco, chave de API, token de terceiro. `PORT=3000` não é
segredo, `DATABASE_URL=postgres://user:senha@host/db` é (repare que a
senha está embutida na própria URL — cuidado redobrado com isso).

## `.env` (real) vs `.env.example` (modelo)

Este projeto de exemplo em Go não usa `.env` (lê `PORT` direto do
sistema, veja [`config/config.go`](../api-exemplo/config/config.go)),
mas se seu projeto crescer e precisar de mais variáveis, a mesma regra
das outras stacks se aplica:
```
.env           → valores reais, IGNORADO pelo Git
.env.example   → mesmas chaves, valores fake, COMMITADO
```

Adicione no `.gitignore`:
```
.env
```

## Se um segredo vazar no Git — a ação certa é trocar o segredo

```bash
git log -p -- .env   # se .env foi commitado algum dia, aparece aqui pra sempre
```
Apagar num commit novo não some do histórico. Vazou senha de banco de
verdade? Troque a senha, não só o arquivo.

## Em produção, geralmente não tem `.env` nenhum

Rodando em container/serviço de hospedagem, as variáveis são injetadas
pelo próprio ambiente (`docker run -e PORT=8080 ...`, ou configuradas no
painel do serviço) — `os.Getenv("PORT")` funciona igual, só que quem
preencheu o valor não foi um arquivo local.
