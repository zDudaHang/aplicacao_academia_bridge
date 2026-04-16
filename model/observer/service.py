
from model.observer.auditoria_service import AuditoriaService
from model.observer.email_service import EmailService
from model.observer.estoque_service import EstoqueService
from model.observer.fornecedor_service import FornecedorService

class Service: 
    __auditoria_service: AuditoriaService
    __estoque_service: EstoqueService
    __email_service: EmailService
    __fornecedor_service: FornecedorService

    def __init__(
            self,
              auditoria_service: AuditoriaService, 
              estoque_service: EstoqueService, 
              email_service: EmailService, 
              fornecedor_service: FornecedorService
        ):
        self.__auditoria_service = auditoria_service
        self.__estoque_service = estoque_service
        self.__email_service = email_service
        self.__fornecedor_service = fornecedor_service
    
    def alterar_estoque(self, nome_item: str, quantidade: int):
        self.__auditoria_service.auditar(nome_item, quantidade)
        self.__estoque_service.atualizar(nome_item, quantidade)
        self.__email_service.enviar_email()
        self.__fornecedor_service.solicitar_mais_produtos()
