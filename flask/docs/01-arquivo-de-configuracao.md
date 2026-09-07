# 01. Arquivo de configuração

| Django | Flask | Pra que serve |
|---|---|---|
| `requirements.txt` | `requirements.txt` | igual |
| `settings.py` (gerado automático, ~200 linhas) | `app/config.py` (você cria do zero) | config da app |
| `manage.py runserver` | `flask run` ou `python run.py` | subir o servidor |
| `INSTALLED_APPS` | não existe | Flask não tem conceito de "app registrado" |

Diferença de mentalidade: Django te dá `settings.py` pronto com 30
configs. Flask te dá **nada** — você cria um dicionário ou classe de
config e injeta na aplicação:

```python
# app/config.py
import os

class Config:
    PORT = int(os.getenv("PORT", 3000))
```

Veja o real em [`api-exemplo/app/config.py`](../api-exemplo/app/config.py).

Rodar: `python run.py` (equivalente ao `manage.py runserver`, mas o
arquivo `run.py` é convenção sua, não vem pronto).
