# 15. Começando um projeto do zero (sem copiar o `api-exemplo/`)

Sequência real se você fosse começar um projeto Flask novo, sozinho.

## 1. Comandos iniciais

```bash
mkdir meu-projeto && cd meu-projeto
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install flask
pip freeze > requirements.txt
```

Sem `django-admin startproject` — Flask não tem scaffold oficial, você
monta as pastas na mão (é o "microframework": vem só o essencial).

## 2. Sequência de arquivos (nessa ordem)

1. `app/config.py` → config da app
2. `app/models/*.py` → dados, não depende de mais nada
3. `app/routes/*.py` → Blueprint, depende do model
4. `app/__init__.py` → `create_app()`, registra os Blueprints (depende de tudo acima)
5. `run.py` → chama `create_app()` e sobe o servidor

Mesma ordem usada no `api-exemplo/` deste repositório.

## 3. Rodar

```bash
python run.py
# ou
flask --app run run --debug
```

## 4. Onde ficam os logs

Com `debug=True`, o Werkzeug (servidor de desenvolvimento do Flask)
imprime uma linha por requisição no **terminal**:
```
127.0.0.1 - - [15/Jan/2024 10:30:00] "GET /users/ HTTP/1.1" 200 -
```

Sem arquivo automático — diferente do Laravel
(`storage/logs/laravel.log`). Pra gravar em arquivo, configure o módulo
`logging` do próprio Python:
```python
import logging
logging.basicConfig(filename="app.log", level=logging.INFO)
app.logger.info("servidor iniciado")
```
