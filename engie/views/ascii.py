from flask import Blueprint, jsonify, request

from engie.controllers import ascii

ascii_routes = Blueprint("convert", __name__, url_prefix="/convert")


@ascii_routes.post("")
def index():
    """
    Takes a json body with a list of ASCII characters and returns their decimal
    representation multiplied by 10 if they're below H or h, otherwise returns 0.

    Example input: ["A", "h", "H", "x"]
    Example output: [650, 0, 0, 0]
    """
    body = request.json
    return jsonify(ascii.multiply(body))
