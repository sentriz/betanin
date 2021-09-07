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
        conf = conf_betanin.read()
        return {"api_key": conf_betanin.find_api_key(conf)}
