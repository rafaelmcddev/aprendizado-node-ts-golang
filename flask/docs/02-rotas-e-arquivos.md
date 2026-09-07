# 02. Rota → qual arquivo é chamado

Flask usa **Blueprint** pra organizar rotas por módulo — é o mais
parecido com "um app do Django" que existe no Flask, mas bem mais simples
(sem `models.py`/`admin.py`/`apps.py` obrigatórios, só rotas).

```python
# app/routes/user.py
bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("/<int:id>", methods=["GET"])
def show(id):
    ...
```

Caminho até achar o código:

1. `app/__init__.py` → `create_app()`, registra os Blueprints
2. `app/routes/user.py` → define `GET /users/<id>` → função `show`
3. A função `show` já é o código que roda (Flask também não separa
   "view" de "controller")

Comparando com Django: `Blueprint` é tipo um `urls.py` + `views.py` de um
app específico, só que sem o resto da estrutura de app do Django em volta.

Veja o real em [`api-exemplo/app/routes/user.py`](../api-exemplo/app/routes/user.py).
