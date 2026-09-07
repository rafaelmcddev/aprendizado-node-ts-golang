# 18. Próximos passos (depois de entender este exemplo)

Mesma lógica das outras stacks: mapa dos próximos degraus.

## 1. Banco de dados de verdade

Troque o dict em memória (`app/models/user.py`) por Flask-SQLAlchemy.
Veja o [doc 11](./11-migrations.md) (Flask-Migrate) e o [doc 10](./10-classes-metodos-propriedades.md)
(como fica a classe `db.Model`).

## 2. Autenticação

Lib mais comum: `flask-jwt-extended`. Mesmo fluxo das outras stacks —
rota de login devolve token, rotas protegidas exigem
`Authorization: Bearer <token>` via decorator `@jwt_required()`.

## 3. Validação mais robusta

Este projeto valida na mão (`if not name or not email`). Em projeto
maior, use **Marshmallow** ou **Pydantic mesmo** (dá pra usar Pydantic
fora do FastAPI) pra declarar o schema de validação uma vez só.

## 4. Logs estruturados

Veja o [doc 15](./15-comecando-do-zero.md) — configure o `logging` do
Python com formato JSON em produção, em vez do log de texto simples do
Werkzeug.

## 5. Deploy

O servidor de desenvolvimento do Flask (`app.run()`) **não é seguro pra
produção** — o próprio Flask avisa isso no terminal. Padrão: Gunicorn
na frente:
```bash
gunicorn -w 4 "app:create_app()"
```
Serviços que simplificam: Railway, Render, Fly.io.

## Resumindo

Nenhum desses é obrigatório pra "aprender Flask" — são os próximos
degraus depois que rota → model → resposta já estiver automático.
