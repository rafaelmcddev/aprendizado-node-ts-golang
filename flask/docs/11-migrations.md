# 11. Migrations

Este projeto não usa banco (dict em memória, de propósito). Pra migration
de verdade em Flask, a ferramenta padrão é **Flask-Migrate** — que por
trás é o mesmo Alembic do FastAPI, só com comandos mais parecidos com o
Django.

## Instalar e configurar

```bash
pip install flask-sqlalchemy flask-migrate
```

```python
# app/__init__.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    return app
```

## Comandos — este é o mais parecido com Django das 4 stacks

| Django | Flask-Migrate |
|---|---|
| `python manage.py makemigrations` | `flask db migrate -m "cria users"` |
| `python manage.py migrate` | `flask db upgrade` |
| desfazer última | `flask db downgrade` |
| pasta `migrations/` | pasta `migrations/` (nome igual!) |
| primeira vez no projeto | `flask db init` (Django não tem isso, já vem pronto) |

## Fluxo completo do zero

```bash
flask db init                          # 1x só, cria a pasta migrations/
flask db migrate -m "cria tabela users"  # gera o arquivo de migration
flask db upgrade                        # aplica no banco
```

## Model precisa ser classe SQLAlchemy, não dict

O `api-exemplo/` deste repo usa dict em `app/models/user.py` só pra focar
no fluxo. Pra migration funcionar de verdade, o model vira classe (igual
mostrado no [doc 10](./10-classes-metodos-propriedades.md)):

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
```

É o `flask db migrate` que lê essa classe e gera o SQL sozinho — igual o
`makemigrations` do Django lê o `models.py`.

## Resumindo pra você que vem de Django

De todas as 4 stacks deste repositório, **Flask-Migrate é a mais parecida
com o fluxo do Django** que você já conhece — só precisa instalar e
inicializar na mão (`flask db init`), o resto é quase copiar o hábito.
