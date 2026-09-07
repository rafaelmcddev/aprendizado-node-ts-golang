from pydantic import BaseModel


# Schema Pydantic: define o formato dos dados. Valida automaticamente
# entrada (request) e saída (response) — sem você escrever `if` nenhum.
class User(BaseModel):
    id: int
    name: str
    email: str


class UserCreate(BaseModel):
    name: str
    email: str


# "Banco" em memória, só pra focar no fluxo, sem SQL.
_users: list[User] = [
    User(id=1, name="Ada Lovelace", email="ada@example.com"),
    User(id=2, name="Alan Turing", email="alan@example.com"),
]


def find_all() -> list[User]:
    return _users


def find_by_id(user_id: int) -> User | None:
    return next((u for u in _users if u.id == user_id), None)


def create(data: UserCreate) -> User:
    user = User(id=len(_users) + 1, name=data.name, email=data.email)
    _users.append(user)
    return user
