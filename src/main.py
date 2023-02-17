from src.structure_functions import StructureFunction
from src.db.concrete.list_engine import ListEngine

funcoes = StructureFunction
engine = ListEngine

funcoes.inicio()
funcoes.quantidade_tabelas(funcoes.create_table)
funcoes.todos_os_carros()
funcoes.add_veiculo()
funcoes.remover_veiculo()
