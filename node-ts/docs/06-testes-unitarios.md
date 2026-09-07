# 06. Onde ficam os testes unitários

Convenção: arquivo `*.test.ts` do lado do que ele testa, ou tudo dentro de
`src/tests/`. Este projeto usa `src/tests/`.

Ferramenta: **Vitest** (parecido com PyTest — sintaxe simples, roda rápido).
Equivalente a `pytest` (Python) ou `PHPUnit` (PHP).

```ts
// src/tests/user.test.ts
import { describe, it, expect } from 'vitest';
import { findById } from '../models/user.model';

describe('user model', () => {
  it('acha usuário existente', () => {
    expect(findById(1)?.name).toBe('Ada');
  });
});
```

Rodar: `npm test` (script já configurado no `package.json`).

Igual PyTest: `describe` agrupa (classe de teste), `it`/`test` é o caso,
`expect(...).toBe(...)` é o assert.
