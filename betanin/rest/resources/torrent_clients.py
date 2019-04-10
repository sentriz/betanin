# betanin
from betanin import main_config
from betanin.rest.base import SecureResource
from betanin.rest.models import response as resp_models
from betanin.rest.namespaces import CLIENTS_NS


@CLIENTS_NS.route("/api_key")
class LoginResource(SecureResource):
    @staticmethod
    @CLIENTS_NS.marshal_with(resp_models.API_KEY)
    def get():
        "fetches the clients api key"
        return {"api_key": main_config.get_api_key()}
