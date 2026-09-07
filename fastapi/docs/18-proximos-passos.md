# 18. Próximos passos (depois de entender este exemplo)

Mesma lógica das outras stacks: mapa dos próximos degraus, sem se
aprofundar agora.

## 1. Banco de dados de verdade

Troque a lista em memória (`app/models/user.py`) por SQLAlchemy + banco
real. Veja o [doc 11](./11-migrations.md) (SQLAlchemy + Alembic) — lá já
mostra a diferença entre o model Pydantic (validação) e o model
SQLAlchemy (banco).

## 2. Autenticação

FastAPI tem suporte de fábrica pra OAuth2/JWT via `fastapi.security` —
mais integrado que nas outras 3 stacks. Fluxo comum: rota `/token`
recebe login/senha, devolve JWT; rotas protegidas usam
`Depends(oauth2_scheme)` pra exigir o token.

## 3. Validação mais robusta

Você já tem a validação automática via Pydantic (doc 10) — o próximo
passo aqui é usar `@field_validator` pra regra customizada:
```python
from pydantic import field_validator

class UserCreate(BaseModel):
    email: str

    @field_validator("email")
    def valida_email(cls, v):
        if "@" not in v:
            raise ValueError("email inválido")
        return v
```

## 4. Logs estruturados

Veja o [doc 15](./15-comecando-do-zero.md) — configure o `logging` do
Python com formato JSON, ou use `structlog`, pra logs mais fáceis de
buscar em produção.

## 5. Deploy

Uvicorn sozinho não é recomendado pra produção com alto tráfego — o
padrão é **Gunicorn gerenciando múltiplos workers Uvicorn**:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```
Serviços que simplificam isso: Railway, Render, Fly.io.

## Resumindo

Nenhum desses é obrigatório pra "aprender FastAPI" — são os próximos
degraus depois que rota → model → resposta já estiver automático.
