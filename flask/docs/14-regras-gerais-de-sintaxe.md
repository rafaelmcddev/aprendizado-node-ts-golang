# 14. Regras gerais de sintaxe

Mesmo Python que você já usa em Django — sem novidade na linguagem em
si. Fica aqui pra fechar a comparação com PHP/Laravel.

| Regra | Python (Flask) | PHP (Laravel) |
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
def show(user_id):
    user = find_by_id(user_id)  # 4 espaços
	return user                  # 1 tab — Python acusa erro aqui
```

Dá `TabError: inconsistent use of tabs and spaces` — configure seu editor
pra sempre inserir espaços (4, padrão PEP 8) ao apertar Tab.

## Diferente do FastAPI: tipagem em Flask é só documentação

```python
def show(user_id: int):   # o tipo aqui é só uma dica visual
def show(user_id):        # funciona exatamente igual
```

Flask **não lê** a tipagem pra validar nada — é puramente informativo
pro seu editor te ajudar. Se `user_id` chegar como string na URL, você
mesmo converte (`int(user_id)`), sem validação automática — diferente do
FastAPI, que converte e valida sozinho.
