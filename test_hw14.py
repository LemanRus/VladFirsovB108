import hw14_client, hw14_server


def test_server():
    res = hw14_server.server_works()
    assert res is None


def test_client():
    pass