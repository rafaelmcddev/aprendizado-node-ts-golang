# 18. Próximos passos (depois de entender este exemplo)

O `api-exemplo/` deste repositório é de propósito simples (sem banco,
sem autenticação) pra você focar no fluxo. Quando isso já estiver
confortável, é aqui que você continua — sem se aprofundar em nenhum
agora, só sabendo que existe e pra onde ir.

## 1. Banco de dados de verdade

Troque o array em memória (`models/user.model.ts`) por um banco real.
Ferramenta mais comum hoje: **Prisma** (veja o [doc 11](./11-migrations.md)).
```bash
npm install prisma --save-dev
npx prisma init
```

## 2. Autenticação

Padrão mais comum em API: **JWT** (JSON Web Token). Lib mais usada:
`jsonwebtoken`. Fluxo básico: usuário manda login/senha, servidor
devolve um token, cliente manda esse token no header
`Authorization: Bearer <token>` nas próximas requisições.

## 3. Validação mais robusta

Este projeto valida campo a campo na mão (`if (!name || !email)`). Em
projeto real, use uma lib de schema, tipo **Zod** — valida e já gera o
tipo TypeScript junto, uma fonte só de verdade.

## 4. Logs estruturados

Veja o [doc 15](./15-comecando-do-zero.md) — em produção, troque
`console.log` solto por uma lib tipo **Pino** ou **Winston**, que gera
log em JSON (mais fácil de buscar/filtrar depois) e separa nível
(info/warning/error).

## 5. Deploy

Opções simples pra Node: **Railway**, **Render**, **Fly.io** — todas
detectam o `package.json` sozinhas e sobem o projeto com poucos clicks.
Configuração de produção real usa `npm run build` (compila TS → JS) +
`npm start`, não o `npm run dev`.

## Resumindo

Nenhum desses é obrigatório pra "aprender Node" — são os próximos degraus
depois que o fluxo básico (rota → controller → model → resposta) já
estiver automático pra você.
