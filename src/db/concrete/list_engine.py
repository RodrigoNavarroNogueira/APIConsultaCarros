from src.db.interface import AbstractEngine

import random
from datetime import datetime

class ListEngine(AbstractEngine):
    def __init__(self):
        super().__init__('carros')


    def create(self, id, marca, modelo, ano, created):
        query = f'''
            INSERT INTO car VALUES(
                {id},
                '{marca}',
                {modelo},
                '{ano}',
                '{created}'
            )
        '''
        self.cursor.execute(query)
        self.database.commit()


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


    def delete(self, escolha, produto):
        query = f'''
        DELETE from {escolha} WHERE product = '{produto}'
        '''
        self.cursor.execute(query)
        self.database.commit()
        return produto
