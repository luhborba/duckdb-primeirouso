from gerador import gerando_dados, criar_pastas
import os

gerando_dados(10000000,20000, 'dados.csv')

# Obtém o diretório atual
diretorio_atual = os.getcwd()

# Cria as pastas
criar_pastas(diretorio_atual)