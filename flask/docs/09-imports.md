# 09. Onde ficam os imports

Igual Python/Django: topo do arquivo.

```python
from flask import Blueprint, jsonify, request   # biblioteca externa
from app.models import user as user_model        # arquivo seu
```

Igual FastAPI: precisa de `__init__.py` (vazio ou não) em cada pasta pra
virar pacote importável — mesma regra do Django.

Diferença pro Django: não existe import automático de `models.py` ou
`views.py` por causa de `INSTALLED_APPS`. Se você criar um Blueprint novo
e esquecer de importar e registrar ele em `app/__init__.py`
(`app.register_blueprint(...)`), a rota simplesmente não existe — sem
erro, sem aviso.
