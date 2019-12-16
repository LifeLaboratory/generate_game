from flask import request, jsonify
from app import app
from app.game.processor import Processor

PREFIX = '/api/v1/game'


@app.route(PREFIX, methods=['GET', 'POST', 'PUT'])
def list_game():
    answer = dict()
    if request.method == 'GET':
        answer = jsonify(Processor().games())
    return answer


@app.route(PREFIX + '/<int:id_game>', methods=['GET'])
def once_game(id_game):
    answer = jsonify(Processor().game(id_game))
    return answer


@app.route(PREFIX + '/user/<int:id_user>', methods=['GET'])
def user_game(id_user):
    answer = jsonify(Processor().user_game(id_user))
    return answer
