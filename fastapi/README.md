# FastAPI

Framework Python focado 100% em API (não tem Admin, não tem ORM próprio,
não tem template engine "oficial" tipo o Jinja do Flask). Como você já
sabe Django, os docs aqui comparam direto com o que você já conhece, sem
reexplicar Python.

Diferencial do FastAPI: tipagem com type hints vira validação automática
(Pydantic) e documentação automática (Swagger) de graça.

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
14. [Regras gerais de sintaxe](./docs/14-regras-gerais-de-sintaxe.md)
15. [Começando um projeto do zero (e onde ficam os logs)](./docs/15-comecando-do-zero.md)
16. [Status HTTP e como retornar erro](./docs/16-status-http-e-erros.md)
17. [Variáveis de ambiente e segredos](./docs/17-variaveis-de-ambiente-e-segredos.md)
18. [Próximos passos](./docs/18-proximos-passos.md)

## API de exemplo

[`api-exemplo/`](./api-exemplo) — CRUD de usuários, sem banco, com
validação automática via Pydantic e Swagger grátis em `/docs`.
