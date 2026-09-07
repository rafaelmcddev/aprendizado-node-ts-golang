# 05. Model / View / Controller

| Camada | Pasta | Faz o quê | Equivalente |
|---|---|---|---|
| Model | `src/models/` | dados e regra de negócio | `models.py` / Eloquent Model |
| Controller | `src/controllers/` | recebe request, chama model, monta resposta | `views.py` (Django) / Controller (Laravel) |
| View | `src/views/` | o que o usuário vê (aqui: HTML estático) | template Django / Blade |

Cuidado com o nome: em Django, "View" = o que em Node chamamos de
"Controller". Em Node/Rails/Laravel, "View" = o HTML/template mesmo.

Fluxo dentro de um controller:
```ts
export function show(req: Request, res: Response) {
  const user = userModel.findById(req.params.id); // Model
  res.json(user);                                  // resposta (aqui não tem View de template)
}
```

Não é uma regra do Node, é uma convenção que **você** organiza. Frameworks
como NestJS forçam mais estrutura; Express (usado aqui) deixa livre — por
isso este projeto já separa as pastas pra você começar com boas práticas.
