# 07. Como debugar (dd/print/raise?)

Idêntico ao que você já usa em Django/Python puro:

| O que você já faz | Continua igual |
|---|---|
| `print()` | `print()` |
| `pdb.set_trace()` | `breakpoint()` |
| `raise Exception(...)` | `raise Exception(...)` / `abort(404)` |
| `try/except` | `try/except` |

Diferencial do Flask: rodando com `debug=True`, qualquer erro não tratado
vira uma página de erro interativa no navegador (Werkzeug debugger) —
parecido com a página de erro do Django em modo `DEBUG=True`, mas dá pra
abrir um console Python **dentro do traceback**, direto no navegador.

```python
app.run(debug=True)  # nunca em produção, só local
```

`abort(404)` é o "raise" de HTTP mais comum:
```python
from flask import abort
abort(404, description="usuário não encontrado")
```
