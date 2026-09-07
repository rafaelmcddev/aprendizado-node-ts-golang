# 08. Como instalar e usar dependências

Igual Django, mesmo fluxo que você já conhece:

```bash
python -m venv venv
source venv/bin/activate       # ou venv\Scripts\activate no Windows
pip install fastapi "uvicorn[standard]"
pip freeze > requirements.txt  # equivalente ao package-lock.json
pip install -r requirements.txt
```

Diferença pro Django: FastAPI **não vem com servidor embutido**
(`manage.py runserver`). Você precisa de um ASGI server — o padrão é
`uvicorn`:
```bash
uvicorn app.main:app --reload
```
`app.main:app` = "no módulo `app/main.py`, pegue a variável `app`".

Uso normal depois de instalado:
```python
from fastapi import FastAPI          # biblioteca instalada
from app.models.user import User     # arquivo seu, caminho de pacote Python
```
