# betanin
import pytest


@pytest.fixture(scope="module")
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_api(client):
    resp = client.get("/")
    assert resp.status_code == 200
