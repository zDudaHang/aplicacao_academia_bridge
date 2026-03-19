from datetime import datetime

from model.logger import Logger

class FileLogger(Logger):
    __name: str
    __filename: str = 'log.txt'

    def __init__(self, name: str):
        self.__name = name
        try:
            open(self.__filename, "x")
        except FileExistsError:
            print(f"O arquivo {self.__filename} já existe.")
            

    def log(self, mensagem: str):
        try:
            with open(self.__filename, "a") as file:
                now = datetime.now()
                file.write(f"{now.isoformat()} [LOG] {self.__name}: {mensagem}\n")
        except FileNotFoundError:
            print(f"Não foi possível encontrar o arquivo {self.__filename}")

    def danger(self, mensagem: str):
        try:
            with open(self.__filename, "a") as file:
                now = datetime.now()
                file.write(f"{now.isoformat()} [DANGER] {self.__name}: {mensagem}\n")
        except FileNotFoundError:
            print(f"Não foi possível encontrar o arquivo {self.__filename}")

    def success(self, mensagem: str):
        try:
            with open(self.__filename, "a") as file:
                now = datetime.now()
                file.write(f"{now.isoformat()} [SUCCESS] {self.__name}: {mensagem}\n")
        except FileNotFoundError:
            print(f"Não foi possível encontrar o arquivo {self.__filename}")
    
    def warning(self, mensagem: str):
        try:
            with open(self.__filename, "a") as file:
                now = datetime.now()
                file.write(f"{now.isoformat()} [WARNING] {self.__name}: {mensagem}\n")
        except FileNotFoundError:
            print(f"Não foi possível encontrar o arquivo {self.__filename}")

    def info(self, mensagem: str):
        try:
            with open(self.__filename, "a") as file:
                now = datetime.now()
                file.write(f"{now.isoformat()} [INFO] {self.__name}: {mensagem}\n")
        except FileNotFoundError:
            print(f"Não foi possível encontrar o arquivo {self.__filename}")

