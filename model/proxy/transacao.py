from datetime import date

class Transacao():
    __data: date
    __valor: str
    __instituicao: str


    def __init__(self, data: date, valor: int, instituicao: str):
        self.__data = data
        self.__valor = valor
        self.__instituicao = instituicao

    @property
    def data(self) -> date:
        return self.__data

    @property
    def valor(self) -> int:
        return self.__valor
    
    @property
    def instituicao(self) -> str:
        return self.__instituicao