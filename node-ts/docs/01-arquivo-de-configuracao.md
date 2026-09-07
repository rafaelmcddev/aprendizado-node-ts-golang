# 01. Arquivo de configuração

| Python/PHP | Node/TS | Pra que serve |
|---|---|---|
| `requirements.txt` / `composer.json` | `package.json` | lista dependências e scripts (`npm run dev`) |
| `.env` | `.env` | variáveis de ambiente (mesma ideia, mesma sintaxe) |
| `settings.py` / `config.php` | `src/config/index.ts` | config da sua aplicação (porta, chaves) — **arquivo que você mesmo cria** |
| — | `tsconfig.json` | configura o compilador TypeScript (pra onde compila, quão rígido é) |

Não existe um único "arquivo de config" mágico como no Django. Você cria
`src/config/index.ts` e ele lê o `.env`. Veja o exemplo real em
[`api-exemplo/src/config/index.ts`](../api-exemplo/src/config/index.ts).

`package.json` é o mais importante: `"scripts"` define os comandos
(`npm run dev` = como rodar em desenvolvimento), `"dependencies"` = o que
está instalado.
