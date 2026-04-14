
from model.observer.auditoria_service import AuditoriaService
from model.observer.estoque_service import EstoqueService

class Service: 
    __auditoria_service: AuditoriaService
    __estoque_service: EstoqueService

    def __init__(self, auditoria_service: AuditoriaService, estoque_service: EstoqueService):
        self.__auditoria_service = auditoria_service
        self.__estoque_service = estoque_service
    
    def alterar_estoque(self, nome_item: str, quantidade: int):
        self.__auditoria_service.auditar(nome_item, quantidade)
        self.__estoque_service.atualizar(nome_item, quantidade)