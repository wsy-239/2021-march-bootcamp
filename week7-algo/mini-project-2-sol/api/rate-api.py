def get_rate(client_id: str) -> float:
    import requests
    response = requests.get("http://127.0.0.1:5000/rate/" + client_id)
    return float(response.content)


def upsert_client_rate(client_id: str, rate: float) -> None:
    import requests
    requests.post("http://127.0.0.1:5000/rate", json={"client_id": client_id, "rate": rate})


def test_get_rate() -> None:
    assert get_rate('client1') == 0.2
    assert get_rate('client-1') == 0.0


def test_upsert_rate() -> None:
    print(get_rate('client2'))
    upsert_client_rate("client2", 0.5)
    assert get_rate('client2') == 0.5

    upsert_client_rate("client0", 0.1)
    assert get_rate('client0') == 0.1


if __name__ == '__main__':
    test_get_rate()
    test_upsert_rate()
