from api.login_api import LoginAPI

def test_token_sucessful():
    loginAPI = LoginAPI()
    response = loginAPI.get_token("admin", "admin")
    data = response.json()
    token = data.get("data", {}).get("token")
    
    assert token, "O token retornou vazio ou não existe"
    assert data["message"] == "Sucesso ao realizar o login" 