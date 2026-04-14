from abc import ABC, abstractmethod
from datetime import date

class Service(ABC):
    @abstractmethod
    def relatorio(self, data_inicio: date, data_fim: date ) -> dict[str, int]:
        pass
    
