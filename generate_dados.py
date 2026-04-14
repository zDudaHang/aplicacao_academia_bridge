import csv
import random
from datetime import date, timedelta

def random_date():
    start_of_year = date(2025, 1, 1)
    return start_of_year + timedelta(days=random.randint(0, 364))

def random_instituicao():
    instituicoes = ['Pôneibank', 'Pôneinter', 'Pôneicaixa', 'Joãozinho LTDA']
    return random.choice(instituicoes)

def export_csv(quantidade_dados: int):
    with open('dados.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,  fieldnames=['DATA DA TRANSAÇÃO', 'VALOR', 'INSTITUIÇÃO'])
        writer.writeheader()
        for i in range(quantidade_dados):
            data_transacao = random_date()
            valor = random.randint(-10000, 10000)
            instituicao = random_instituicao()
            writer.writerow({ 
                'DATA DA TRANSAÇÃO': data_transacao, 
                'VALOR': valor, 
                'INSTITUIÇÃO': instituicao
            })
            print(f"{i} de {quantidade_dados}")


# Check if the script is being run as the main program
if __name__ == "__main__":    
    quantidade_dados = int(input("Quantidade de dados que precisam ser gerados:"))
    export_csv(quantidade_dados)




