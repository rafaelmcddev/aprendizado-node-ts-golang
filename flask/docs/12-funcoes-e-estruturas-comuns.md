# 12. Funções e estruturas built-in mais usadas

Mesma base de Python que você já usa com Django — aqui o foco é o que
mais aparece escrevendo API com Flask.

## 1. Comprehensions (list / dict / set)

```python
pares = [n for n in range(10) if n % 2 == 0]
por_id = {u["id"]: u for u in users}   # indexar por id, muito comum em API
ids_unicos = {u["id"] for u in users}
```

## 2. `*args` e `**kwargs`

```python
def rota(*args, **kwargs):
    print(args)    # tupla com posicionais
    print(kwargs)  # dict com nomeados
```
Aparece em decorators customizados e em `**request.args` quando você
quer repassar query params adiante.

## 3. `enumerate` e `zip`

```python
for i, user in enumerate(users):
    print(i, user["name"])

for user, role in zip(users, roles):
    print(user["name"], role)
```

## 4. `with` — context manager

```python
with open("arquivo.txt") as f:
    conteudo = f.read()
```
Em Flask aparece em `with app.app_context():` (necessário fora de uma
requisição, tipo em scripts) e `with app.test_client() as client:` nos
testes.

## 5. `collections.defaultdict` e `Counter`

```python
from collections import defaultdict, Counter

agrupado = defaultdict(list)
for u in users:
    agrupado[u["role"]].append(u)

Counter([u["role"] for u in users])  # {'admin': 2, 'user': 5}
```

## 6. `request` — o objeto mais usado do Flask

```python
from flask import request

request.args.get("page")       # query string: /users?page=2
request.get_json()             # body JSON do POST
request.headers.get("Authorization")
```
Equivalente ao `request` do Django, só que os métodos têm nomes
diferentes (`request.GET.get(...)` no Django vira `request.args.get(...)`
no Flask).

## 7. `Optional` / `X | None` — tipo opcional

```python
def busca(id: int) -> dict | None:   # Python 3.10+
    ...
```
Flask não obriga tipagem (diferente do FastAPI), mas usar type hints
ajuda seu editor a te avisar de erro antes de rodar.

## 8. `sorted(..., key=...)`

```python
sorted(users, key=lambda u: u["name"])
sorted(users, key=lambda u: u["age"], reverse=True)
```

## 9. f-strings com expressão dentro

```python
f"{user['name'].upper()} tem {user['age']} anos"
f"{valor:.2f}"
```

## 10. `jsonify` — o "JSON.stringify" do Flask

```python
from flask import jsonify

return jsonify({"name": "Ada"})            # dict → resposta JSON
return jsonify(users), 201                  # com status code
```
Diferente de `json.dumps` (que só converte pra string), `jsonify` já
monta a resposta HTTP inteira com o `Content-Type` certo — é o que
você usa em toda rota que devolve JSON, como já viu em
[`app/routes/user.py`](../api-exemplo/app/routes/user.py).
