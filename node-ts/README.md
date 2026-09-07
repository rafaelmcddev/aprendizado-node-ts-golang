# Node.js + TypeScript

Node.js = ambiente que roda JavaScript fora do navegador (tipo o PHP-FPM,
mas pra JS). TypeScript = JavaScript com tipos, parecido com type hints do
Python, só que checado antes de rodar (compila pra JS puro).

> Se você sempre evitou Node por achar que era "aquele JS de clique e
> DOM", leia primeiro: [00 — não é frontend](./docs/00-backend-vs-frontend.md).

## Docs (leitura de 2 min cada)

0. [Isso não é o JS de manipular botão?](./docs/00-backend-vs-frontend.md)
0. [Sintaxe estranha (`:tipo`, `=>`, `{ }`, `...`, `??`)](./docs/00-sintaxe-estranha.md)
1. [Arquivo de configuração](./docs/01-arquivo-de-configuracao.md)
2. [Rota → qual arquivo é chamado](./docs/02-rotas-e-arquivos.md)
3. [Fluxo da requisição](./docs/03-fluxo-da-requisicao.md)
4. [Backend chamando o front](./docs/04-backend-chama-front.md)
5. [Model / View / Controller](./docs/05-mvc.md)
6. [Testes unitários](./docs/06-testes-unitarios.md)
7. [Debug (dd/print/raise?)](./docs/07-debug.md)
8. [Dependências (npm)](./docs/08-dependencias.md)
9. [Imports](./docs/09-imports.md)
10. [Classes, métodos e properties](./docs/10-classes-metodos-propriedades.md)
11. [Migrations](./docs/11-migrations.md)
12. [Funções e estruturas built-in mais usadas](./docs/12-funcoes-e-estruturas-comuns.md)

## API de exemplo

[`api-exemplo/`](./api-exemplo) — CRUD de usuários com Express + TS, sem
banco de dados (guarda em memória, pra você focar no fluxo, não no SQL).
