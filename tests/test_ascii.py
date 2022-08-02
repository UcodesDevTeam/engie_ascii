def test_request_ascii_convert(client):
    """
    Test /convert. Should return the ASCII list's decimal representation multiplied by
    10 if between a-A and h-H.
    """
    response = client.post("/convert", json=["A", "h", "H", "x"])
    assert response.json == [650, 0, 0, 0]


def test_request_ascii_convert_invalid_input_1(client):
    """
    Test /convert. Invalid body. Should return error.
    """
    response = client.post("/convert", json={"ascii": ["a", "b", "c", "d"]})
    expected = "type_error.list"
    assert response.json["validation_error"]["body_params"][0]["type"] == expected


def test_request_ascii_convert_invalid_input_2(client):
    """
    Test /convert. Too many characters. Should return error.
    """
    response = client.post("/convert", json=["a", "b", "cd"])
    expected = "value_error.any_str.max_length"
    assert response.json["validation_error"]["body_params"][0]["type"] == expected
