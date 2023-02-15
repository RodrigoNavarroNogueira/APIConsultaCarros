from src.db.concrete.list_engine import ListEngine
from src.db.db_structure import DatabaseStructure
import sqlite3
from datetime import datetime
import random

class StructureFunction:
    def inicio():
        print('Começando o programa')


    def create_list():
        name_list = input('Escolha o nome da sua lista:\n').lower().strip()
        db.create_table_lista(name_list)
        return name_list


    def quantidade_tabelas(create_list):
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        if len(cursor.fetchall()) >= 1:
            print('Já existe a tabela')
        else:
            create_list()


    def add_produtos():
        marca = input('Digite a marca: (Para sair pressione "X") ').capitalize().strip()
        modelo = input('Digite o modelo: (Para sair pressione "X") ').capitalize().strip()
        ano = int(input('Ano?: '))
        engine.create(random.randint(1, 999), marca, modelo, ano, datetime.now())
        print(f'O carro {modelo} foi adicionado com sucesso')


banco = sqlite3.connect('carros.db')
cursor = banco.cursor()
engine = ListEngine()
db = DatabaseStructure()