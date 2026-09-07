# 06. Onde ficam os testes unitários

Igual Django: `pytest`. Pra simular requisição HTTP, Flask usa o próprio
`test_client()` da aplicação (equivalente ao `Client` do Django, ao
`TestClient` do FastAPI).

Convenção: pasta `tests/`, arquivo `test_*.py`.

```python
# tests/test_user.py
from app import create_app

def test_lista_usuarios():
    app = create_app()
    client = app.test_client()
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.get_json()) == 2
```

Rodar: `pytest`.

Diferença sutil pro Django: você monta a `app` na mão em cada teste
(`create_app()`) — não tem um `settings.TEST` mágico rodando por trás.
