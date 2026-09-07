# 10. "Classes", métodos e properties em Go

**Go não tem classes.** Isso trava todo mundo que vem de Python/PHP. O
que existe é **struct** (o "molde" dos dados) + **função com receiver**
(o "método"), que juntos fazem o mesmo trabalho.

## Struct = os campos da classe, sem os métodos dentro

```go
type User struct {
	ID    int
	Name  string
	Email string
}

u := User{ID: 1, Name: "Ada", Email: "ada@example.com"}
fmt.Println(u.Name) // acesso direto ao campo — é a "property"
```

| Python | Go |
|---|---|
| `class User:` + `def __init__(self, id, name, email):` | `type User struct { ID int; Name string; Email string }` |
| `self.name = name` dentro do `__init__` | os campos já existem só de declarar o struct, sem "construtor" obrigatório |
| `user.name` | `u.Name` |

Não existe `__init__`. Pra "construir" com regra própria, você escreve
uma função normal que retorna o struct:
```go
func NewUser(name, email string) User {
	return User{ID: geraID(), Name: name, Email: email}
}
```

## Método = função "grudada" no struct via receiver

Você já viu isso em `t.Errorf` — agora o completo:

```go
func (u User) Greet() string {          // receiver: (u User)
	return "Olá, " + u.Name
}

u.Greet() // chama como se fosse método de classe
```

O `(u User)` antes do nome da função é o **receiver** — é isso que
"pluga" a função `Greet` no tipo `User`. Sem ele, seria só uma função
solta que precisa receber `user` como parâmetro comum.

| Python | Go |
|---|---|
| `def greet(self):` dentro da classe | `func (u User) Greet() { ... }` fora, no mesmo arquivo/pacote |
| chama com `user.greet()` | chama com `u.Greet()` |

## Receiver por valor vs por ponteiro — a pegadinha

```go
func (u User) MudaNomeErrado(novo string) {
	u.Name = novo // muda só a cópia local, o original NÃO muda
}

func (u *User) MudaNomeCerto(novo string) {
	u.Name = novo // muda o original, porque *User é ponteiro (endereço)
}
```

Se o método **só lê** os campos, receiver por valor `(u User)` está ok.
Se o método **precisa alterar** o struct original, o receiver tem que ser
ponteiro `(u *User)` — mesma lógica do `*http.Request` que você já viu.
Regra prática: na dúvida, use ponteiro.

## Não existe `private`/`public` de método — é a mesma regra da maiúscula

```go
func (u User) Greet() string { ... }      // maiúscula = método público
func (u User) validaEmail() bool { ... }  // minúscula = só usa dentro do pacote
```

Mesma regra do [doc 00](./00-sintaxe-estranha.md): não é palavra-chave,
é a letra inicial do nome do método.

## Não existe getter/setter "de verdade"

Go não tem `@property` nem `get`/`set` especial. Se você quer um campo
calculado, é só um método normal:
```go
func (u User) EmailNormalizado() string {
	return strings.ToLower(u.Email)
}
```
Chama como `u.EmailNormalizado()` — com parênteses, diferente de Python
(`@property` deixa sem parênteses) e de TypeScript (`get` também deixa
sem parênteses).
