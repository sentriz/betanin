# standard library
import random
import string
from string import Template

# 3rd party
import gevent
from apprise import Apprise
from apprise import AppriseAsset

# betanin
import betanin.config.betanin as conf_betanin
from betanin.status import Status


_apprise_asset = AppriseAsset()
_apprise_asset.app_id = "betanin"
_apprise_asset.app_desc = "betanin"
_apprise_asset.async_mode = False
APPRISE = Apprise(asset=_apprise_asset)
STATUS_LONG = {
    Status.COMPLETED: "has completed",
    Status.FAILED: "has failed",
    Status.NEEDS_INPUT: "needs input",
}


def _random_string(size=6, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))


def _make_templates(config):
    return {
        "title": Template(config["notifications"]["strings"]["title"]),
        "body": Template(config["notifications"]["strings"]["body"]),
    }


def register_all():
    config = conf_betanin.read()
    APPRISE.clear()
    APPRISE.add(
        [
            f'{service["protocol"]}://{service["not_protocol"]}'
            for service in config["notifications"]["services"].values()
            if all(
                service[key] for key in ("enabled", "protocol", "not_protocol")
            )
        ]
    )


def get_possible_services():
    return APPRISE.details()


def get_services():
    with conf_betanin.mutate() as config:
        # remove incomplete services
        config["notifications"]["services"] = {
            service_id: service
            for service_id, service in config["notifications"][
                "services"
            ].items()
            if service["not_protocol"]
        }
        return config["notifications"]["services"]


def get_strings():
    config = conf_betanin.read()
    return config["notifications"]["strings"]


def add_service(service_type):
    service_id = _random_string(16)
    with conf_betanin.mutate() as config:
        config["notifications"]["services"][service_id] = {
            "type": service_type,
            "enabled": True,
            "protocol": "",
            "not_protocol": "",
        }
        return {
            "id": service_id,
            **config["notifications"]["services"][service_id],
        }


def update_services(services):
    with conf_betanin.mutate() as config:
        config["notifications"]["services"] = services
    register_all()


def test_services():
    return APPRISE.notify(
        title="betanin test notification", body="testing succeeded 😎"
    )


def update_strings(strings):
    with conf_betanin.mutate() as config:
        config["notifications"]["strings"] = strings


def send(torrent):
    config = conf_betanin.read()
    templates = _make_templates(config)
    torrents_path = (
        "complete" if torrent.status == Status.COMPLETED else "active"
    )
    variables = {
        "name": torrent.name,
        "id": torrent.id,
        "time": torrent.updated,
        "console_path": f"#/torrents/{torrents_path}/console/{torrent.id}",
        "status": STATUS_LONG.get(
            torrent.status,  # custom
            f"has status {torrent.status.name.lower()}",  # default
        ),
    }
    APPRISE.notify(
        title=templates["title"].safe_substitute(variables),
        body=templates["body"].safe_substitute(variables),
    )


def send_async(torrent):
    gevent.spawn(send, torrent)
