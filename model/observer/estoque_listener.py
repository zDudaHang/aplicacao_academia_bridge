from abc import ABC, abstractmethod

class EstoqueListener(ABC):
    @abstractmethod
    def update(self, nome_item: str, quantidade: int):
        pass
