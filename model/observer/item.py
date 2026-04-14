
class Item():
    __nome: str
    __quantidade: int = 0

    def __init__(self, nome: str, quantidade: int):
        self.__nome = nome
        self.__quantidade = quantidade
    
    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def quantidade(self) -> int:
        return self.__quantidade
    
    def alterar_estoque(self, quantidade: int):
        self.__quantidade += quantidade
    