# Go (Golang)

Go = linguagem compilada, tipada, feita pro Google, muito usada em
backend/infra hoje. Sem framework "padrão" tipo Django — o próprio Go já
vem com servidor HTTP na standard library.

> Nome de função maiúsculo, `w`/`r` como parâmetro, `:=` em vez de `=`,
> `*` antes do tipo, `t.Errorf` — se isso te travou, leia primeiro:
> [00 — sintaxe estranha](./docs/00-sintaxe-estranha.md).

Termo estranho? Veja o [glossário cruzado](../GLOSSARIO.md) na raiz do repositório.

## Docs (leitura de 2 min cada)

0. [Sintaxe estranha (maiúscula, `w`/`r`, `:=`, `*`, `t.Errorf`)](./docs/00-sintaxe-estranha.md)
1. [Arquivo de configuração](./docs/01-arquivo-de-configuracao.md)
2. [Rota → qual arquivo é chamado](./docs/02-rotas-e-arquivos.md)
3. [Fluxo da requisição](./docs/03-fluxo-da-requisicao.md)
4. [Backend chamando o front](./docs/04-backend-chama-front.md)
5. [Model / View / Controller](./docs/05-mvc.md)
6. [Testes unitários](./docs/06-testes-unitarios.md)
7. [Debug (dd/print/raise?)](./docs/07-debug.md)
8. [Dependências (go mod)](./docs/08-dependencias.md)
9. [Imports](./docs/09-imports.md)
10. ["Classes", métodos e properties (structs)](./docs/10-structs-metodos-propriedades.md)
11. [Migrations](./docs/11-migrations.md)
12. [Funções e pacotes da standard library mais usados](./docs/12-funcoes-e-estruturas-comuns.md)
13. [Erros comuns](./docs/13-erros-comuns.md)
14. [Regras gerais de sintaxe](./docs/14-regras-gerais-de-sintaxe.md)
15. [Começando um projeto do zero (e onde ficam os logs)](./docs/15-comecando-do-zero.md)

## API de exemplo

[`api-exemplo/`](./api-exemplo) — CRUD de usuários, só com a standard
library (`net/http`), sem framework, sem banco.
