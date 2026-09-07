# 16. Status HTTP e como retornar erro

Os 6 códigos que cobrem 95% de uma API REST — e como cada um aparece no
`api-exemplo/` deste projeto.

| Código | Nome | Quando usar |
|---|---|---|
| `200` | OK | deu certo, tem corpo na resposta (GET, PUT que retorna o item) |
| `201` | Created | criou algo novo (POST que criou um recurso) |
| `400` | Bad Request | o cliente mandou dado inválido/incompleto (campo obrigatório faltando) |
| `401` | Unauthorized | precisa estar autenticado e não está |
| `403` | Forbidden | está autenticado, mas não tem permissão pra essa ação |
| `404` | Not Found | o recurso pedido não existe |
| `422` | Unprocessable Entity | o formato do dado está certo, mas o valor é inválido (mais usado com validação automática, tipo Pydantic) |
| `500` | Internal Server Error | erro do seu código, não é culpa do cliente |

## Como isso aparece no código

```ts
res.status(201).json(user);                              // criou
res.status(404).json({ error: 'usuário não encontrado' }); // não achou
res.status(400).json({ error: 'name e email são obrigatórios' }); // dado inválido
```
Veja em [`api-exemplo/src/controllers/user.controller.ts`](../api-exemplo/src/controllers/user.controller.ts).

## Padrão de corpo de erro usado neste repositório

```json
{ "error": "mensagem explicando o que deu errado" }
```
Simples de propósito. Em projeto real, é comum ter um formato mais rico
(`{ "error": { "code": "...", "message": "...", "fields": {...} } }`),
mas o princípio é o mesmo: **sempre devolva um corpo explicando o erro**,
nunca só o status code sem contexto.

## Erro do seu código (500) nunca deve vazar detalhe pro cliente

```ts
app.use((err, req, res, next) => {
  console.error(err);                          // log completo só no servidor
  res.status(500).json({ error: 'erro interno' }); // resposta genérica pro cliente
});
```
Nunca devolva `err.message`/stack trace direto pro cliente em produção —
pode vazar detalhe interno (caminho de arquivo, versão de lib, etc).
