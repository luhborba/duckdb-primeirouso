import csv
from faker import Faker
from random import randint


lista = [['Computador', 2000], ['Celular Xiaomi',1000], ['Celular Samsung',1500], ['Celular Iphone', 5000], ['Monitor',700], ['Teclado', 50], ['Mouse',20],['HeadSet',100],
          ['HeadSet JBL', 250],['HeadSet',100],['Carregador Iphone', 105],['Carregador Samsung', 80],
          ['Carregador Xiaomi', 90],['Carregador Motorola', 100],['Carregador Nokia', 110],['PenDrive 4 GB', 20],['PenDrive 8 GB', 30],['PenDrive 16 GB', 40]]
cliente = []
   

def gerando_dados(total_linhas: int, total_clientes: int, nome_arquivo: str):
    falso = Faker()
    data = []
    print("Iniciando Geração de Dados")

    for _ in range(total_clientes):
        cliente.append(falso.name())


    for _ in range(total_linhas):
        produto = randint(0,17)

        data.append([
            cliente[randint(0,total_clientes-1)],
            falso.date(),
            lista[produto][0],
            lista[produto][1],
            falso.random_number(1,10)
        ])
    
    with open(nome_arquivo, 'w', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(['Cliente','Data_Compra','Produto','ValorProduto','Quantidade'])
        escrever.writerows(data)


    print("Dados gerados com sucesso!")
