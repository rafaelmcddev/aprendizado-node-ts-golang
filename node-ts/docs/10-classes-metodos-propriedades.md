# 10. Classes, métodos e properties

Este projeto usa **funções soltas** nos models (estilo funcional, comum
em Express), não classes — por isso você não viu isso no `api-exemplo/`.
Mas classes existem em TS e você vai encontrar em qualquer projeto maior
(especialmente com TypeORM, NestJS, ou qualquer lib orientada a objeto).

## Anatomia de uma classe

```ts
class User {
  id: number;                 // property (campo)
  name: string;
  private senha: string;      // "private" existe de verdade aqui (diferente de Go)

  constructor(id: number, name: string, senha: string) {
    this.id = id;              // "this" = "self" do Python
    this.name = name;
    this.senha = senha;
  }

  greet(): string {            // método de instância
    return `Olá, ${this.name}`;
  }

  static fromEmail(email: string): User {  // método estático
    return new User(0, email.split('@')[0], '');
  }
}

const user = new User(1, 'Ada', '123');
user.greet();          // chama método de instância
User.fromEmail('a@a.com'); // chama método estático, sem instanciar
```

| Python | TypeScript |
|---|---|
| `class User:` | `class User {` |
| `def __init__(self, ...):` | `constructor(...) {` |
| `self` | `this` |
| `def metodo(self):` | `metodo() {` |
| `@staticmethod` | `static nome() {` |
| `@classmethod` | não existe direto — usa `static` que retorna a própria classe |
| convenção `_privado` | `private` de verdade (palavra-chave, erro de compilação se acessar de fora) |

## Getter/setter (property computada)

```ts
class User {
  private _email: string = '';

  get email(): string {
    return this._email;
  }

  set email(value: string) {
    this._email = value.toLowerCase();
  }
}

const u = new User();
u.email = 'ADA@EXAMPLE.COM'; // chama o "set" por trás
console.log(u.email);         // chama o "get" — imprime "ada@example.com"
```

Parecido com `@property` do Python, só que a sintaxe fica "escondida" —
parece acesso direto ao campo, mas roda uma função.

## Interface vs Class

```ts
interface UserShape {   // só o formato, sem implementação — "contrato"
  id: number;
  name: string;
}

class User implements UserShape {  // promete seguir esse formato
  id = 0;
  name = '';
}
```

`interface` não existe em Python/PHP nesse formato (mais perto de uma
`Protocol` do `typing` do Python, se você já viu). Só existe em tempo de
compilação — não sobra nada disso no JS final.
