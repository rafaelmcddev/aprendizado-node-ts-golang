# 00. "Mas isso não é o JavaScript de manipular botão?"

Não. E essa confusão é comum em quem vem de backend puro.

**JavaScript no navegador** (o que você sempre evitou):
```js
document.querySelector('#botao').addEventListener('click', () => {...})
```
Isso é DOM, evento de clique, blur, foco — coisa de **frontend**, roda
dentro do navegador. Você tem razão em nunca ter gostado disso pra
trabalho de backend.

**JavaScript no Node.js** (o que este repositório ensina):
```js
app.get('/users/:id', (req, res) => { res.json({...}) })
```
Isso roda no **servidor**, não existe navegador, não existe `document`,
não existe DOM, não existe clique. É a mesma linguagem (JS/TS), mas outro
ambiente de execução — parecido com a diferença entre PHP rodando no
servidor (Laravel) e o `alert()` de JS que às vezes aparecia dentro do
Blade. Mesma linguagem, mundos diferentes.

| | Frontend (navegador) | Backend (Node) |
|---|---|---|
| Onde roda | dentro do navegador do usuário | no seu servidor |
| APIs disponíveis | DOM, `window`, `document`, eventos de clique | sistema de arquivos, banco de dados, rede, HTTP |
| Equivalente que você já conhece | — (você sempre evitou) | Django (Python) / Laravel (PHP) |

Todo o resto deste `node-ts/` é 100% servidor: rotas, controllers, model,
banco. Em nenhum lugar você vai ver `document` ou `addEventListener`. Se
aparecer, é bug.
