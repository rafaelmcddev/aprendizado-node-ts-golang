# 11. Migrations

Este projeto não usa banco (dados em memória, de propósito). Assim como
em Node, Go **não tem ORM oficial** nem sistema de migration embutido —
você escolhe a ferramenta.

## O que é (mesmo conceito do Django)

Migration = arquivo versionado que descreve uma mudança no schema do
banco, aplicado em ordem, com histórico do que já rodou.

## Ferramentas mais usadas em Go

| Ferramenta | O que é |
|---|---|
| **golang-migrate** | só migrations, puro SQL, sem ORM — a mais comum em projetos que usam `database/sql` puro (como o `api-exemplo/` deste repo faria) |
| **GORM** | ORM completo (mais parecido com o ORM do Django), tem `AutoMigrate()` |
| **goose** | parecida com golang-migrate, também baseada em arquivos SQL |

## Exemplo com golang-migrate (a mais comum)

```bash
migrate create -ext sql -dir db/migrations -seq cria_users
```

Isso gera **dois** arquivos (Go sempre separa "aplicar" de "desfazer",
igual o Django faz por trás dos panos, mas aqui explícito em SQL puro):

```
db/migrations/000001_cria_users.up.sql
db/migrations/000001_cria_users.down.sql
```

```sql
-- 000001_cria_users.up.sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
```
```sql
-- 000001_cria_users.down.sql
DROP TABLE users;
```

Aplicar:
```bash
migrate -database "postgres://..." -path db/migrations up
```

## Comparando com o que você já faz em Django

| Django | golang-migrate |
|---|---|
| `models.py` (Python vira SQL escondido) | você escreve o SQL direto, sem tradução |
| `makemigrations` (gera automático a partir do model) | você escreve o `.sql` na mão |
| `migrate` (aplica) | `migrate ... up` (aplica) |
| `migrate <app> <número>` (desfaz) | `migrate ... down` (roda o `.sql` de desfazer) |
| histórico guardado em tabela `django_migrations` | histórico guardado em tabela `schema_migrations` |

## Resumindo pra você que vem de Django

Maior diferença de mentalidade: no Django o SQL é **gerado** a partir do
`models.py`. Em Go (com golang-migrate), **você escreve o SQL direto** —
mais controle, mais trabalho manual. Se quiser algo mais próximo do
Django (model em código gerando SQL), aí sim entra o GORM.
