# 13. Erros comuns (os que todo mundo bate no começo)

## 1. Rota nova dá 404 e não tem erro nenhum explicando

**Causa**: criou o router novo em `app/routers/`, mas esqueceu
`app.include_router(...)` no `main.py`. Diferente do Django, não existe
`INSTALLED_APPS` fazendo isso sozinho.

**Correção**: toda rota nova precisa do `include_router` explícito.

## 2. `422 Unprocessable Entity` sem entender por quê

**Causa**: o Pydantic validou o body/parâmetro e não bateu com o tipo
esperado — isso acontece **antes** do seu código rodar, então não
adianta procurar `print()` na sua função, o erro nem chegou lá.

**Correção**: veja o corpo da resposta 422 — ele já diz exatamente qual
campo falhou e por quê. Ou teste direto pelo `/docs` (Swagger), que
mostra o schema esperado.

## 3. Rota fixa "escondida" por uma rota dinâmica

```python
@router.get("/{user_id}")   # declarada primeiro
def show(user_id: int): ...

@router.get("/me")          # nunca é alcançada!
def me(): ...
```

**Causa**: FastAPI testa as rotas na ordem que foram declaradas. Como
`/me` bate no padrão `/{user_id}` primeiro (viraria `user_id="me"`, e daí
dá erro de tipo), a rota fixa nunca é alcançada.

**Correção**: declare rotas fixas (`/me`) **antes** das dinâmicas
(`/{user_id}`).

## 4. Função `async def` travando o servidor inteiro

```python
@router.get("/lento")
async def lento():
    time.sleep(5)   # bloqueia TODO o servidor, não só essa requisição
```

**Causa**: `time.sleep` é bloqueante. Dentro de uma função `async`, você
precisa de operações que também sejam assíncronas.

**Correção**: use `await asyncio.sleep(5)` em vez de `time.sleep(5)`
(ou, se a função não faz nada assíncrono de verdade, nem precisa ser
`async def` — pode ser `def` normal, o FastAPI lida com os dois).

## 5. `ModuleNotFoundError` mesmo depois de instalar

**Causa**: instalou com `pip install` fora do ambiente virtual (ou o
`venv` não estava ativado).

**Correção**: confirme que ativou (`source venv/bin/activate`) antes de
instalar e antes de rodar `uvicorn`.

## 6. Editou o código e o servidor não atualiza

**Causa**: rodou `uvicorn app.main:app` sem `--reload`.

**Correção**: `uvicorn app.main:app --reload` em desenvolvimento (nunca
em produção).
