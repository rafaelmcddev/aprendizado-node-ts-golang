# 11. Migrations

Este projeto não usa banco (dados em memória, de propósito). Migration só
faz sentido quando existe banco de verdade — mas você vai precisar disso
no primeiro projeto real, então aqui vai o conceito.

## O que é

Migration = um arquivo que descreve **uma mudança** no schema do banco
(criar tabela, adicionar coluna, etc), versionado e aplicado em ordem.
Mesmo conceito do Django, só que Node não vem com isso de fábrica — você
escolhe uma ferramenta.

## Diferente do Django: você escolhe a ferramenta

Node **não tem ORM oficial**. As mais usadas hoje:

| Ferramenta | Comando de criar migration | Comando de aplicar |
|---|---|---|
| **Prisma** (mais popular atualmente) | `npx prisma migrate dev --name cria_users` | roda junto com o `dev` acima |
| **Knex** (query builder, mais manual) | `npx knex migrate:make cria_users` | `npx knex migrate:latest` |
| **TypeORM** | `npx typeorm migration:generate` | `npx typeorm migration:run` |

Comparando com o que você já faz em Django:

| Django | Prisma (equivalente mais próximo) |
|---|---|
| `models.py` (define o modelo) | `schema.prisma` (arquivo separado, não é uma classe TS) |
| `python manage.py makemigrations` | `npx prisma migrate dev` (gera **e** aplica de uma vez) |
| `python manage.py migrate` | já aplicado no comando acima |
| pasta `migrations/` com arquivos `.py` | pasta `prisma/migrations/` com arquivos `.sql` |

## Exemplo de schema Prisma (equivalente ao `models.py`)

```prisma
// prisma/schema.prisma
model User {
  id    Int    @id @default(autoincrement())
  name  String
  email String @unique
}
```

Rodar `npx prisma migrate dev --name cria_users` gera um arquivo SQL
dentro de `prisma/migrations/<timestamp>_cria_users/migration.sql` — bem
parecido com o arquivo que o Django gera em `migrations/0001_initial.py`,
só que em SQL puro em vez de código Python.

## Resumindo pra você que vem de Django

O conceito é idêntico (mudança versionada, aplicada em ordem, com
histórico). A diferença é que em Node **você monta essa parte manualmente
escolhendo a ferramenta**, não vem pronto.
