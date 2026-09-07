# 16. Status HTTP e como retornar erro

Os mesmos 6 códigos, agora no Flask.

| Código | Quando usar |
|---|---|
| `200` | deu certo, tem corpo na resposta |
| `201` | criou algo novo |
| `400` | dado inválido/incompleto |
| `401` | precisa autenticação |
| `403` | sem permissão |
| `404` | recurso não existe |
| `422` | formato certo, valor inválido |
| `500` | erro não tratado no seu código |

Diferente do FastAPI, Flask **não valida nada sozinho** — todo `400`/`404`
você mesmo decide e retorna.

## Como isso aparece no código

```python
return jsonify(user), 201                                    # criou
return jsonify({"error": "usuário não encontrado"}), 404     # não achou
return jsonify({"error": "name e email são obrigatórios"}), 400  # dado inválido
```
O status vem como segundo item da tupla que a rota retorna — jeito mais
comum no Flask. Veja em [`api-exemplo/app/routes/user.py`](../api-exemplo/app/routes/user.py).

## Alternativa: `abort()`

```python
from flask import abort
abort(404, description="usuário não encontrado")
```
Faz a rota parar ali e devolver o erro, sem precisar de `return` — mais
parecido com um `raise`. Usado quando você quer interromper o fluxo de
qualquer ponto da função, não só no final.

## Padrão de corpo de erro usado neste repositório

```json
{ "error": "mensagem explicando o que deu errado" }
```
Mesmo formato usado em Node e Go — só o FastAPI foge disso (usa
`"detail"` em vez de `"error"`, veja o [doc equivalente](../../fastapi/docs/16-status-http-e-erros.md)).

## Erro não tratado também vira 500 sozinho

Se seu código explodir com uma exceção qualquer não tratada, o Flask
devolve `500` automaticamente — mas com `debug=False` (produção), o
corpo da resposta é genérico, sem vazar o traceback pro cliente. Com
`debug=True`, ele mostra a página de erro interativa (útil só em
desenvolvimento, veja o [doc 07](./07-debug.md)).
