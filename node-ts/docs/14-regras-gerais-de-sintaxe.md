# 14. Regras gerais de sintaxe

O básico que ninguém explica porque assume que você já sabe. Você vem de
Python (indentação) e PHP (`{ }` + `$var` + `;`) — TypeScript fica no
meio do caminho entre os dois.

| Regra | TypeScript | Python | PHP |
|---|---|---|---|
| Delimita bloco | `{ }` (chaves) | indentação (espaços) | `{ }` (chaves) |
| Indentação importa pro código rodar? | não — só estética | **sim** — indentação errada quebra o código | não — só estética |
| Fim de instrução | `;` (opcional, mas use sempre) | quebra de linha, sem `;` | `;` **obrigatório** |
| Comentário de 1 linha | `// comentário` | `# comentário` | `// comentário` |
| Comentário de bloco | `/* comentário */` | `""" comentário """` (docstring) | `/* comentário */` |
| Variável | sem prefixo: `nome` | sem prefixo: `nome` | com prefixo: `$nome` |
| Nomenclatura de variável/função | `camelCase` | `snake_case` | `camelCase` (convenção, não regra) |
| Nomenclatura de classe/tipo | `PascalCase` | `PascalCase` | `PascalCase` |
| Nomenclatura de constante "de verdade" | `UPPER_SNAKE_CASE` | `UPPER_SNAKE_CASE` | `UPPER_SNAKE_CASE` |
| String | `'aspas simples'`, `"aspas duplas"`, ou `` `crase, com ${interpolação}` `` | `'aspas simples'`, `"aspas duplas"`, `f"com {interpolação}"` | `'aspas simples'`, `"com $interpolação"` |
| Extensão de arquivo | `.ts` | `.py` | `.php` |

## Indentação: não quebra o código, mas quebra a leitura

```ts
function show(req, res) {
res.json(userModel.findAll());
}
```
Isso **roda** normalmente em TS — o compilador não liga pra indentação.
Mas ninguém vai conseguir ler seu código. Convenção do ecossistema JS/TS:
**2 espaços** (não 4, diferente da convenção mais comum de Python).

## Template literals — a string que você vai usar mais

```ts
const nome = 'Ada';
console.log(`Olá, ${nome}!`); // crase, não aspas — permite ${...} dentro
```
Equivalente direto ao f-string do Python (`f"Olá, {nome}!"`). Aspas
simples/duplas normais **não** permitem interpolação em TS.
