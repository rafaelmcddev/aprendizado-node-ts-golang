# 10. Classes, métodos e properties

Igual FastAPI: Python puro você já conhece. A diferença aqui é que o
`api-exemplo/` deste projeto usa **dict puro** no lugar de classe (viu em
`app/models/user.py`) — de propósito, pra não precisar de ORM. Mas numa
API Flask real, o normal é usar classe via **Flask-SQLAlchemy**.

## Classe Python normal (revisão rápida, você já sabe isso)

```python
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def greet(self) -> str:
        return f"Olá, {self.name}"

    @staticmethod
    def from_email(email: str) -> "User":
        return User(0, email.split("@")[0])

    @classmethod
    def vazio(cls) -> "User":
        return cls(0, "")

    @property
    def email_fake(self) -> str:
        return f"{self.name.lower()}@example.com"
```

Nada muda aqui — é o Python que você já usa em Django.

## Se fosse usar Flask-SQLAlchemy (o "model" de verdade do Flask)

```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def greet(self) -> str:              # método normal, mistura numa boa
        return f"Olá, {self.name}"
```

| Django | Flask-SQLAlchemy |
|---|---|
| `class User(models.Model):` | `class User(db.Model):` |
| `models.CharField(max_length=80)` | `db.Column(db.String(80))` |
| campo vira "property" automática (`user.name`) | igual — `user.name` também funciona direto |
| método normal dentro do model | igual, funciona igual |

A grande diferença pro Django: você **instala e configura** o
Flask-SQLAlchemy (`pip install flask-sqlalchemy`), não vem pronto no
framework. Por isso o `api-exemplo/` deste repositório usa dict simples
— pra não misturar "aprender Flask" com "aprender SQLAlchemy" ao mesmo
tempo.
