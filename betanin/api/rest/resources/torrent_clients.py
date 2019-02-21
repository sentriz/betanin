# betanin
from betanin import main_config
from betanin.api.rest.base import SecureResource
from betanin.api.rest.models import response as resp_models
from betanin.api.rest.namespaces import clients_ns


@clients_ns.route('/api_key')
class LoginResource(SecureResource):
    @staticmethod
    @clients_ns.marshal_with(resp_models.api_key)
    def get():
        'fetches the clients api key'
        return {
            'api_key': main_config.get_api_key()
        }
