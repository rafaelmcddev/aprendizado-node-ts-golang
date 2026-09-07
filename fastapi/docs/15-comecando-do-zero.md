# 15. Começando um projeto do zero (sem copiar o `api-exemplo/`)

Sequência real se você fosse começar um projeto FastAPI novo, sozinho.

## 1. Comandos iniciais

```bash
mkdir meu-projeto && cd meu-projeto
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install fastapi "uvicorn[standard]"
pip freeze > requirements.txt
```

Sem `django-admin startproject` — não existe scaffold oficial, você cria
as pastas na mão.

## 2. Sequência de arquivos (nessa ordem)

1. `app/config.py` → lê variáveis de ambiente
2. `app/models/*.py` → schemas Pydantic (dados), não depende de mais nada
3. `app/routers/*.py` → depende do model
4. `app/main.py` → cria o `FastAPI()`, faz `include_router` (depende de tudo acima)

Mesma ordem usada no `api-exemplo/` deste repositório.

## 3. Rodar

```bash
uvicorn app.main:app --reload
```
`app.main:app` = "no arquivo `app/main.py`, pegue a variável `app`".

## 4. Onde ficam os logs

O `uvicorn` já imprime, por padrão, uma linha por requisição no
**terminal** (parecido com o `runserver` do Django):
```
INFO:     127.0.0.1:52341 - "GET /users/ HTTP/1.1" 200 OK
```

Não grava em arquivo sozinho — diferente do Laravel
(`storage/logs/laravel.log`). Pra gravar em arquivo:
```bash
uvicorn app.main:app --log-config log_config.yaml   # configuração customizada
# ou, mais simples:
uvicorn app.main:app > saida.log 2>&1
```
