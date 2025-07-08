from api.login_api import LoginAPI

def test_token_sucessful():
    loginAPI = LoginAPI()
    response = loginAPI.get_token("admin", "admin")
    data = response.json()
    
    assert not data['data'] is None, "O token retornou vazio"
    assert data["message"] == "Sucesso ao realizar o login"