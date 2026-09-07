# 00. Sintaxe estranha (o que ninguém explica de cara)

Se você vem de Python/PHP, essas 5 coisas travam todo mundo no começo.
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

## 4. O `*` de novo — ponteiro

```go
func Show(w http.ResponseWriter, r *http.Request) { ... }
//                                 ^ ponteiro pra Request

func TestFindByID(t *testing.T) { ... }
//                  ^ ponteiro pra T
```

`*Tipo` quer dizer "isso aqui não é o dado, é o **endereço na memória**
de onde o dado está" — um ponteiro. Quando você recebe `r *http.Request`,
não chegou uma cópia da requisição, chegou a referência pra requisição
original.

Python e PHP fazem isso o tempo todo **por baixo dos panos**, sem você
escrever nada — quando você passa um objeto pra uma função em Python, ele
já é passado por referência, silenciosamente. Go só torna isso **visível
e explícito** na assinatura:

| | Sem `*` | Com `*` |
|---|---|---|
| O que é | uma cópia do valor | o endereço do valor original |
| Alterou dentro da função? | não afeta o original | afeta o original |
| Parecido com | `def f(numero):` em Python (tipos simples são cópia) | `def f(lista):` em Python (objetos são referência) |

Dois símbolos relacionados que você vai ver:
- `*variavel` → "pega o valor que está nesse endereço" (dereferência)
- `&variavel` → "me dá o endereço dessa variável" (o oposto)

Na prática, no dia a dia deste projeto: `*http.Request` e `*testing.T`
são sempre recebidos assim por convenção da própria linguagem — você não
precisa decidir isso, só reconhecer que "tem um `*` ali porque é assim
que a standard library define esses tipos".

## 5. `t.Errorf` — métodos com "receiver"

```go
func TestFindByIDExistente(t *testing.T) {
    user, ok := FindByID("1")
    if !ok || user.Name != "Ada Lovelace" {
        t.Errorf("esperava Ada Lovelace, veio %+v (ok=%v)", user, ok)
    }
}
```

Go não tem classes, mas tem uma forma de "anexar" função a um tipo — isso
é o que faz `t.Errorf(...)` funcionar. Em algum lugar da standard library
existe algo como:

```go
func (t *T) Errorf(format string, args ...any) { ... }
//    ^^^^^^ isso é o "receiver": diz que essa função pertence ao tipo *T
```

Isso é o mais próximo que Go chega de método de classe. Comparando:

| Python | Go |
|---|---|
| `self.assertEqual(a, b)` (dentro de uma classe `TestCase`) | `t.Errorf(...)` (`t` é uma instância de `testing.T` recebida como parâmetro) |
| método definido dentro da classe | método definido **fora**, ligado ao tipo via `func (t *T) Nome(...)` |

`t` no seu teste é só uma variável — o framework de testes do Go cria um
`*testing.T` e passa pra sua função `TestAlgumaCoisa(t *testing.T)`. A
partir daí, `t.Errorf(...)`, `t.Fatalf(...)`, `t.Log(...)` são métodos
desse objeto, chamados com `.`, exatamente como você chamaria um método
de objeto em Python (`objeto.metodo()`) — só que a "classe" foi definida
em outro arquivo, ligada ao tipo por esse `func (t *T) ...` que você
talvez nunca precise escrever, só usar.

Veja `t.Errorf` em ação em [`models/user_test.go`](../api-exemplo/models/user_test.go).
