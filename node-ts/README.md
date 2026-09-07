# Node.js + TypeScript

Node.js = ambiente que roda JavaScript fora do navegador (tipo o PHP-FPM,
mas pra JS). TypeScript = JavaScript com tipos, parecido com type hints do
Python, só que checado antes de rodar (compila pra JS puro).

## Docs (leitura de 2 min cada)

1. [Arquivo de configuração](./docs/01-arquivo-de-configuracao.md)
2. [Rota → qual arquivo é chamado](./docs/02-rotas-e-arquivos.md)
3. [Fluxo da requisição](./docs/03-fluxo-da-requisicao.md)
4. [Backend chamando o front](./docs/04-backend-chama-front.md)
5. [Model / View / Controller](./docs/05-mvc.md)
6. [Testes unitários](./docs/06-testes-unitarios.md)
7. [Debug (dd/print/raise?)](./docs/07-debug.md)
8. [Dependências (npm)](./docs/08-dependencias.md)
9. [Imports](./docs/09-imports.md)

## API de exemplo

[`api-exemplo/`](./api-exemplo) — CRUD de usuários com Express + TS, sem
banco de dados (guarda em memória, pra você focar no fluxo, não no SQL).
