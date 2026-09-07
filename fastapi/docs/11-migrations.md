# 11. Migrations

Este projeto não usa banco (dados em memória, de propósito). No Django,
migration vem de fábrica. No FastAPI, **não vem nada** — você monta a
peça sozinho, com SQLAlchemy (o ORM) + Alembic (as migrations).

## Ferramenta: Alembic

Alembic é pro SQLAlchemy o que o sistema de migrations é pro Django ORM
— só que é um pacote **separado**, você instala e configura na mão.

```bash
pip install sqlalchemy alembic
alembic init alembic          # cria a estrutura de pastas (1x, no início)
```

## Fluxo comparado com Django

| Django | FastAPI + SQLAlchemy + Alembic |
|---|---|
| `models.py` | `app/models/user.py`, mas com classe SQLAlchemy (`Base`), não Pydantic |
| `python manage.py makemigrations` | `alembic revision --autogenerate -m "cria users"` |
| `python manage.py migrate` | `alembic upgrade head` |
| desfazer última migration | `alembic downgrade -1` |
| pasta `migrations/` | pasta `alembic/versions/` |

## Cuidado: o model Pydantic ≠ o model do banco

No FastAPI, o `BaseModel` (Pydantic, que você viu no doc 10) é só pra
**validar request/response** — não é ligado a tabela nenhuma. Pra ter
migration, você precisa de **outra** classe, agora em SQLAlchemy:

```python
# app/db_models/user.py (SQLAlchemy — gera tabela de verdade)
from sqlalchemy import Column, Integer, String
from app.database import Base

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
```

Essa classe `UserDB` (SQLAlchemy) é o equivalente direto do
`class User(models.Model)` do Django. A classe `User(BaseModel)`
(Pydantic) que você já tem no projeto é só a "casca" de validação da API
— comum ter as duas coexistindo em projeto real, uma convertendo pra
outra.

## Resumindo pra você que vem de Django

Onde o Django te dá **uma** classe fazendo tudo (model = banco = validação
de formulário), no ecossistema FastAPI isso normalmente vira **duas
classes**: uma SQLAlchemy (banco + migration) e uma Pydantic (validação
de entrada/saída da API). Mais peças pra montar, mais controle sobre cada
uma.
