# 12. Funções e estruturas built-in mais usadas

As 10 que você vai usar toda semana escrevendo backend em Node/TS.
Comparando sempre com o que você já faz em Python.

## 1. `Array.map` — transforma cada item

```ts
const dobrados = [1, 2, 3].map((n) => n * 2); // [2, 4, 6]
```
Python: `[n * 2 for n in [1, 2, 3]]`

## 2. `Array.filter` — filtra itens

```ts
const pares = [1, 2, 3, 4].filter((n) => n % 2 === 0); // [2, 4]
```
Python: `[n for n in [1,2,3,4] if n % 2 == 0]`

## 3. `Array.reduce` — acumula num valor só

```ts
const total = [10, 20, 30].reduce((soma, n) => soma + n, 0); // 60
```
Python: `sum([10, 20, 30])` (pra soma simples) ou `functools.reduce`

## 4. `Array.find` — acha o primeiro que bate

```ts
const user = users.find((u) => u.id === 1);
```
Python: `next((u for u in users if u.id == 1), None)`

## 5. `Object.keys` / `Object.values` / `Object.entries`

```ts
const obj = { a: 1, b: 2 };
Object.keys(obj);    // ['a', 'b']
Object.values(obj);  // [1, 2]
Object.entries(obj); // [['a', 1], ['b', 2]]
```
Python: `obj.keys()`, `obj.values()`, `obj.items()`

## 6. `JSON.stringify` / `JSON.parse`

```ts
JSON.stringify({ name: 'Ada' }); // '{"name":"Ada"}'
JSON.parse('{"name":"Ada"}');    // { name: 'Ada' }
```
Python: `json.dumps(...)` / `json.loads(...)`

## 7. `Map` — dicionário de verdade (diferente de `Object`)

```ts
const cache = new Map<string, number>();
cache.set('a', 1);
cache.get('a');      // 1
cache.has('a');      // true
```
Python: `dict()`. Use `Map` em vez de `{}` quando as chaves não são
sempre string, ou quando você precisa manter a ordem de inserção
garantida e iterar com frequência.

## 8. `Set` — valores únicos

```ts
const ids = new Set([1, 2, 2, 3]); // {1, 2, 3}
ids.has(2); // true
```
Python: `set([1, 2, 2, 3])`

## 9. `Promise.all` — roda várias promises em paralelo

```ts
const [users, posts] = await Promise.all([
  fetchUsers(),
  fetchPosts(),
]);
```
Python (`asyncio`): `await asyncio.gather(fetch_users(), fetch_posts())`

## 10. `try/catch` com `async/await`

```ts
async function getUser(id: number) {
  try {
    const res = await fetch(`/users/${id}`);
    return await res.json();
  } catch (err) {
    console.error('erro ao buscar usuário:', err);
    throw err;
  }
}
```
Python: `try/except` em volta de um `await` normal — mesma ideia,
sintaxe quase igual.
