# 08. Como instalar e usar dependências

Gerenciador: **npm** (vem com o Node), equivalente ao `pip`/`composer`.

```bash
npm install express        # instala e grava em package.json + package-lock.json
npm install -D typescript  # -D = só dev (equivalente a requirements-dev.txt)
npm install                # instala tudo que já está no package.json (== pip install -r requirements.txt)
```

Onde fica instalado: pasta `node_modules/` (parecido com `venv/`, mas
**por projeto sempre**, nunca global tipo o Python permite). Nunca commite
essa pasta — já está no `.gitignore`.

**Como usar depois de instalar:**
```ts
import express from 'express';   // ES Modules (padrão deste projeto)
// ou
const express = require('express'); // CommonJS (mais antigo, ainda comum)
```

`package.json` guarda a versão; `package-lock.json` trava a versão exata
(equivalente ao `poetry.lock` / `composer.lock`) — sempre commite os dois.
