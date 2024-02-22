import pandas as pd
import time
import os

# Registrando o tempo de início
inicio = time.time()

# Carregando dados
df = pd.read_csv('./dados.csv')

# Criando nova coluna de Valor Total
df['ValorTotal'] = df['ValorProduto'] * df['Quantidade']

# Verificando o total de vendas por produtos
total_vendas_produtos = df.groupby('Produto')['ValorTotal'].sum().reset_index()
total_vendas_produtos = total_vendas_produtos.rename(columns={'ValorTotal': 'TotalVendas'})
total_vendas_produtos = total_vendas_produtos.sort_values(by='TotalVendas', ascending=False)


# Verificando o total de vendas por clientes
total_vendas_cliente = df.groupby('Cliente')['ValorTotal'].sum().reset_index()
total_vendas_cliente = total_vendas_cliente.rename(columns={'ValorTotal': 'TotalVendas'})
total_vendas_cliente = total_vendas_cliente.sort_values(by='TotalVendas', ascending=False)

# Salvando DF em CSV
df.to_csv('data/csv/dados.csv', index=False)

# Salvando DF de Total De Vendas por Produto
total_vendas_produtos.to_csv('data/csv/total_vendas_produtos.csv', index=False)

# Salvando DF de Total De Vendas por Cliente
total_vendas_cliente.to_csv('data/csv/total_vendas_cliente.csv', index=False)

# Registrando o tempo de término
fim = time.time()

# Calculando o tempo de execução
tempo_execucao = fim - inicio

print(f"Tempo de execução: {tempo_execucao:.2f} segundos")