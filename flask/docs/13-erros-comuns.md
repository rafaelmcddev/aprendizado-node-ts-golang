# 13. Erros comuns (os que todo mundo bate no começo)

## 1. Blueprint criado mas a rota não existe

**Causa**: esqueceu `app.register_blueprint(bp)` dentro de
`create_app()`. Igual FastAPI, Flask não registra nada sozinho.

**Correção**: toda `Blueprint` nova precisa do `register_blueprint`
explícito em `app/__init__.py`.

## 2. `/users` funciona mas `/users/` dá redirect (ou vice-versa)

**Causa**: Flask trata rota **com** barra no final e **sem** barra no
final como coisas diferentes. Se você declarou `@bp.route("/users/")`,
acessar `/users` (sem barra) faz redirect automático; o contrário não
tem redirect e dá 404.

**Correção**: escolha um padrão (este projeto usa sempre **com** barra
no final, tipo `/users/`) e siga ele em toda rota.

## 3. `request.get_json()` retorna `None`

**Causa**: o cliente não mandou o header `Content-Type: application/json`
no POST — sem isso, o Flask não tenta interpretar o body como JSON.

**Correção**: sempre mande `Content-Type: application/json` (no Postman,
na aba Headers; no `curl`, com `-H "Content-Type: application/json"`).

## 4. `RuntimeError: Working outside of application context`

**Causa**: tentou acessar algo de dentro do Flask (tipo `db` ou
`current_app`) fora de uma requisição — comum em scripts soltos ou
testes mal configurados.

**Correção**: envolva com `with app.app_context():` quando for código
fora do ciclo normal de requisição.

## 5. Dado "sumiu" ou virou de outro usuário — race condition

**Causa**: este projeto guarda os usuários numa lista Python global
(`_users` em `app/models/user.py`). Isso funciona numa requisição de
cada vez, mas **não é seguro** com múltiplas requisições simultâneas
alterando a lista ao mesmo tempo — problema real em qualquer app que
guarda estado em variável global do processo.

**Correção**: em projeto de verdade, isso é resolvido usando banco de
dados (que trata concorrência por você), não variável em memória — é
exatamente por isso que exemplos didáticos como este evitam simular
carga real.

## 6. Editou o código e o servidor não atualiza

**Causa**: rodou sem `debug=True` (ou sem `FLASK_DEBUG=1`).

**Correção**: `app.run(debug=True)` em desenvolvimento — também te dá a
página de erro interativa (veja o [doc 07](./07-debug.md)).
