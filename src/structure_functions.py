from src.db.concrete.list_engine import ListEngine
from src.db.db_structure import DatabaseStructure
import sqlite3
from datetime import datetime as dt
import random as rd

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
            id = rd.randint(1, 999)
            marca = input('Digite a marca: ')
            modelo = input('Digite o modelo: ')
            ano = int(input('Digite o ano: '))
            engine.create(id, marca, modelo, ano, dt.now())
            print(f'O carro {modelo} foi adicionado com sucesso')


    def tabelas_existentes_str():
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        print(cursor.fetchall())


banco = sqlite3.connect('carros.db')
cursor = banco.cursor()
engine = ListEngine()
db = DatabaseStructure()