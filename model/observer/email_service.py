
from model.observer.estoque_listener import EstoqueListener


class EmailService(EstoqueListener):
    
    def update(self, nome_item: str, quantidade: int):
        print("E-mail enviado")