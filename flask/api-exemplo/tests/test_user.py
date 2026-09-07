import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()


def test_lista_usuarios(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_busca_usuario_existente(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Ada Lovelace"


def test_busca_usuario_inexistente(client):
    response = client.get("/users/999")
    assert response.status_code == 404


def test_cria_usuario(client):
    response = client.post(
        "/users/", json={"name": "Grace Hopper", "email": "grace@example.com"}
    )
    assert response.status_code == 201
    assert response.get_json()["name"] == "Grace Hopper"


def test_cria_usuario_sem_email(client):
    response = client.post("/users/", json={"name": "Sem Email"})
    assert response.status_code == 400
