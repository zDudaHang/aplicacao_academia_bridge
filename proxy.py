from model.proxy.csv_reader import CsvReader
from model.proxy.proxy_service import ProxyService
from model.proxy.transacao_service import TransacaoService
from datetime import datetime

# Check if the script is being run as the main program
if __name__ == "__main__":
    reader = CsvReader()
    transacoes = reader.read()
    service = TransacaoService(transacoes)
    proxy = ProxyService(service)

    sair = False

    while sair == False:
        data_inicio = datetime.strptime(input("Escolha a data inicial:"), '%d/%m/%Y').date()
        data_fim = datetime.strptime(input("Escolha a data final:"), '%d/%m/%Y').date()
        print(proxy.relatorio(data_inicio=data_inicio, data_fim=data_fim))
        sair = input("Deseja sair? (S/N)") == "S"

