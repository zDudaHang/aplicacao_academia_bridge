
import csv
from datetime import datetime

class AuditoriaService():
    __filename : str = 'auditoria.csv'

    __COLUNA_DATA_EVENTO = 'DATA DO EVENTO'
    __COLUNA_ITEM = 'ITEM'
    __COLUNA_EVENTO = 'EVENTO'

    def __init__(self):

        try:
            with open(self.__filename, "x") as file:
                writer = csv.DictWriter(file, fieldnames=[self.__COLUNA_DATA_EVENTO, self.__COLUNA_ITEM, self.__COLUNA_EVENTO])
                writer.writeheader()
        except FileExistsError:
            print(f"O arquivo {self.__filename} já existe.")
    
    def auditar(self, nome_item: str, quantidade: int):
        with open(self.__filename, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=[self.__COLUNA_DATA_EVENTO, self.__COLUNA_ITEM, self.__COLUNA_EVENTO])
            evento : str = f"{quantidade} unidades"
            writer.writerow({ self.__COLUNA_DATA_EVENTO: datetime.now().isoformat(), self.__COLUNA_ITEM: nome_item, self.__COLUNA_EVENTO : evento })