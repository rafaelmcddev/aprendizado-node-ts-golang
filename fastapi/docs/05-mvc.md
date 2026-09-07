# 05. Model / View / Controller

Django usa "MTV" (Model-Template-View, onde "View" = o que outros
frameworks chamam de Controller). FastAPI não impõe nome nenhum — você
organiza como quiser. Este projeto usa:

| Camada | Pasta | Django equivalente |
|---|---|---|
| Model | `app/models/` | `models.py` — mas aqui sem ORM, é dado + Pydantic schema |
| Controller | `app/routers/` | `views.py` (a "View" do Django é o Controller de todo mundo) |
| View (template) | não tem, projeto é API pura | `templates/` |

Detalhe importante: no FastAPI, o "Model" costuma ter **duas partes**:
- **Schema Pydantic**: define o formato dos dados (validação de entrada/saída)
- **Dado de verdade**: se tivesse banco, seria SQLAlchemy; aqui é uma lista

```python
# app/models/user.py
class User(BaseModel):   # schema Pydantic — valida formato
    id: int
    name: str
    email: str
```

Veja os dois se misturando em [`api-exemplo/app/models/user.py`](../api-exemplo/app/models/user.py).
