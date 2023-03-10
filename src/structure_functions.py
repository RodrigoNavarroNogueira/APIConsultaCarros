from src.db.concrete.list_engine import ListEngine
from src.db.db_structure import DatabaseStructure
import sqlite3
from datetime import datetime as dt
import random as rd

class StructureFunction:
    def inicio():
        print('Começando o programa')


    def create_table():
        name_list = input('Escolha o nome da sua lista:\n').lower().strip()
        db.create_table_lista(name_list)
        return name_list


    def quantidade_tabelas(create_list):
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        if len(cursor.fetchall()) >= 1:
            print('Já existe a tabela')
        else:
            create_list()


    def todos_os_carros():
        cursor.execute(f"SELECT * FROM car")
        x = list(cursor.fetchall())
        carros = []
        count = 0
        for chave in x:
            carro = {}
            carro['id'] = x[count][0]
            carro['marca'] = x[count][1]
            carro['modelo'] = x[count][2]
            carro['ano'] = x[count][3]
            carro['created'] = x[count][4]
            count += 1
            carros.append(carro)
        return carros


    def add_veiculo(carro):
            id = carro['id']
            marca = carro['marca']
            modelo = carro['modelo']
            ano = carro['ano']
            engine.create(id, marca, modelo, ano, dt.now())
            print(f'O carro {modelo} foi adicionado com sucesso')


    def tabelas_existentes_str():
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        print(cursor.fetchall())


    def remover_veiculo(id):
        engine.delete(id)
        print(f'O carro {id} foi excluido com sucesso')


banco = sqlite3.connect('carros.db', check_same_thread=False)
cursor = banco.cursor()
engine = ListEngine()
db = DatabaseStructure()
