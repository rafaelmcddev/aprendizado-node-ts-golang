# Flask

Microframework Python — o oposto filosófico do Django. Não vem com ORM,
não vem com Admin, não vem com estrutura de pastas imposta. Você monta a
casa do zero, peça por peça. Como você já conhece Django, os docs aqui
comparam o que muda de "framework completo" pra "framework mínimo".

Termo estranho? Veja o [glossário cruzado](../GLOSSARIO.md) na raiz do repositório.

## Docs (leitura de 2 min cada)

1. [Arquivo de configuração](./docs/01-arquivo-de-configuracao.md)
2. [Rota → qual arquivo é chamado](./docs/02-rotas-e-arquivos.md)
3. [Fluxo da requisição](./docs/03-fluxo-da-requisicao.md)
4. [Backend chamando o front](./docs/04-backend-chama-front.md)
5. [Model / View / Controller](./docs/05-mvc.md)
6. [Testes unitários](./docs/06-testes-unitarios.md)
7. [Debug (dd/print/raise?)](./docs/07-debug.md)
8. [Dependências (pip)](./docs/08-dependencias.md)
9. [Imports](./docs/09-imports.md)
10. [Classes, métodos e properties](./docs/10-classes-metodos-propriedades.md)
11. [Migrations](./docs/11-migrations.md)
12. [Funções e estruturas built-in mais usadas](./docs/12-funcoes-e-estruturas-comuns.md)
13. [Erros comuns](./docs/13-erros-comuns.md)

## API de exemplo

[`api-exemplo/`](./api-exemplo) — CRUD de usuários, sem banco, usando
Blueprint (o jeito Flask de organizar rotas por módulo).
