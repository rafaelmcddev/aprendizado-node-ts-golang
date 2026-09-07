from flask import Flask, send_from_directory

from app.config import Config
from app.routes.user import bp as users_bp


def create_app():
    # create_app() = "fábrica" da aplicação. Padrão Flask pra facilitar
    # testes (cada teste cria sua própria instância, isolada).
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(users_bp)

    @app.route("/")
    def home():
        # Serve o front estático — front chama backend, nunca o contrário.
        return send_from_directory(app.root_path + "/views", "index.html")

    return app
