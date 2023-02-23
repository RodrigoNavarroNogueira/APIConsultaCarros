from src.db.interface import AbstractEngine
from src.db.db_structure import DatabaseStructure
import sqlite3
from datetime import datetime as dt
import random as rd


class ListEngine(AbstractEngine):
    def __init__(self):
        super().__init__('carros')


    def create(self, id, marca, modelo, ano, created_at):
        try:
            banco
            cursor
            query = f'''
                INSERT INTO car VALUES(
                    {id},
                    '{marca}',
                    '{modelo}',
                    {ano},
                    '{created_at}'
                )
            '''
            self.cursor.execute(query)
            self.database.commit()
        except:
            banco.rollback()
        finally:
            banco.close()


    
    

    def read(self, query):
        result = self.cursor.execute(query)
        result = result.fetchall()
        return result


    def update(self, escolha, product_amount, novo, antigo):
        if product_amount == 'product':
            query = f"UPDATE {escolha} SET {product_amount} = '{novo}' WHERE {product_amount} = '{antigo}'"
            self.cursor.execute(query)
            self.database.commit()
            print('O produto foi alterado!')

        elif product_amount == 'amount':
            query = f"UPDATE {escolha} SET {product_amount} = {novo} WHERE product = '{antigo}'"
            self.cursor.execute(query)
            self.database.commit()
            print('A quantidade foi alterada!')


    def delete(self, modelo):
        query = f'''
        DELETE from car WHERE modelo = '{modelo}'
        '''
        self.cursor.execute(query)
        self.database.commit()
        return modelo

banco = sqlite3.connect('carros.db', check_same_thread=False)
cursor = banco.cursor()
engine = ListEngine()
db = DatabaseStructure()