import csv
from faker import Faker
from random import randint

lista = [['Computador', 2000], ['Celular',1000], ['Monitor',700], ['Teclado', 50], ['Mouse',20], ['HeadSet',100]]
cliente = []
   

def gerando_dados(total_linhas: int, total_clientes: int, nome_arquivo: str):
    falso = Faker()
    data = []

    for _ in range(total_clientes):
        cliente.append(falso.name())


    for _ in range(total_linhas):
        produto = randint(0,5)

        data.append([
            cliente[randint(0,total_clientes-1)],
            falso.date(),
            lista[produto][0],
            lista[produto][1],
            falso.random_number(1,40)
        ])
    
    with open(nome_arquivo, 'w', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(['Cliente','Data_Compra','Produto','ValorProduto','Quantidade'])
        escrever.writerows(data)
