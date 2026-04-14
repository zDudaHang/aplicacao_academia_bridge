from typing import List
from model.proxy.service import Service
from model.proxy.transacao import Transacao
import time
from datetime import date

class ProxyService(Service):
    __cache: dict[str, dict[str, int]] = {}
    __service: Service

    def __init__(self, service: Service):
        self.__service = service
    
    def relatorio(self, data_inicio: date, data_fim: date ) -> dict[str, int]:
        print(f"[PROXY] Gerando relatório do período {data_inicio.isoformat()} até {data_fim.isoformat()}")
        start = time.perf_counter()

        chave_cache = f"{data_inicio.isoformat()}-{data_fim.isoformat()}"
        
        balanco_por_instituicao : dict[str, int] = {}
        if (chave_cache in self.__cache):
            print("[PROXY] Resultado computado presente na cache")
            balanco_por_instituicao = self.__cache[chave_cache]
        else: 
            print("[PROXY] Resultado computado não está presente na cache")
            balanco_por_instituicao = self.__service.relatorio(data_inicio, data_fim)
            self.__cache[chave_cache] = balanco_por_instituicao
        
        end = time.perf_counter()
        print(f"[PROXY] Tempo de execução: {end - start:.1f} segundos")

        return balanco_por_instituicao
