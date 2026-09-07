from flask import Blueprint, jsonify, request

from app.models import user as user_model

# Blueprint = o jeito Flask de agrupar rotas de um "recurso".
# É o mais próximo que existe de um app do Django, mas bem mais simples.
bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/", methods=["GET"])
def index():
    return jsonify(user_model.find_all())


@bp.route("/<int:user_id>", methods=["GET"])
def show(user_id):
    user = user_model.find_by_id(user_id)
    if user is None:
        # debug tip: print(user_id) aqui mostra o valor cru vindo da URL
        return jsonify({"error": "usuário não encontrado"}), 404
    return jsonify(user)


@bp.route("/", methods=["POST"])
def store():
    data = request.get_json() or {}
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name e email são obrigatórios"}), 400

    user = user_model.create(name, email)
    return jsonify(user), 201
