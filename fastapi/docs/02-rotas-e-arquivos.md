# 02. Rota → qual arquivo é chamado

Não tem `urls.py` centralizado. Cada arquivo de rota (aqui chamado de
"router", equivalente a um `urls.py` + `views.py` por app do Django)
declara suas próprias rotas com decorator:

```python
# app/routers/user.py
@router.get("/{id}")
def show(id: int):
    ...
```

Caminho até achar o código:

1. `app/main.py` → cria a instância `FastAPI()`, faz `include_router(...)`
2. `app/routers/user.py` → define `GET /users/{id}` → função `show`
3. A própria função `show` já é o código que executa (não separa
   "view" de "controller" como o Django faz)

Comparando com Django: `router.get(...)` é tipo o `path()` do `urls.py` +
a função de `views.py`, tudo junto no mesmo lugar.

Veja o real em [`api-exemplo/app/routers/user.py`](../api-exemplo/app/routers/user.py).
