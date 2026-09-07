# 07. Como debugar (dd/print/raise?)

Igual você já usa em Django — nada muda:

| O que você já faz | Continua igual |
|---|---|
| `print()` | `print()` |
| `pdb.set_trace()` | `breakpoint()` (built-in do Python 3.7+, chama o pdb) |
| `raise Exception(...)` | `raise Exception(...)` / `raise HTTPException(status_code=400, ...)` |
| `try/except` | `try/except` |

O que muda é que erro não tratado em rota async pode ser mais chato de
rastrear no terminal — o traceback fica mais longo por causa do asyncio.
Dica: comece sempre com `print()` simples na função da rota antes de
sair caçando erro de "async".

Erro de validação (Pydantic) nem chega no seu código: se você fez
`name: str` e mandaram `name: 123`, o FastAPI já responde 422 sozinho,
sem seu `print` disparar — não é bug seu, é o comportamento esperado.

`HTTPException` é o `raise` "oficial" da API:
```python
from fastapi import HTTPException
raise HTTPException(status_code=404, detail="usuário não encontrado")
```
