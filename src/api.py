from flask import Flask, make_response, jsonify, request
from src.structure_functions import StructureFunction
from src.db.concrete.list_engine import ListEngine

funcoes = StructureFunction
engine = ListEngine

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

carros = funcoes.todos_os_carros()
# Se colocar a função add_veiculo dá erro ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 5648 and this is thread id 22096.
# Se colocar a função engine.create dá erro ListEngine.create() missing 1 required positional argument: 'self'


@app.route('/carros', methods=['GET'])
# Busca todos os carros
def get_carros():
    return jsonify(carros)


@app.route('/carros/<int:id>', methods=['GET'])
# Busca todos os carros por ID
def obter_carro_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    funcoes.add_veiculo(carro)
    return make_response(
        jsonify(
            message='Carro cadastrado com sucesso',
            data=carro
            )
        )


@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.json()
    for index, carro in enumerate(carros):
        if carro.get('id') == id:
            carros[index].update(carro_alterado)
            return jsonify(carros[index])


@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    funcoes.remover_veiculo(id)
    return jsonify(carros)


app.run()
