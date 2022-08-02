def test_request_ascii_convert(client):
    """
    Test /convert. Should return the ASCII list's decimal representation multiplied by
    10 if between a, A and h, H.
    """
    response = client.post("/convert", json=["A", "h", "H", "x"])
    assert response.json == [650, 0, 0, 0]
