from typing import List

from model.observer.estoque_listener import EstoqueListener


class EstoquePublisher:
    __listeners : List[EstoqueListener] = []

    def subscribe(self, listener: EstoqueListener):
        self.__listeners.append(listener)
    
    def unsubscribe(self, listener: EstoqueListener):
        self.__listeners.remove(listener)
    
    def notify(self, nome_item: str, quantidade: int):
        for listener in self.__listeners:
            listener.update(nome_item, quantidade)
