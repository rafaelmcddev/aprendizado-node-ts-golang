# 00-2. Sintaxe estranha do TypeScript (o que ninguém explica de cara)

Você vem de Python/PHP — nada disso existe do jeito que aparece aqui. São
6 coisas pequenas que aparecem toda hora no código deste projeto.

## 1. `req: Request, res: Response` — tipo depois de `:`

```ts
export function show(req: Request, res: Response) { ... }
```

Não é atribuição de valor, é **anotação de tipo**. Diz "esse parâmetro
`req` é do tipo `Request`". Equivalente ao type hint do Python:

| Python | TypeScript |
|---|---|
| `def show(req: Request, res: Response):` | `function show(req: Request, res: Response) {` |

A diferença: em Python o type hint é só documentação (ninguém te impede
de passar outra coisa em runtime). Em TypeScript, o compilador **erra**
se você passar tipo errado — antes mesmo de rodar.

## 2. `const` e `let` — não existe `var` solto tipo PHP

```ts
const id = Number(req.params.id);  // nunca muda de valor depois
let contador = 0;                   // pode mudar de valor depois
```

Equivalente ao `$var = ...` do PHP, mas dividido em dois: `const` trava a
variável (não pode reatribuir), `let` permite reatribuir. Python não tem
essa distinção — toda variável em Python pode ser reatribuída. Use `const`
por padrão; só use `let` quando o valor realmente vai mudar.

## 3. `=>` — arrow function

```ts
users.find((u) => u.id === id)
```

É uma função anônima, só que mais curta. Equivalente ao `lambda` do
Python:

| Python | TypeScript |
|---|---|
| `lambda u: u.id == id` | `(u) => u.id === id` |

`find` aqui é equivalente ao `next(filter(...))` do Python — acha o
primeiro item que bate com a condição.

## 4. `const { name, email } = req.body;` — destructuring

```ts
const { name, email } = req.body;
// é o mesmo que:
const name = req.body.name;
const email = req.body.email;
```

Puxa várias propriedades de um objeto de uma vez. Não existe exatamente
isso em Python/PHP — o mais parecido é o unpacking de dict do Python,
mas por nome de chave, não por posição.

## 5. `...data` — spread

```ts
const user: User = { id: users.length + 1, ...data };
```

"Espalha" todas as propriedades de `data` dentro do novo objeto.
Equivalente ao `**data` do Python (`{**data, "id": novo_id}`), só que a
ordem dos campos muda a prioridade: quem vem depois sobrescreve quem veio
antes.

## 6. `??` e `Omit<User, 'id'>`

```ts
Number(process.env.PORT ?? 3000)      // usa 3000 só se PORT for null/undefined
Omit<User, 'id'>                       // "o tipo User, mas sem o campo id"
```

`??` é tipo o `or` do Python, mas mais estrito — só cai no valor padrão se
for `null`/`undefined`, não se for `0` ou string vazia (o `or` do Python
cairia nesses casos também, o que costuma ser bug).

`Omit<...>` é um "tipo utilitário": pega um tipo existente e remove um
campo. Usado em [`models/user.model.ts`](../api-exemplo/src/models/user.model.ts)
porque pra **criar** um usuário você não tem o `id` ainda (quem gera é o
banco/array). Não tem equivalente direto em Python/PHP — é recurso só do
sistema de tipos do TypeScript, some completamente quando compila pra JS.
