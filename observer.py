

from model.observer.auditoria_service import AuditoriaService
from model.observer.email_service import EmailService
from model.observer.estoque_publisher import EstoquePublisher
from model.observer.estoque_service import EstoqueService
from model.observer.fornecedor_service import FornecedorService
from model.observer.service import Service


def main():
    auditoria_service = AuditoriaService()
    estoque_service = EstoqueService()
    email_service = EmailService()
    fornecedor_service = FornecedorService()

    publisher = EstoquePublisher()
    publisher.subscribe(auditoria_service)
    publisher.subscribe(estoque_service)
    publisher.subscribe(email_service)
    publisher.subscribe(fornecedor_service)

    service = Service(publisher)

    sair = False

    while sair == False:
        item = input("\nEscolha o item: ")
        quantidade = int(input("Quantide que será alterada no estoque: "))
        service.alterar_estoque(item, quantidade)
        sair = input("Deseja sair? (S/N) ") == "S"


# Check if the script is being run as the main program
if __name__ == "__main__":
    main()