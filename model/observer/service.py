from model.observer.estoque_publisher import EstoquePublisher


class Service: 
    __publisher: EstoquePublisher

    def __init__(self, publisher: EstoquePublisher):
        self.__publisher = publisher
    
    def alterar_estoque(self, nome_item: str, quantidade: int):
        self.__publisher.notify(nome_item, quantidade)