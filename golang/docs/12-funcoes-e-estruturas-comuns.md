# 12. Funções e pacotes da standard library mais usados

As 10 que aparecem em praticamente todo código Go de backend. Comparando
com o que você já faz em Python.

## 1. `fmt.Println` / `fmt.Printf` / `fmt.Sprintf`

```go
fmt.Println("Olá", nome)                    // print com espaço/quebra de linha
fmt.Printf("Nome: %s, Idade: %d\n", n, i)   // print formatado
msg := fmt.Sprintf("Olá, %s", nome)         // formata SEM imprimir, retorna string
```
Python: `print(...)`, `f"Nome: {n}, Idade: {i}"`, `"Olá, {}".format(nome)`

## 2. `strings` — manipulação de texto

```go
strings.ToUpper("ada")           // "ADA"
strings.Split("a,b,c", ",")      // ["a", "b", "c"]
strings.Contains("hello", "ell") // true
strings.TrimSpace("  oi  ")      // "oi"
strings.Join([]string{"a","b"}, "-") // "a-b"
```
Python: `.upper()`, `.split(',')`, `'ell' in 'hello'`, `.strip()`, `'-'.join([...])`

## 3. `strconv` — converter texto ↔ número

```go
n, err := strconv.Atoi("42")   // string → int
s := strconv.Itoa(42)          // int → string
```
Python: `int("42")`, `str(42)` — só que em Go sempre vem com `err` junto.

## 4. `append` — adicionar item numa slice (o "list" do Go)

```go
nums := []int{1, 2, 3}
nums = append(nums, 4) // [1, 2, 3, 4] — precisa reatribuir!
```
Python: `nums.append(4)` (muda a lista original, não precisa reatribuir —
diferença importante: `append` do Go **retorna** uma nova slice).

## 5. `range` — iterar (o "for" do Go)

```go
for i, nome := range []string{"Ada", "Alan"} {
    fmt.Println(i, nome) // 0 Ada / 1 Alan
}
for chave, valor := range map[string]int{"a": 1} {
    fmt.Println(chave, valor)
}
```
Python: `for i, nome in enumerate([...])`, `for chave, valor in dict.items()`

## 6. `map` — o "dict" do Go

```go
idades := map[string]int{"Ada": 36, "Alan": 41}
idade, ok := idades["Ada"] // "comma ok idiom": ok=false se não existir
idades["Grace"] = 85        // adiciona/atualiza
delete(idades, "Alan")      // remove
```
Python: `idades = {"Ada": 36}`, `idades.get("Ada")`, `idades["Grace"] = 85`, `del idades["Alan"]`

## 7. `errors.New` / `fmt.Errorf`

```go
err := errors.New("algo deu errado")
err2 := fmt.Errorf("erro ao buscar user %d: %w", id, err) // %w "embrulha" o erro original
```
Python: `raise Exception("algo deu errado")` — mas em Go você **retorna**
o erro, não lança (veja o [doc 07 de debug](./07-debug.md)).

## 8. `time` — datas e duração

```go
agora := time.Now()
depois := agora.Add(24 * time.Hour)
fmt.Println(agora.Format("2006-01-02")) // formato de data "esquisito" do Go
```
Python: `datetime.now()`, `timedelta(hours=24)`, `.strftime('%Y-%m-%d')`.
O formato de data do Go usa uma data mágica de referência
(`2006-01-02`) em vez de códigos tipo `%Y-%m-%d` — estranho, mas é assim.

## 9. `encoding/json` — o que já vimos nas APIs de exemplo

```go
dados, _ := json.Marshal(user)         // struct → JSON (bytes)
var user User
json.Unmarshal(dados, &user)           // JSON → struct (repara no &, é ponteiro)
```
Python: `json.dumps(user)`, `json.loads(dados)`

## 10. `defer` — roda algo só quando a função terminar

```go
func lerArquivo() {
    f, _ := os.Open("arquivo.txt")
    defer f.Close()  // fecha o arquivo, não importa como a função termine
    // ... resto do código usando f
}
```
Python: mais parecido com `with open("arquivo.txt") as f:` — o `defer` é
o "sempre executa no final", útil pra fechar conexão, arquivo, lock, etc.
