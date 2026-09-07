# 05. Model / View / Controller

Flask não tem convenção oficial de pastas (diferente do Django "MTV").
Este projeto organiza assim:

| Camada | Pasta | Django equivalente |
|---|---|---|
| Model | `app/models/` | `models.py` — mas sem ORM, é dado puro |
| Controller | `app/routes/` (Blueprints) | `views.py` |
| View (template) | `app/views/` (aqui HTML estático) | `templates/` |

Sem ORM = sem `class User(models.Model)`. Aqui `models/user.py` é só
funções manipulando uma lista Python:

```python
# app/models/user.py
def find_by_id(user_id):
    return next((u for u in _users if u["id"] == user_id), None)
```

Se fosse projeto real com banco, entraria SQLAlchemy aqui — mas o
propósito deste repo é o fluxo, não SQL.

Veja o real em [`api-exemplo/app/models/user.py`](../api-exemplo/app/models/user.py).
