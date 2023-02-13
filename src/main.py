from flask import Flask, make_response, jsonify
from src.bd import carros

app = Flask(__name__)


@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(jsonify(carros))


app.run()