# 02. Rota → qual arquivo é chamado

Não tem roteamento automático por pasta (tipo Django/Laravel auto-discovery
simples). Você declara a rota explicitamente, parecido com Flask/Laravel
manual:

```ts
// src/routes/user.routes.ts
router.get('/users/:id', userController.show);
```

Caminho até achar o código:

1. `src/server.ts` → sobe o servidor, importa `app.ts`
2. `src/app.ts` → registra os grupos de rotas (`app.use('/users', userRoutes)`)
3. `src/routes/user.routes.ts` → mapeia `GET /users/:id` → `userController.show`
4. `src/controllers/user.controller.ts` → função `show` executa

É basicamente igual a `urls.py` do Django ou `routes/web.php` do Laravel,
só que dividido por "recurso" (um arquivo de rotas por entidade).

Veja o real em [`api-exemplo/src/routes`](../api-exemplo/src/routes).
