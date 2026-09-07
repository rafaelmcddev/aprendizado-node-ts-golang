# 07. Como debugar (equivalente a `dd()` / `print()` / `raise`)

| Python/PHP | Node/TS | Uso |
|---|---|---|
| `print()` | `console.log()` | mostrar valor no terminal |
| `dd($var)` (Laravel) | `console.log(var); process.exit()` | mostrar e parar |
| `pdb.set_trace()` | `debugger;` | pausa real, com breakpoint navegável |
| `raise Exception(...)` | `throw new Error('...')` | lançar erro |
| `try/except` | `try/catch` | capturar erro |

**No dia a dia, 90% é `console.log`.** Não tem vergonha nisso, todo mundo
usa. Exemplo:
```ts
console.log('user recebido:', req.params.id);
```

**Debugger de verdade (equivalente ao `pdb`)**: no VS Code, aperte F5 com o
projeto aberto — ele já lê o `.vscode/launch.json` deste repo, para no
`debugger;` ou em breakpoints clicados na margem do editor.

Erros não tratados derrubam o processo (igual PHP sem try/catch mostra
stack trace). Middleware de erro do Express captura isso globalmente —
veja `src/app.ts`, o último `app.use` do arquivo.
