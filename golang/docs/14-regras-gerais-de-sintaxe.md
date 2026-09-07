# 14. Regras gerais de sintaxe

O básico antes dos detalhes finos do [doc 00](./00-sintaxe-estranha.md).

| Regra | Go | Python | PHP |
|---|---|---|---|
| Delimita bloco | `{ }` (chaves) — **obrigatório** | indentação | `{ }` (chaves) |
| Indentação importa pro código rodar? | não — mas `gofmt` formata sozinho e vira padrão do time todo | **sim** | não |
| Fim de instrução | sem `;` — o compilador insere sozinho | sem `;` | `;` obrigatório |
| Comentário de 1 linha | `// comentário` | `# comentário` | `// comentário` |
| Comentário de bloco | `/* comentário */` | `""" comentário """` | `/* comentário */` |
| Variável | sem prefixo: `nome` | sem prefixo: `nome` | com prefixo: `$nome` |
| Nomenclatura | `camelCase` (privado) / `PascalCase` (exportado) — [doc 00](./00-sintaxe-estranha.md) | `snake_case` | `camelCase` |
| String | `"aspas duplas"` — aspas simples são só pra 1 caractere (`rune`) | `'simples'` ou `"duplas"`, iguais | `'simples'` ou `"duplas"` |
| Extensão de arquivo | `.go` | `.py` | `.php` |

## A chave `{` tem que ficar na mesma linha — regra real, não estilo

```go
func Show(w http.ResponseWriter, r *http.Request) {  // { aqui, sempre
    ...
}
```

```go
func Show(w http.ResponseWriter, r *http.Request)
{                                                      // ERRO de compilação
    ...
}
```

Diferente de C/Java/PHP, onde colocar a chave na linha de baixo é só
questão de estilo, em Go **isso quebra o build**. O compilador insere
ponto-e-vírgula automaticamente no fim de cada linha que "parece"
completa — se a chave estiver sozinha na linha seguinte, ele fecha a
instrução ali, cedo demais.

## `gofmt` — formatação não é opinião, é regra da comunidade

```bash
gofmt -w arquivo.go   # reformata o arquivo no padrão oficial
go fmt ./...          # mesma coisa, pro projeto inteiro
```

Diferente de Python/PHP, onde formatação (tabs vs espaços, chave na
mesma linha ou não) é debate infinito de time, em Go **existe um único
formato oficial** e praticamente todo código Go do mundo segue ele.
Rode `gofmt` antes de cada commit — é convenção forte o suficiente pra
ser considerada regra.
