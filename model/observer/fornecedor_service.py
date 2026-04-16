
from model.observer.estoque_listener import EstoqueListener


class FornecedorService(EstoqueListener):
    
    def update(self, nome_item: str, quantidade: int):
        print("Mais produtos foram solicitados")