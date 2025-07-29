from api.usuario_api import UsuarioAPI
from faker import Faker

def test_create_new_user_successfull():
    f = Faker()
    usuarioNome = f.name()
    usuarioLogin = f.name()
    usuarioSenha = f.password()
    
    usuarioAPI = UsuarioAPI()
    response = usuarioAPI.create_new_user(usuarioNome, usuarioLogin, usuarioSenha)
    responseJson = response.json()
    data = responseJson.get("data", {})
    assert data["usuarioId"] > 0
    assert data["usuarioLogin"] == usuarioLogin
    assert data["usuarioNome"] == usuarioNome
    assert responseJson["message"] == "Usuário adicionado com sucesso"



