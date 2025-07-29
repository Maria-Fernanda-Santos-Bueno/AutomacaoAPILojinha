from api.usuario_api import UsuarioAPI
from faker import Faker

def test_create_new_user_successfull():
    faker = Faker()
    nome = faker.name()
    login = faker.user_name()
    senha = faker.password()

    usuarioAPI = UsuarioAPI()
    response = usuarioAPI.create_new_user(nome, login, senha)

    response_json = response.json()
    data = response_json.get("data", {})
    assert data["usuarioId"] > 0, "ID do usuário deveria ser maior que 0."
    assert data["usuarioLogin"] == login, "Login retornado não corresponde ao enviado!"
    assert data["usuarioNome"] == nome, "Nome retornado não corresponde ao enviado!"
    assert response_json["message"] == "Usuário adicionado com sucesso"



