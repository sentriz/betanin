# betanin
import betanin.config.betanin as conf_betanin
from betanin.rest.base import SecureResource
from betanin.rest_models import response as resp_models
from betanin.rest.namespaces import CLIENTS_NS


@CLIENTS_NS.route("/api_key")
class LoginResource(SecureResource):
    @staticmethod
    @CLIENTS_NS.marshal_with(resp_models.API_KEY)
    def get():
        "fetches the clients api key"
        return {"api_key": conf_betanin.get_api_key()}
