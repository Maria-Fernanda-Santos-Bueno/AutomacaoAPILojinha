from api.base_api import BaseAPI

class LoginAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = "/v2/login"

    def get_token(self, user, password):
        payload = {
            "usuarioLogin": user,
            "usuarioSenha": password
        }
        return self.post(endpoint=self.endpoint, json=payload)