# 10. Classes, métodos e properties

Python puro você já conhece. A parte nova é como o FastAPI **usa** classe
de um jeito específico: os schemas Pydantic que você já viu em
`app/models/user.py`.

## Classe Python normal (revisão rápida, você já sabe isso)

```python
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def greet(self) -> str:                  # método de instância
        return f"Olá, {self.name}"

    @staticmethod
    def from_email(email: str) -> "User":     # método estático
        return User(0, email.split("@")[0])

    @classmethod
    def vazio(cls) -> "User":                 # método de classe
        return cls(0, "")

    @property
    def email_fake(self) -> str:              # property computada
        return f"{self.name.lower()}@example.com"
```

Nada disso muda em FastAPI — é Python puro, igual você já usa.

## A diferença: classe Pydantic (`BaseModel`)

```python
class User(BaseModel):
    id: int
    name: str
    email: str
```

Parece uma classe comum, mas o `BaseModel` por trás gera automaticamente:
- **`__init__`** — você não escreve, ele cria sozinho a partir dos campos
- **validação** — se você passar `id="abc"`, dá erro sozinho
- **serialização** — `user.model_dump()` vira dict, `user.model_dump_json()` vira JSON

| Classe comum | Classe Pydantic (`BaseModel`) |
|---|---|
| você escreve `__init__` | gerado a partir dos campos anotados |
| sem validação — aceita qualquer tipo | valida o tipo de cada campo sozinho |
| `class User(models.Model)` do Django é o mais parecido que você já viu | igual o Django Model, mas sem banco embutido |

Dá pra misturar os dois — método normal dentro de uma classe Pydantic:
```python
class User(BaseModel):
    id: int
    name: str

    def greet(self) -> str:      # método normal, funciona igual
        return f"Olá, {self.name}"
```

Veja isso de verdade em [`api-exemplo/app/models/user.py`](../api-exemplo/app/models/user.py) —
`User` e `UserCreate` são as duas classes Pydantic do projeto.
