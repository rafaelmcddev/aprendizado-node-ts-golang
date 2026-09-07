from fastapi import APIRouter, HTTPException

from app.models import user as user_model
from app.models.user import User, UserCreate

# Isto aqui é o "urls.py + views.py" do Django, só que junto.
router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def index() -> list[User]:
    return user_model.find_all()


@router.get("/{user_id}")
def show(user_id: int) -> User:
    # user_id: int já valida sozinho — se mandar texto, nem chega aqui
    user = user_model.find_by_id(user_id)
    if user is None:
        # debug tip: print(user_id) aqui mostra o valor já validado
        raise HTTPException(status_code=404, detail="usuário não encontrado")
    return user


@router.post("/", status_code=201)
def store(data: UserCreate) -> User:
    return user_model.create(data)
