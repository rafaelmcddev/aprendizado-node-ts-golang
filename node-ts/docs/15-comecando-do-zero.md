# 15. Começando um projeto do zero (sem copiar o `api-exemplo/`)

O `api-exemplo/` deste repo já vem pronto. Aqui está a sequência real de
comandos e arquivos se você fosse começar um projeto novo do absoluto
zero, sozinho.

## 1. Comandos iniciais

```bash
mkdir meu-projeto && cd meu-projeto
npm init -y                                          # cria package.json
npm install express dotenv
npm install -D typescript tsx @types/node @types/express
npx tsc --init                                        # cria tsconfig.json
```

## 2. Sequência de arquivos (nessa ordem, cada um depende do anterior)

1. `.env` → variáveis de ambiente
2. `src/config/index.ts` → lê o `.env`
3. `src/models/*.ts` → dados (não depende de mais nada)
4. `src/controllers/*.ts` → depende do model
5. `src/routes/*.ts` → depende do controller
6. `src/app.ts` → junta tudo (middlewares + rotas)
7. `src/server.ts` → sobe o servidor (depende do `app.ts` e do `config`)

Essa é a mesma ordem usada no `api-exemplo/` deste repositório — dá pra
comparar arquivo por arquivo.

## 3. Rodar

Adicione em `package.json`:
```json
"scripts": { "dev": "tsx watch src/server.ts" }
```
```bash
npm run dev
```

## 4. Onde ficam os logs

`console.log`/`console.error` imprimem direto no **terminal** onde você
rodou `npm run dev` (stdout/stderr) — não existe arquivo de log
automático, diferente do Laravel, que já grava sozinho em
`storage/logs/laravel.log`.

Se fechar o terminal, perde o log. Pra gravar em arquivo, duas opções:
```bash
npm run dev > saida.log 2>&1     # redireciona manualmente
```
ou instalar uma lib de log estruturado (`winston`, `pino`) — comum em
projeto de verdade, fora do escopo deste repositório didático.
