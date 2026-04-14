

from model.observer.auditoria_service import AuditoriaService
from model.observer.estoque_service import EstoqueService
from model.observer.service import Service


def main():
    auditoria_service = AuditoriaService()
    estoque_service = EstoqueService()
    estoque_service.listar_estoque()
    service = Service(auditoria_service, estoque_service)

    sair = False

    while sair == False:
        item = input("Escolha o item: ")
        quantidade = int(input("Quantide que será alterada no estoque: "))
        service.alterar_estoque(item, quantidade)
        sair = input("Deseja sair? (S/N) ") == "S"


# Check if the script is being run as the main program
if __name__ == "__main__":
    main()