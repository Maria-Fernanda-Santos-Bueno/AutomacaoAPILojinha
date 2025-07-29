from api.base_api import BaseAPI

class UsuarioAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = "/v2/usuarios"

    def create_new_user(self, name, login, password):
        payload = {
            "usuarioNome": name,
            "usuarioLogin": login,
            "usuarioSenha": password
        }
        return self.post(endpoint=self.endpoint, json=payload)
