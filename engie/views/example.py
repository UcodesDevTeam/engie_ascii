from flask import Blueprint, jsonify, request

from engie.controllers import example

example_routes = Blueprint("example", __name__, url_prefix="/example")


@example_routes.post("")
def index():
    """
    Takes a json body with a list of numbers and returns their sum.

    Example input: {"numbers": [1,2,3,4]}
    Example output: {"result": 10}
    """
    body = request.json
    return jsonify({"result": example.example_calculator(body["numbers"])})
