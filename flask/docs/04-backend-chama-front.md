# 04. Como o backend "fala" com o front

Mesma regra sempre: front chama backend, nunca o contrário.

Flask, diferente do FastAPI, **vem com template engine** (Jinja2, o mesmo
motor por trás do Django Templates) — por isso historicamente muita gente
usa Flask pra servir HTML direto do servidor.

**1. Front separado (API pura)**
```python
return jsonify(users)
```

**2. Servir HTML com Jinja2** (o "jeito Flask clássico")
```python
return render_template("index.html", users=users)
```

**3. Servir HTML estático simples** (o que este projeto faz, pra manter
o exemplo igual ao das outras linguagens)
```python
return send_from_directory("views", "index.html")
```

O `api-exemplo/` serve HTML estático com `fetch('/users')` — mesmo padrão
do `node-ts/`, `golang/` e `fastapi/`, pra comparação direta entre eles.
