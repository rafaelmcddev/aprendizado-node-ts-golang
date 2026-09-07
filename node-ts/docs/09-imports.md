# 09. Onde ficam os imports

Sempre no **topo do arquivo**, igual Python/PHP.

```ts
import express from 'express';           // biblioteca externa (node_modules)
import { findById } from '../models/user.model'; // arquivo seu (caminho relativo)
import type { User } from '../types';    // "type" = só existe em tempo de compilação, some no JS final
```

Regras rápidas:
- Sem `./` ou `../` → é do `node_modules` (biblioteca instalada)
- Com `./` ou `../` → é arquivo seu, no seu projeto
- `import type` → importa só o tipo (equivalente a não existir em runtime,
  serve só pro TypeScript checar antes de compilar)

Não precisa `__init__.py` nem autoload do Composer — cada arquivo `.ts` já
é importável direto pelo caminho dele.
