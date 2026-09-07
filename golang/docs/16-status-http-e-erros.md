# 16. Status HTTP e como retornar erro

Os mesmos 6 códigos do [doc equivalente do Node](../../node-ts/docs/16-status-http-e-erros.md),
agora do jeito Go.

| Código | Constante em `net/http` | Quando usar |
|---|---|---|
| `200` | `http.StatusOK` | deu certo, tem corpo na resposta |
| `201` | `http.StatusCreated` | criou algo novo |
| `400` | `http.StatusBadRequest` | dado inválido/incompleto |
| `401` | `http.StatusUnauthorized` | precisa autenticação |
| `403` | `http.StatusForbidden` | autenticado, mas sem permissão |
| `404` | `http.StatusNotFound` | recurso não existe |
| `422` | `http.StatusUnprocessableEntity` | formato certo, valor inválido |
| `500` | `http.StatusInternalServerError` | erro do seu código |

Go tem **constante nomeada** pra cada status — evite escrever o número
mágico (`404`) direto, use `http.StatusNotFound`. Mais legível e o editor
autocompleta.

## Como isso aparece no código

```go
w.WriteHeader(http.StatusCreated)                    // criou
http.Error(w, `{"error":"não encontrado"}`, http.StatusNotFound) // não achou
```
Veja em [`api-exemplo/controllers/user_controller.go`](../api-exemplo/controllers/user_controller.go).

## Cuidado: `w.WriteHeader` só pode ser chamado uma vez

```go
w.WriteHeader(http.StatusCreated) // define o status
w.Write([]byte("..."))            // escreve o corpo DEPOIS

w.Write([]byte("..."))            // se escrever ANTES, o status vira 200 sozinho
w.WriteHeader(http.StatusCreated) // e isso aqui não faz mais nada — tarde demais
```
Ordem importa: sempre defina o status **antes** de escrever qualquer
coisa no corpo. Diferente de Node/Python, onde a ordem entre `status()` e
`json()` normalmente não quebra nada.

## Padrão de corpo de erro usado neste repositório

```json
{ "error": "mensagem explicando o que deu errado" }
```
Mesmo formato das outras 3 stacks deste repositório — facilita comparar
lado a lado.
