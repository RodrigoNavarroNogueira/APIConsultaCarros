from src.structure_functions import StructureFunction
from src.db.concrete.list_engine import ListEngine

funcoes = StructureFunction
engine = ListEngine

funcoes.inicio()
funcoes.quantidade_tabelas(funcoes.create_list)
table_name = 'car'
funcoes.add_produtos()
