from src.db.interface import AbstractEngine

class DatabaseStructure(AbstractEngine):
    def __init__(self):
        super().__init__('carros')


    def create_table_lista(self, name_list):
            self.cursor.execute(
                f'''
                CREATE TABLE {name_list}(
                    id INT PRIMARY KEY,
                    marca VARCHAR,
                    modelo VARCHAR,
                    ano INT,
                    created DATETIME
                )
                '''
            )
            self.database.commit()


    def drop_table_lista(self, name_list):
        query = f'DROP TABLE {name_list};'
        self.cursor.execute(query)
        self.database.commit()


    def rename_lista(self, name_list, new_name):
        query = f'ALTER TABLE {name_list} RENAME TO {new_name};'
        self.cursor.execute(query)
        self.database.commit()


#engine = DatabaseStructure()
#engine.drop_table_lista('testeum')