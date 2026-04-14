
import csv
import time
from typing import List

from model.proxy.transacao import Transacao

class CsvReader():
    __filename= 'dados.csv'
    
    __COLUNA_DATA = 'DATA DA TRANSAÇÃO'
    __COLUNA_VALOR = 'VALOR'
    __COLUNA_INSTITUICAO = 'INSTITUIÇÃO'

    def read(self) -> List[Transacao]:
        print('Início do processamento do CSV...')
        start = time.perf_counter()
        transacoes : List[Transacao] = []
        with open(self.__filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Linha={reader.line_num}")
                partida = self.__criar_transacao(row)
                transacoes.append(partida)
        end = time.perf_counter()
        print(f"Quantida de transações: {transacoes.__len__()}")
        print(f"Tempo de execução do processamento do CSV: {end - start:.1f} segundos")
        return transacoes
    
    def __criar_transacao(self, row: dict[str, str]) -> Transacao:
        data = row.get(self.__COLUNA_DATA)
        valor = row.get(self.__COLUNA_VALOR)
        instituicao = row.get(self.__COLUNA_INSTITUICAO)

        return Transacao(
            data,
            int(valor),
            instituicao 
        )
