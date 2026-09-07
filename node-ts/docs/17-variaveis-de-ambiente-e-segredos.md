# 17. Variáveis de ambiente e segredos

Regra de ouro, igual em qualquer linguagem: **segredo nunca vai pro
código, nunca vai pro Git.**

## O que é "segredo"

Senha de banco, chave de API, token de terceiro, qualquer coisa que se
vazar dá acesso a algo. `PORT=3000` não é segredo. `DATABASE_PASSWORD=...`
é.

## As duas peças: `.env` (real, nunca commitado) e `.env.example` (modelo, sempre commitado)

```
.env           → valores reais, no seu computador, IGNORADO pelo Git
.env.example   → mesmas chaves, valores fake/vazios, COMMITADO no Git
```

Este projeto já vem assim — veja
[`.env.example`](../api-exemplo/.env.example) commitado e
[`.gitignore`](../api-exemplo/.gitignore) ignorando o `.env` real:
```
node_modules/
dist/
.env
```

Quando alguém clona o repositório, copia `.env.example` pra `.env` e
preenche com os valores reais dela — é o que a instrução `cp .env.example
.env` no README de cada `api-exemplo/` já faz.

## Se um segredo vazar no Git — mesmo apagando depois, ele fica no histórico

```bash
git log -p -- .env    # se algum dia .env foi commitado, ele TODO aparece aqui
```
Apagar o arquivo num commit novo não remove do histórico. Se um segredo
real vazar, a ação certa é **trocar o segredo** (nova senha, nova chave
de API) — não só apagar o arquivo.

## Em produção, `.env` normalmente nem existe

Em produção (Render, Railway, Vercel, AWS, etc.), você configura as
variáveis direto no painel do serviço de hospedagem — não sobe arquivo
`.env` nenhum pro servidor. O código lê `process.env.X` do mesmo jeito,
só que quem populou a variável foi o serviço de hospedagem, não um
arquivo local.
