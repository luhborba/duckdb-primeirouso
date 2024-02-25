import duckdb
import time
import os

# Registrando o tempo de início
inicio = time.time()

# Conectando ao banco de dados DuckDB
con = duckdb.connect()

# Carregando dados
con.execute("CREATE TABLE dados AS SELECT * FROM read_csv('dados.csv');")

# Criando nova coluna de Valor Total
con.execute("ALTER TABLE dados ADD COLUMN ValorTotal DECIMAL(10,2)")
con.execute("UPDATE dados SET ValorTotal = ValorProduto * Quantidade")

# Salvando dados-duck.parquet
con.execute("COPY (SELECT * FROM dados) TO 'data/parquet/dados-duck.parquet' (FORMAT PARQUET)")

# Salvando total_vendas_produtos-duck.parquet
con.execute("COPY (SELECT Produto, SUM(ValorTotal) AS TotalVendas FROM dados GROUP BY Produto ORDER BY TotalVendas DESC) TO 'data/parquet/total_vendas_produtos-duck.parquet' (FORMAT PARQUET)")

# Salvando total_vendas_cliente-duck.parquet
con.execute("COPY (SELECT Cliente, SUM(ValorTotal) AS TotalVendas FROM dados GROUP BY Cliente ORDER BY TotalVendas DESC) TO 'data/parquet/total_vendas_cliente-duck.parquet' (FORMAT PARQUET)")

# Fechando a conexão com o banco de dados
con.close()

# Registrando o tempo de término
fim = time.time()

# Calculando o tempo de execução
tempo_execucao = fim - inicio

print(f"Tempo de execução: {tempo_execucao:.2f} segundos")
