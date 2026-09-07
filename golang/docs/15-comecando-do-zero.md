# 15. Começando um projeto do zero (sem copiar o `api-exemplo/`)

Sequência real se você fosse começar um projeto Go novo, sozinho, sem
copiar este repositório.

## 1. Comandos iniciais

```bash
mkdir meu-projeto && cd meu-projeto
go mod init github.com/seu-usuario/meu-projeto   # cria go.mod
```

Repare: não tem `npm install`/`pip install` de framework nenhum — a
standard library já resolve servidor HTTP. Só roda `go get` quando
precisar de algo externo de verdade (ex: driver de banco).

## 2. Sequência de arquivos (nessa ordem)

1. `config/config.go` → lê variáveis de ambiente
2. `models/*.go` → dados (structs), não depende de mais nada
3. `controllers/*.go` → depende do model
4. `routes/routes.go` → depende do controller
5. `main.go` → junta tudo e sobe o servidor (depende de todos os outros)

Mesma ordem usada no `api-exemplo/` deste repositório.

## 3. Rodar

```bash
go run main.go              # roda direto, sem compilar binário separado
go build -o app && ./app    # compila um binário e executa (mais parecido com produção)
```

## 4. Onde ficam os logs

`fmt.Println`/`log.Println` imprimem no **terminal** (stdout/stderr) —
sem arquivo automático, igual Node, diferente do Laravel.

O pacote `log` da standard library já adiciona timestamp sozinho:
```go
log.Println("servidor iniciado") // 2024/01/15 10:30:00 servidor iniciado
```

Pra gravar em arquivo:
```go
f, _ := os.OpenFile("app.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
log.SetOutput(f) // a partir daqui, log.Println grava no arquivo, não no terminal
```
