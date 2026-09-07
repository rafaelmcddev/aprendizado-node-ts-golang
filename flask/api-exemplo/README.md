# API de exemplo — Flask

CRUD simples de usuários, sem banco, usando Blueprint pra organizar rota
por recurso.

## Rodar

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Abra `http://localhost:3000` → front simples.
Abra `http://localhost:3000/users/` → JSON puro.

## Testar

```bash
pytest
```

> Também dá pra testar pelo Postman: collection pronta em [`/postman`](../../postman).

## Endpoints

| Método | Rota | O que faz |
|---|---|---|
| GET | `/users/` | lista todos |
| GET | `/users/<id>` | busca um |
| POST | `/users/` | cria (body: `{ "name": "...", "email": "..." }`) |

## Estrutura

```
app/
  config.py     → config da app (você cria, sem settings.py de fábrica)
  models/       → dados
  routes/       → Blueprint (rota + lógica juntos)
  views/        → front estático
  __init__.py   → create_app(), monta a aplicação
run.py          → sobe o servidor
tests/          → testes com pytest + test_client()
```
