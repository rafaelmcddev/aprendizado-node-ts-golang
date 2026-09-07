# 13. Erros comuns (os que todo mundo bate no começo)

## 1. Rota nova retorna 404 e você não sabe por quê

**Causa**: criou o arquivo em `routes/`, mas esqueceu de registrar em
`app.ts` (`app.use('/algo', algoRoutes)`). Diferente do Django
(`INSTALLED_APPS` + autodiscovery), Node não importa nada sozinho.

**Correção**: confira se o arquivo novo está com `app.use(...)` em
`app.ts`.

## 2. `req.body` chega `undefined`

**Causa**: esqueceu `app.use(express.json())` no `app.ts`. Sem esse
middleware, o Express não sabe transformar o JSON bruto do POST em
objeto.

**Correção**: `app.use(express.json())` **antes** das rotas.

## 3. Esqueceu o `await` e recebeu um objeto estranho em vez do valor

```ts
const user = buscarUsuario(id); // faltou await
console.log(user); // Promise { <pending> }, não o usuário
```

**Causa**: função `async` sempre retorna uma `Promise`. Sem `await`, você
pega a "caixa" (Promise), não o valor de dentro.

**Correção**: `const user = await buscarUsuario(id);`

## 4. `EADDRINUSE: address already in use`

**Causa**: já tem um processo rodando na mesma porta (geralmente uma
instância anterior do `npm run dev` que você esqueceu de parar).

**Correção**: `lsof -i :3000` (acha o processo) e `kill <PID>`, ou troque
a porta no `.env`.

## 5. Mudou o `.ts` mas o comportamento não muda

**Causa**: rodou com `node dist/server.js` (JS já compilado, antigo) em
vez de `npm run dev` (que usa `tsx`, lê o `.ts` direto e recompila
sozinho a cada mudança).

**Correção**: use `npm run dev` durante o desenvolvimento; `npm run
build` + `npm start` só quando for simular produção.

## 6. Servidor cai sozinho sem log de erro claro

**Causa**: um `throw` dentro de função `async` sem `try/catch` em volta —
vira uma "unhandled promise rejection", que em versões recentes do Node
derruba o processo inteiro.

**Correção**: sempre `try/catch` em rota `async`, ou centralize num
middleware de erro (veja `app.ts` do `api-exemplo/`).
