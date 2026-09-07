# Aprendizado Backend: Node.js/TS, Go, FastAPI, Flask

Repositório de estudo rápido, 100% backend, feito para quem já é dev
backend (Python/Django, PHP/Laravel) e quer entender outras stacks sem
ler curso de 10 horas.

Regra do repositório: **cada arquivo é curto**. Se você não entender em 2
minutos de leitura, o arquivo está errado.

> Se você sempre evitou Node.js achando que era "aquele JS de clicar em
> botão e mexer em DOM": não é. Leia
> [`node-ts/docs/00-backend-vs-frontend.md`](./node-ts/docs/00-backend-vs-frontend.md)
> primeiro — é exatamente sobre isso.

Cada stack com sintaxe muito diferente de Python/PHP tem um doc `00` só
pra isso — coisas tipo `:=` e nome de função maiúsculo em Go, ou `=>` e
`{ }` de destructuring em TypeScript. Comece por ele antes do `01`.

## Como usar

Toda dúvida do tipo "como funciona X nessa stack?" tem resposta objetiva
em `docs/`. Node e Go comparam com Python/PHP; FastAPI e Flask comparam
direto com Django, já que você já manja.

- [`/node-ts`](./node-ts) — Node.js + TypeScript
- [`/golang`](./golang) — Go
- [`/fastapi`](./fastapi) — FastAPI (Python)
- [`/flask`](./flask) — Flask (Python)

Cada pasta tem:
- `docs/` → textos curtos, um por tópico
- `api-exemplo/` → uma API REST simples e real que você roda e mexe

## Tópicos cobertos (nas 4 stacks)

1. Arquivo de configuração
2. Rota → qual arquivo é chamado
3. Fluxo da requisição (do request até a tela)
4. Como o backend "fala" com o front
5. Separação Model / View / Controller
6. Onde ficam os testes unitários
7. Como debugar (equivalente ao `dd()`/`print()`/`raise`)
8. Como instalar e usar dependências
9. Onde ficam os imports
10. Uma API REST simples, ponta a ponta, testada e rodável

## Ordem sugerida

Leia `docs/01` a `09` de uma stack por vez, depois rode a `api-exemplo/`
dela. Não precisa ler as quatro juntas — escolha pelo que o mercado está
pedindo na vaga que você está de olho.
