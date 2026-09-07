# 16. Status HTTP e como retornar erro

Os mesmos 6 códigos, agora no FastAPI — que tem uma vantagem: **muitos
desses códigos saem automáticos**, sem você escrever nada.

| Código | Quando usar | Quem dispara |
|---|---|---|
| `200` | deu certo, GET normal | automático |
| `201` | criou algo novo | você define (`status_code=201` no decorator) |
| `400` | dado inválido — regra de negócio sua | você lança (`HTTPException`) |
| `401` | precisa autenticação | você lança |
| `403` | sem permissão | você lança |
| `404` | recurso não existe | você lança |
| `422` | Pydantic recusou o formato do dado | **automático**, você não escreve nada |
| `500` | erro não tratado no seu código | automático, o FastAPI captura sozinho |

## Como isso aparece no código

```python
@router.post("/", status_code=201)      # 201 declarado no próprio decorator
def store(data: UserCreate) -> User:
    return user_model.create(data)

@router.get("/{user_id}")
def show(user_id: int) -> User:
    user = user_model.find_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="usuário não encontrado")
    return user
```
Veja em [`api-exemplo/app/routers/user.py`](../api-exemplo/app/routers/user.py).

## O 422 "de graça" — vantagem real do FastAPI

Se `data: UserCreate` não bater com o schema Pydantic (faltou campo,
tipo errado), o FastAPI já responde `422` sozinho, **antes** da sua
função rodar — sem você escrever `if`/`raise` nenhum. É o principal
diferencial de status automático que as outras 3 stacks não têm de
fábrica.

## Padrão de corpo de erro

```json
{ "detail": "usuário não encontrado" }
```
Repare: FastAPI usa a chave `"detail"` por padrão (convenção do
framework), diferente do `{"error": "..."}` usado nas outras 3 stacks
deste repositório — se for integrar um front único com as 4 APIs de
exemplo, essa é a diferença a tratar.
