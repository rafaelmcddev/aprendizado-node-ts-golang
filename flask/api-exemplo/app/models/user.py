# "Model" = dados + regra de negócio. Sem ORM, sem banco de propósito
# — dado puro em memória (dict), pra focar no fluxo.

_users = [
    {"id": 1, "name": "Ada Lovelace", "email": "ada@example.com"},
    {"id": 2, "name": "Alan Turing", "email": "alan@example.com"},
]


def find_all():
    return _users


def find_by_id(user_id: int):
    return next((u for u in _users if u["id"] == user_id), None)


def create(name: str, email: str):
    user = {"id": len(_users) + 1, "name": name, "email": email}
    _users.append(user)
    return user
