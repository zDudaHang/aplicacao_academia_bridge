
from model.factory.console_logger import ConsoleLogger
from model.factory.file_logger import FileLogger
from model.factory.logger import Logger
from model.factory.logger_enum import TipoLoggerEnum

class LoggerFactory:
    def get_logger(self, name: str, tipo: TipoLoggerEnum) -> Logger : 
        if tipo == TipoLoggerEnum.CONSOLE:
            return ConsoleLogger(name)
        elif tipo == TipoLoggerEnum.FILE:
            return FileLogger(name)
        else:
            raise ValueError("Tipo de logger não suportado")
    