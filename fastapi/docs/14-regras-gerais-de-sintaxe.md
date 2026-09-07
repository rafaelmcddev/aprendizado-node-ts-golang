# 14. Regras gerais de sintaxe

Isso aqui é 100% o Python que você já usa em Django — sem novidade
nenhuma na sintaxe da linguagem em si. Fica aqui só pra fechar a
comparação com PHP/Laravel, caso você use essa tabela como referência
rápida entre as 4 stacks do repositório.

| Regra | Python (FastAPI) | PHP (Laravel) |
|---|---|---|
| Delimita bloco | indentação — **sem** chaves | `{ }` (chaves) |
| Indentação importa pro código rodar? | **sim, sempre** — indentação errada é `IndentationError` | não — só estética |
| Fim de instrução | quebra de linha, sem `;` | `;` obrigatório |
| Comentário de 1 linha | `# comentário` | `// comentário` |
| Comentário de bloco/docstring | `""" comentário """` | `/* comentário */` |
| Variável | sem prefixo: `nome` | com prefixo: `$nome` |
| Nomenclatura de variável/função | `snake_case` | `camelCase` |
| Nomenclatura de classe | `PascalCase` | `PascalCase` |
| String | `'simples'` ou `"duplas"`, iguais; `f"com {interpolação}"` | `'simples'` ou `"com $interpolação"` |
| Extensão de arquivo | `.py` | `.php` |

## A pegadinha real: misturar tab e espaço

```python
def show(user_id: int):
    user = find_by_id(user_id)  # 4 espaços
	return user                  # 1 tab — Python acusa erro aqui
```

Isso dá `TabError: inconsistent use of tabs and spaces` — o único erro de
indentação que realmente pega até quem já usa Python há anos, geralmente
por colar código de fontes diferentes. Configure seu editor pra **sempre
inserir espaços** ao apertar Tab (4 espaços é o padrão do PEP 8, a
convenção oficial de estilo Python).

## Tipagem é opcional, mas o FastAPI depende dela

```python
def show(user_id: int):   # com tipo — FastAPI valida sozinho
def show(user_id):        # sem tipo — funciona, mas perde a validação automática
```

Diferente do resto do Python (onde tipagem é só documentação, igual no
Django), no FastAPI a tipagem **muda o comportamento em runtime** — é o
que aciona a validação do Pydantic. Sempre tipe os parâmetros de rota.
