# 06. Onde ficam os testes unitários

Igual Django: `pytest`. A diferença é a ferramenta pra simular requisições
HTTP: `TestClient` do próprio FastAPI (equivalente ao `Client` do Django
Test).

Convenção: pasta `tests/`, arquivo `test_*.py`.

```python
# tests/test_user.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_lista_usuarios():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_usuario_inexistente():
    response = client.get("/users/999")
    assert response.status_code == 404
```

Rodar: `pytest` (mesmo comando de sempre).

Se você já usa `pytest` com Django, é o mesmo `assert` puro — só troca o
`Client` do Django pelo `TestClient` do FastAPI.
