# 17. Variáveis de ambiente e segredos

Mesma regra de ouro: **segredo nunca vai pro código, nunca vai pro Git**
— provavelmente você já segue isso no Django com `django-environ` ou
similar, a ideia é idêntica aqui.

## O que é "segredo"

Senha de banco, `SECRET_KEY` de assinatura de token, chave de API
externa. `PORT=3000` não é segredo.

## `.env` (real) vs `.env.example` (modelo)

```
.env           → valores reais, IGNORADO pelo Git
.env.example   → mesmas chaves, valores fake, COMMITADO
```

Este `api-exemplo/` só usa `PORT`, então não tem segredo de verdade —
mas se adicionar banco (doc 11, migrations), a `DATABASE_URL` viraria o
primeiro segredo real do projeto, e seguiria essa mesma regra.

Adicione no `.gitignore`:
```
.env
venv/
__pycache__/
```

## Se um segredo vazar no Git — troque o segredo, não só o arquivo

```bash
git log -p -- .env   # se .env foi commitado algum dia, fica no histórico pra sempre
```

## Em produção, normalmente não sobe `.env`

O serviço de hospedagem (Railway, Render, AWS, etc.) injeta as variáveis
direto no ambiente do processo — `os.getenv("DATABASE_URL")` continua
funcionando igual, só que sem arquivo `.env` físico no servidor.

## `pydantic-settings` — se quiser validar as variáveis também

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port: int = 3000
    database_url: str  # sem valor padrão = obrigatório, erro se faltar

settings = Settings()  # já lê do .env sozinho e valida os tipos
```
Detecta na hora de subir o servidor se falta alguma variável obrigatória
— em vez de descobrir só quando o código tentar usá-la e quebrar.
