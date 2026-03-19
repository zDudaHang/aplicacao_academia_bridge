from datetime import datetime

from model.logger import Logger

class ConsoleLogger(Logger):

    __name: str

    __RED='\033[91m'
    __GREEN = '\033[92m'
    __YELLOW = '\033[93m'
    __BLUE = '\033[94m'
    __RESET = '\033[0m'

    def __init__(self, name: str):
        self.__name = name

    def log(self, mensagem: str):
        now = datetime.now()
        print(f"{now.isoformat()} [LOG] {self.__name}: {mensagem}")

    def danger(self, mensagem: str):
        now = datetime.now()
        print(f"{now.isoformat()} [{self.__RED}DANGER{self.__RESET}] {self.__name}: {mensagem}")

    def success(self, mensagem: str):
        now = datetime.now()
        print(f"{now.isoformat()} [{self.__GREEN}SUCCESS{self.__RESET}] {self.__name}: {mensagem}")
    
    def warning(self, mensagem: str):
        now = datetime.now()
        print(f"{now.isoformat()} [{self.__YELLOW}WARNING{self.__RESET}] {self.__name}: {mensagem}")

    def info(self, mensagem: str):
        now = datetime.now()
        print(f"{now.isoformat()} [{self.__BLUE}INFO{self.__RESET}] {self.__name}: {mensagem}")
    
    