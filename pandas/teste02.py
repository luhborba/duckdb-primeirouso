import pandas as pd

df = pd.read_csv('./dados.csv')

df['ValorTotal'] = df['ValorProduto'] * df['Quantidade']

print(df.groupby('Produto')['ValorTotal'].sum())