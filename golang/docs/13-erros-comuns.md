# 13. Erros comuns (os que todo mundo bate no começo)

## 1. Ignorou o `err` e o bug sumiu sem explicação

```go
user, _ := models.FindByID(id) // jogou o erro fora com "_"
fmt.Println(user.Name)          // user pode estar vazio, sem aviso nenhum
```

**Causa**: Go não obriga tratar erro — se você usar `_`, o compilador
deixa passar. Diferente de exceção em Python, que pelo menos avisa
derrubando o programa.

**Correção**: sempre `if err != nil { ... }` — é chato, mas é assim que
Go funciona. Vira hábito rápido.

## 2. `declared and not used` / `imported and not used`

**Causa**: Go trata variável ou import não usado como **erro de
compilação**, não warning (diferente de Python/PHP).

**Correção**: apague o import/variável que sobrou, ou use `_` se
precisar declarar mas não usar de propósito (raro).

## 3. Mudou um campo dentro de um método e o original não mudou

```go
func (u User) MudaNome(novo string) {
	u.Name = novo // muda só a cópia
}
```

**Causa**: receiver por valor `(u User)` recebe uma **cópia** do struct.
Veja o [doc 10](./10-structs-metodos-propriedades.md).

**Correção**: use receiver por ponteiro `(u *User)` quando o método
precisa alterar o struct original.

## 4. `nil pointer dereference` — o pânico mais comum

```go
var user *User          // ponteiro "vazio", aponta pra lugar nenhum
fmt.Println(user.Name)  // panic: tentando ler campo de ponteiro nil
```

**Causa**: declarou um ponteiro mas nunca atribuiu um struct de verdade
a ele.

**Correção**: sempre confira `if user == nil { ... }` antes de acessar
campo de algo que pode ser ponteiro nulo — muito comum depois de uma
busca que pode não encontrar nada.

## 5. `go: module ... : not found` depois de importar algo novo

**Causa**: adicionou um `import` de uma lib externa, mas esqueceu de
rodar `go mod tidy` (ou `go get`) pra registrar no `go.mod`.

**Correção**: `go mod tidy` depois de qualquer novo import externo.

## 6. Variável "sumiu" dentro de um `if`

```go
user, err := models.FindByID("1")
if outraCondicao {
	user, err := models.FindByID("2") // := aqui cria um NOVO user, só do if
}
fmt.Println(user) // ainda é o de fora, não o de dentro do if
```

**Causa**: `:=` dentro de um bloco `{ }` cria variável nova, mesmo que já
exista uma com o mesmo nome fora — é o "shadowing". Veja o
[doc 00](./00-sintaxe-estranha.md#3--vs-).

**Correção**: use `=` (não `:=`) quando quiser reatribuir a variável de
fora, não criar uma nova escondida.
