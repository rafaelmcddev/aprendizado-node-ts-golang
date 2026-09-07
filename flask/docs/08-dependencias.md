# 08. Como instalar e usar dependências

Idêntico ao fluxo que você já usa em Django:

```bash
python -m venv venv
source venv/bin/activate
pip install flask
pip freeze > requirements.txt
pip install -r requirements.txt
```

Diferença pro Django: Flask **vem com servidor de desenvolvimento
embutido** (igual Django), mas o comando muda:
```bash
flask --app app run --debug
# ou, se você definir um run.py:
python run.py
```

Uso normal depois de instalado:
```python
from flask import Flask, jsonify   # biblioteca instalada
from app.models.user import find_all  # arquivo seu
```
