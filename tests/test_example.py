def test_request_example(client):
    """
    Test /example. Should return the sum of the given numbers.
    """
    response = client.post("/example", json={"numbers": [1, 2, 3]})
    assert response.json["result"] == 6
