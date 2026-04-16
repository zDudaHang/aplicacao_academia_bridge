
import csv
import shutil
from tempfile import NamedTemporaryFile
from typing import List

from model.observer.item import Item


class EstoqueService():
    __itens: List[Item] = [] 
    __filename : str = 'estoque.csv'

    __COLUNA_NOME_ITEM = 'NOME DO ITEM'
    __COLUNA_QUANTIDADE = 'QUANTIDADE EM ESTOQUE'

    def __init__(self):
        print(f"Iniciando leitura do {self.__filename}")
        with open(self.__filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = self.__criar_item(row)
                self.__itens.append(item)
        print(f"Quantidade de itens no estoque: {self.__itens.__len__()}")
    
    def __criar_item(self, row: dict[str, str]) -> Item:
        nome = row.get(self.__COLUNA_NOME_ITEM)
        quantidade = row.get(self.__COLUNA_QUANTIDADE)

        return Item(
            nome,
            int(quantidade)
        )

    def atualizar(self, nome_item: str, quantidade: int):
        tempfile = NamedTemporaryFile('w', newline='', delete=False)

        antiga_quantidade : int
        nova_quantidade : int
        for item in self.__itens:
            if (item.nome == nome_item):
                antiga_quantidade = item.quantidade
                item.alterar_estoque(quantidade)
                nova_quantidade = item.quantidade

        with tempfile:
            writer = csv.DictWriter(tempfile, fieldnames=[self.__COLUNA_NOME_ITEM, self.__COLUNA_QUANTIDADE])
            writer.writeheader()
            for item in self.__itens:
                writer.writerow({ self.__COLUNA_NOME_ITEM: item.nome, self.__COLUNA_QUANTIDADE: item.quantidade})
        
        shutil.move(tempfile.name, self.__filename)
        print("Estoque alterado com sucesso")
        print(f"Item {nome_item}: {antiga_quantidade} unidades -> {nova_quantidade} unidades")

    def listar_estoque(self): 
        print("\nESTOQUE")
        for item in self.__itens:
            print(f"{item.nome}: {item.quantidade} unidades")
