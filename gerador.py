import csv
import os
from random import choice

from faker import Faker
from tqdm import tqdm

lista_produtos = {
    "Computador": 2000,
    "Celular Xiaomi": 1000,
    "Celular Samsung": 1500,
    "Celular Iphone": 5000,
    "Monitor": 700,
    "Teclado": 50,
    "Mouse": 20,
    "HeadSet": 100,
    "HeadSet JBL": 250,
    "Carregador Iphone": 105,
    "Carregador Samsung": 80,
    "Carregador Xiaomi": 90,
    "Carregador Motorola": 100,
    "Carregador Nokia": 110,
    "PenDrive 4 GB": 20,
    "PenDrive 8 GB": 30,
    "PenDrive 16 GB": 40,
}
cliente = []


def gerando_dados(
    total_linhas: int, total_clientes: int, nome_arquivo: str, tamanho_bloco: int = 100
):
    falso = Faker()

    with open(nome_arquivo, "w", newline="") as file:
        escrever = csv.writer(file)
        escrever.writerow(
            ["Cliente", "Data_Compra", "Produto", "ValorProduto", "Quantidade"]
        )

        for _ in range(total_clientes):
            cliente.append(falso.name())

        data = []
        for i in tqdm(range(total_linhas), desc="Progresso", unit="linha"):
            produto = choice(list(lista_produtos.keys()))
            data.append(
                [
                    choice(cliente),
                    falso.date(),
                    produto,
                    lista_produtos[produto],
                    falso.random_number(1, 10),
                ]
            )

            if i % tamanho_bloco == tamanho_bloco - 1:
                escrever.writerows(data)
                data = []

        if data:
            escrever.writerows(data)

    print("Dados gerados com sucesso!")


def criar_pastas(diretorio_atual):
    """
    Cria a estrutura de pastas 'data/csv/' e 'data/parquet/' na pasta atual.

    Args:
      diretorio_atual: Caminho da pasta atual.
    """

    pastas = ["data/csv/", "data/parquet/"]

    for pasta in pastas:
        diretorio_completo = os.path.join(diretorio_atual, pasta)

        # Verifica se o diretório existe
        if not os.path.exists(diretorio_completo):
            # Cria o diretório
            os.makedirs(diretorio_completo)
            print(f"Diretório '{diretorio_completo}' criado com sucesso!")
