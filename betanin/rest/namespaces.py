# betanin
from betanin.extensions import REST


# this removes the default namespace
REST.namespaces.clear()

TORRENTS_NS = REST.namespace(
    "torrents", description="operations related to torrents"
)
BEETS_NS = REST.namespace(
    "beets", description="operations related to beets and it's config"
)
NOTIFICATIONS_NS = REST.namespace(
    "notifications", description="operations related to notifications"
)
AUTHENTICATION_NS = REST.namespace(
    "authentication", description="operations related to authentication"
)
CLIENTS_NS = REST.namespace(
    "clients", description="operations related to the torrent clients"
)
META_NS = REST.namespace(
    "meta", description="operations related to betanin and the current system"
)
