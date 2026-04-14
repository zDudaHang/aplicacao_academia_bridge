from model.factory.logger_enum import TipoLoggerEnum
from model.factory.logger_factory import LoggerFactory

def main():
    factory = LoggerFactory()
    logger = factory.get_logger(name="Main", tipo=TipoLoggerEnum.CONSOLE)

    logger.log("Log")
    logger.danger("Perigo")
    logger.success("Sucesso")
    logger.warning("Cuidado")
    logger.info("Informativa")

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()