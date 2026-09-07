# 00. Sintaxe estranha (o que ninguém explica de cara)

Se você vem de Python/PHP, essas 3 coisas travam todo mundo no começo.
Nenhuma delas é "mágica" — é só sintaxe nova.

## 1. Função com nome maiúsculo

```go
func Show(w http.ResponseWriter, r *http.Request) { ... }  // maiúscula
func findByID(id string) { ... }                            // minúscula
```

Não é estilo, é **regra da linguagem**: a primeira letra maiúscula decide
se a função (ou variável, ou struct) é visível fora do arquivo/pacote.

| Python/PHP | Go |
|---|---|
| `def _privado():` (convenção, não é imposto) | `func privado()` (minúscula) — só visível dentro do mesmo pacote |
| `public function publico()` (PHP, palavra-chave) | `func Publico()` (maiúscula) — visível em outros pacotes |

Não existe `public`/`private` como palavra-chave em Go. É só a letra
inicial. Por isso em [`controllers/user_controller.go`](../api-exemplo/controllers/user_controller.go)
`Show`, `Index`, `Store` são maiúsculas (o `routes/routes.go` de outro
pacote precisa chamá-las) e em [`models/user.go`](../api-exemplo/models/user.go)
tem funções que poderiam ser minúsculas se só o próprio pacote usasse.

## 2. O que é esse `w` e esse `r`?

```go
func Show(w http.ResponseWriter, r *http.Request) { ... }
```

`w` e `r` **não são sintaxe especial** — são só nomes de variável, curtos
por convenção da comunidade Go (quase todo código Go usa `w`/`r` pra esses
dois parâmetros, do mesmo jeito que Python convenciona `self` ou Express
convenciona `req`/`res`). Poderiam se chamar `resposta` e `requisicao`,
funcionaria igual.

- `w` = `http.ResponseWriter` → onde você escreve a resposta (equivalente
  ao `res` do Express, ao `HttpResponse` do Django)
- `r` = `*http.Request` → a requisição recebida (equivalente ao `req` do
  Express, ao `request` do Django) — o `*` quer dizer "ponteiro", assunto
  do próximo tópico de Go que você vai encontrar (referência ao dado
  original, não uma cópia — parecido com passar objeto por referência em
  Python, mas explícito na assinatura da função).

## 3. `=` vs `:=`

```go
var nome string = "Ada"   // declaração completa: tipo explícito
nome = "Turing"           // reatribuição de algo que já existe (=)
idade := 30                // declaração curta: Go descobre o tipo sozinho (:=)
```

| | `=` | `:=` |
|---|---|---|
| O que faz | atribui valor a uma variável **que já existe** | declara **e** atribui uma variável **nova**, inferindo o tipo |
| Equivalente | `nome = "Turing"` (Python, reatribuição) | `nome = "Turing"` (Python, primeira vez — Python não distingue os dois casos) |

Python/PHP não têm essa distinção porque não são tipados assim — toda
atribuição em Python usa `=`. Em Go, `:=` só funciona **dentro de função**
(nunca no nível do arquivo) e só na primeira vez que a variável aparece.
Depois disso, é `=`:

```go
user, err := models.FindByID(id)  // primeira vez → :=
if err != nil {
    err = errors.New("outro erro") // reatribuindo → =
}
```

Veja isso acontecendo em [`controllers/user_controller.go`](../api-exemplo/controllers/user_controller.go).
