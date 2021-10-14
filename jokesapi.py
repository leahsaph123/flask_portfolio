import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api')
jokes = []
joke_list = [
    "fjhdkal"
    "fdlkaj;sklf;d"
    "fdkaljs;jfl"
]
def _find_next_id():
    return max(jokes ["id"] for joke in jokes) + 1

def _init_jokes():
    idJokes = 1
    for joke in joke_list:
        jokes.append({"id": idJokes, "joke": joke})
        idJokes += 1


@api_bp.route('/joke')
def get_joke():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(random.choice(jokes))