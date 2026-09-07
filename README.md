# Aprendizado: Node.js + TypeScript + Go

Repositório de estudo rápido, feito para quem já é dev backend (Python/PHP) e
quer entender **Node+TS** e **Go** sem ler curso de 10 horas.

Regra do repositório: **cada arquivo é curto**. Se você não entender em 2
minutos de leitura, o arquivo está errado — abra uma issue.

## Como usar

Toda dúvida do tipo "como funciona X em Node/Go?" tem uma resposta objetiva
em `docs/`. Cada tópico compara com o que você já conhece de Python/PHP.

- [`/node-ts`](./node-ts) — Node.js + TypeScript
- [`/golang`](./golang) — Go

Cada pasta tem:
- `docs/` → textos curtos, um por tópico
- `api-exemplo/` → uma API REST simples e real que você roda e mexe

## Tópicos cobertos (nas duas linguagens)

1. Arquivo de configuração
2. Rota → qual arquivo é chamado
3. Fluxo da requisição (do clique até a tela)
4. Como o backend "fala" com o front
5. Separação Model / View / Controller
6. Onde ficam os testes unitários
7. Como debugar (equivalente ao `dd()`/`print()`/`raise`)
8. Como instalar e usar dependências
9. Onde ficam os imports
10. Uma API REST simples, ponta a ponta

## Ordem sugerida

Leia `docs/01` a `09` da pasta que você quiser primeiro (Node ou Go), depois
rode a `api-exemplo/`. Não precisa ler as duas linguagens juntas.
