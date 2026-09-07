# Glossário cruzado

Mesmo conceito, nome diferente em cada lugar. Use esta tabela quando ler
documentação de alguma stack e travar num termo — ache a linha, veja o
que já conhece.

| Conceito | Django | Laravel | Node + TS | Go | FastAPI | Flask |
|---|---|---|---|---|---|---|
| Onde declara a URL | `urls.py` | `routes/web.php` | `routes/*.routes.ts` | `routes/routes.go` | `routers/*.py` (`APIRouter`) | `routes/*.py` (`Blueprint`) |
| Função que processa a rota | View (`views.py`) | Controller | Controller | Controller (função) | Path operation (função com decorator) | View function (função com decorator) |
| Onde ficam os dados | Model (`models.py`, com ORM) | Model (Eloquent) | Model (funções, sem ORM aqui) | Model (`struct`, sem ORM aqui) | Model Pydantic (validação) + Model SQLAlchemy (banco) | dict/`db.Model` (Flask-SQLAlchemy) |
| Instância principal da app | não existe (é o projeto inteiro) | `$app` | `app` (Express) | `mux` (`http.ServeMux`) | `app` (`FastAPI()`) | `app` (`Flask()`) |
| Função que "monta" a app | não existe (settings já é global) | não existe | `app.ts` (arquivo) | `routes.New()` | `main.py` (arquivo) | `create_app()` (factory) |
| Middleware | Middleware (`MIDDLEWARE` em settings) | Middleware | Middleware (`app.use(...)`) | Middleware (função que envolve o handler) | Middleware (`@app.middleware`) | Middleware (`before_request`) |
| ORM | Django ORM (embutido) | Eloquent (embutido) | Prisma / TypeORM / Knex (você escolhe) | GORM (você escolhe) | SQLAlchemy (você escolhe) | Flask-SQLAlchemy (você escolhe) |
| Criar migration | `makemigrations` | `make:migration` | `prisma migrate dev` | `migrate create` (golang-migrate) | `alembic revision --autogenerate` | `flask db migrate` |
| Aplicar migration | `migrate` | `migrate` | aplicado junto no `migrate dev` | `migrate ... up` | `alembic upgrade head` | `flask db upgrade` |
| Instalar dependência | `pip install` | `composer install` | `npm install` | `go get` | `pip install` | `pip install` |
| Arquivo de dependências | `requirements.txt` | `composer.json` | `package.json` | `go.mod` | `requirements.txt` | `requirements.txt` |
| Rodar servidor dev | `manage.py runserver` | `php artisan serve` | `npm run dev` | `go run main.go` | `uvicorn app.main:app --reload` | `flask run` / `python run.py` |
| Rodar testes | `pytest` / `manage.py test` | `phpunit` / `artisan test` | `npm test` (Vitest) | `go test ./...` | `pytest` | `pytest` |
| Simular requisição no teste | `Client()` (Django Test) | `$this->get(...)` | `supertest` (lib externa) | `httptest` (standard library) | `TestClient` | `test_client()` |
| Debugger interativo | `pdb` / `ipdb` | Xdebug | `debugger;` + VS Code | `dlv` (Delve) | `pdb` / `breakpoint()` | `pdb` / `breakpoint()` |
| "self"/referência ao próprio objeto | `self` | `$this` | `this` | receiver (`func (u User) ...`) | `self` | `self` |
| Documentação automática da API | não tem (precisa de lib extra tipo DRF) | não tem (precisa de lib extra) | não tem (precisa de lib extra) | não tem (precisa de lib extra) | `/docs` (Swagger, embutido) | não tem (precisa de lib extra) |

## Como usar

Se um doc de uma stack usa um termo que não faz sentido, procura a linha
aqui, olha a coluna do que você já sabe (Django ou Laravel) e volta pro
doc com o significado já claro.
