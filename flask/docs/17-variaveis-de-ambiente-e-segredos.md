# 17. Variáveis de ambiente e segredos

Mesma regra de ouro: **segredo nunca vai pro código, nunca vai pro Git.**

## O que é "segredo"

Senha de banco, `SECRET_KEY` (usada pelo Flask pra assinar sessão/cookie),
chave de API externa. `PORT=3000` não é segredo.

## `.env` (real) vs `.env.example` (modelo)

```
.env           → valores reais, IGNORADO pelo Git
.env.example   → mesmas chaves, valores fake, COMMITADO
```

Adicione no `.gitignore`:
```
.env
venv/
__pycache__/
```

## Atenção especial: `app.config["SECRET_KEY"]`

```python
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
```
Essa chave especificamente assina cookies de sessão e tokens CSRF. Se
vazar, alguém pode forjar sessão de outro usuário — trate com o mesmo
cuidado de senha de banco, nunca hardcoded no código:
```python
app.config["SECRET_KEY"] = "abc123"  # NUNCA faça isso, nem "só por enquanto"
```

## Se um segredo vazar no Git — troque o segredo, não só o arquivo

```bash
git log -p -- .env   # fica no histórico pra sempre, mesmo apagando depois
```

## Em produção, normalmente não sobe `.env`

O serviço de hospedagem injeta as variáveis direto no ambiente —
`os.getenv("SECRET_KEY")` funciona igual, sem arquivo físico no
servidor.
