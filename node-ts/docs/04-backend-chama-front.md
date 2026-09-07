# 04. Como o backend "fala" com o front

Igual Python/PHP: o backend **não chama** o front. O front (React, HTML,
qualquer coisa) que faz uma requisição HTTP pro backend.

Duas formas comuns:

**1. API separada (o mais comum hoje, tipo DRF/API Platform)**
Front roda em outro processo/porta, chama sua API via `fetch`:
```js
fetch('http://localhost:3000/users').then(r => r.json())
```

**2. Backend serve HTML pronto (tipo Flask com Jinja / Blade)**
Express serve um arquivo estático e o próprio HTML tem um `<script>` que
faz o `fetch`. É o que o `api-exemplo/` faz, pra você ver os dois lados
sem precisar montar um projeto React.

Veja [`api-exemplo/src/views/index.html`](../api-exemplo/src/views/index.html):
a página HTML chama `fetch('/users')` e desenha a lista na tela.

Resumindo: não existe "backend chamando o front". Existe front chamando
backend via HTTP — o backend só responde JSON (ou HTML).
