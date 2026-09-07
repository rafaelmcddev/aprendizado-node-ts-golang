from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_lista_usuarios():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_busca_usuario_existente():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Ada Lovelace"


def test_busca_usuario_inexistente():
    response = client.get("/users/999")
    assert response.status_code == 404


def test_cria_usuario():
    response = client.post(
        "/users/", json={"name": "Grace Hopper", "email": "grace@example.com"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Grace Hopper"


def test_valida_tipo_do_id():
    response = client.get("/users/abc")
    assert response.status_code == 422
