from flask import Flask, make_response, jsonify, request
from src.bd import carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            message='Lista de carros',
            data=carros
            )
        )


@app.route('/carros/<int:id>', methods=['GET'])
def obter_carro_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    carros.append(carro)
    return make_response(
        jsonify(
            message='Carro cadastrado com sucesso',
            data=carro
            )
        )


app.run()
