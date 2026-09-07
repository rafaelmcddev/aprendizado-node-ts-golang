# 01. Arquivo de configuração

| Python/PHP | Go | Pra que serve |
|---|---|---|
| `requirements.txt` / `composer.json` | `go.mod` | lista o módulo e as dependências |
| — | `go.sum` | trava os hashes exatos das dependências (== lock file) |
| `.env` | `.env` (lido manualmente ou com lib) | variáveis de ambiente |
| `settings.py` / `config.php` | `config/config.go` | config da sua app — **você cria** |

Go **não tem** leitor de `.env` embutido. Ou você lê variável de ambiente
direto (`os.Getenv`), ou usa uma lib pequena. Neste projeto, pra manter
zero dependência externa, `config/config.go` lê direto do ambiente com
valor padrão. Veja [`api-exemplo/config/config.go`](../api-exemplo/config/config.go).

`go.mod` é o `package.json` do Go:
```
module aprendizado/api-exemplo

go 1.22
```
