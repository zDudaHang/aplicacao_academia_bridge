from typing import List
from model.proxy.service import Service
from model.proxy.transacao import Transacao
import time
from datetime import date

class TransacaoService(Service):
    __transacoes : List[Transacao] = []

    def __init__(self, transacoes: List[Transacao]):
        self.__transacoes = transacoes
    
    def relatorio(self, data_inicio: date, data_fim: date ) -> dict[str, int]:
        print(f"[SERVICE] Gerando relatório do período {data_inicio.isoformat()} até {data_fim.isoformat()}")
        start = time.perf_counter()
        balanco_por_instituicao : dict[str, int] = {}
        
        for transacao in self.__transacoes:
            data_transacao = date.fromisoformat(transacao.data)
            if (data_transacao >= data_inicio and data_transacao <= data_fim):
                instituicao = transacao.instituicao
                balanco_atual = balanco_por_instituicao.get(instituicao)
                if (balanco_atual is None):
                    balanco_atual = 0
                balanco_por_instituicao[instituicao] = balanco_atual + transacao.valory
    
        end = time.perf_counter()
        print(f"[SERVICE] Tempo de execução: {end - start:.1f} segundos")
        return balanco_por_instituicao
    