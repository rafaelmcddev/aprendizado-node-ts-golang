# 12. Funções e estruturas built-in mais usadas

Você já usa Python todo dia com Django, então isso aqui não é revisão de
básico — é foco no que aparece muito em **API** (FastAPI) e que às vezes
fica esquecido no dia a dia de Django puro.

## 1. Comprehensions (list / dict / set)

```python
pares = [n for n in range(10) if n % 2 == 0]
por_id = {u.id: u for u in users}          # dict comprehension — ótimo pra indexar por id
ids_unicos = {u.id for u in users}          # set comprehension
```
Você já usa isso, mas o `dict` comprehension pra indexar por id é o
padrão mais comum em código de API pra evitar `O(n)` toda hora buscando
numa lista.

## 2. `*args` e `**kwargs`

```python
def rota(*args, **kwargs):
    print(args)    # tupla com posicionais
    print(kwargs)  # dict com nomeados
```
Aparece direto em decorators e em assinatura de dependência do FastAPI.

## 3. `enumerate` e `zip`

```python
for i, user in enumerate(users):
    print(i, user.name)

for user, role in zip(users, roles):
    print(user.name, role)
```

## 4. `with` — context manager

```python
with open("arquivo.txt") as f:
    conteudo = f.read()
# fecha sozinho, mesmo se der erro
```
Em FastAPI aparece muito em `Depends` com `yield` (dependência que abre
sessão de banco e fecha depois — é basicamente um context manager por
trás dos panos).

## 5. `collections.defaultdict` e `Counter`

```python
from collections import defaultdict, Counter

agrupado = defaultdict(list)
for u in users:
    agrupado[u.role].append(u)   # não precisa checar se a chave existe

Counter([u.role for u in users])  # {'admin': 2, 'user': 5}
```
Evita o clássico `if chave not in dict: dict[chave] = []`.

## 6. `dataclasses` — "Pydantic sem validação"

```python
from dataclasses import dataclass

@dataclass
class Ponto:
    x: int
    y: int
```
Gera `__init__` automático igual o `BaseModel` do Pydantic (doc 10), mas
**sem validar nada**. Use quando não precisa validar entrada de API, só
quer uma classe de dados simples.

## 7. `Optional` / `X | None` — tipo opcional

```python
def busca(id: int) -> User | None:   # Python 3.10+
    ...
```
Muito usado em assinatura de função e em campo de Pydantic — mesma ideia
de `nullable=True` do Django, mas explícito no tipo.

## 8. `sorted(..., key=...)`

```python
sorted(users, key=lambda u: u.name)
sorted(users, key=lambda u: u.age, reverse=True)
```

## 9. f-strings com expressão dentro

```python
f"{user.name.upper()} tem {user.age} anos"
f"{valor:.2f}"   # formata com 2 casas decimais
```

## 10. `httpx` — chamar outra API de dentro do FastAPI

```python
import httpx

async def busca_externa():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.exemplo.com/dados")
        return r.json()
```
Equivalente assíncrono do `requests` (que você já deve conhecer do
Django) — usado quando seu backend precisa chamar outro serviço.
