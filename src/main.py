from flask import Flask, make_response, jsonify, request
from src.bd import carros

app = Flask(__name__)


@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(jsonify(carros))


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    carros.append(carro)
    return carro


app.run()