# 01. Arquivo de configuração

| Django | FastAPI | Pra que serve |
|---|---|---|
| `requirements.txt` | `requirements.txt` | igual — nada muda aqui |
| `settings.py` | `app/config.py` (você cria) | config da app — não existe `settings.py` de fábrica |
| `.env` + `django-environ` | `.env` + `pydantic-settings` (ou manual) | variáveis de ambiente |
| `manage.py` | não existe | FastAPI não tem CLI de projeto; você roda com `uvicorn` direto |

Não existe `settings.py` mágico com 200 linhas pré-geradas. Você mesmo
cria `app/config.py`, geralmente pequeno, usando `pydantic-settings` pra
já validar as variáveis (tipo um `settings.py` com type hints).

Veja o real em [`api-exemplo/app/config.py`](../api-exemplo/app/config.py).

Rodar o projeto: `uvicorn app.main:app --reload` (equivalente ao
`python manage.py runserver`, mas o `--reload` você pede explicitamente).
