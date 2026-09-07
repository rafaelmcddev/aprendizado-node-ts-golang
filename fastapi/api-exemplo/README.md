# API de exemplo — FastAPI

CRUD simples de usuários, sem banco, com validação automática via
Pydantic.

## Rodar

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abra `http://localhost:8000` → front simples.
Abra `http://localhost:8000/docs` → Swagger, testa a API sem precisar de nada.

## Testar

```bash
pytest
```

## Endpoints

| Método | Rota | O que faz |
|---|---|---|
| GET | `/users/` | lista todos |
| GET | `/users/{id}` | busca um |
| POST | `/users/` | cria (body: `{ "name": "...", "email": "..." }`) |

## Estrutura

```
app/
  config.py    → lê variáveis de ambiente
  models/      → schema Pydantic + dados
  routers/     → rota + lógica (urls.py + views.py juntos)
  views/       → front estático
  main.py      → cria o FastAPI(), inclui os routers
tests/         → testes com pytest + TestClient
```
