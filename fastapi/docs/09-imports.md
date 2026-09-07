# 09. Onde ficam os imports

Igual Django/Python puro: topo do arquivo.

```python
from fastapi import APIRouter, HTTPException   # biblioteca externa
from app.models.user import User, find_by_id   # arquivo seu (caminho de pacote)
```

Diferença pro Django: FastAPI não tem app registrado em `INSTALLED_APPS`
nem import automático de nada. Se o arquivo existe mas você não importou,
ele simplesmente **não roda** — nenhuma rota dele é registrada, e não dá
erro nenhum avisando isso (é o erro mais comum de quem começa: criar um
router novo e esquecer o `include_router` no `main.py`).

Precisa de `__init__.py` vazio em cada pasta pra virar pacote Python
importável — igual toda estrutura Django que você já usa.
