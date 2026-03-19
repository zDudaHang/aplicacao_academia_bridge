from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, mensagem: str):
        pass
    
    @abstractmethod
    def danger(self, mensagem: str):
        pass

    @abstractmethod
    def success(self, mensagem: str):
        pass
    
    @abstractmethod
    def warning(self, mensagem: str):
        pass

    @abstractmethod
    def info(self, mensagem: str):
        pass
