-- Criando tabela para agregar consultas
CREATE TABLE vendas AS SELECT * FROM read_csv_auto('./dados.csv');

-- Verificando existência da tabela
SHOW tables;


-- Criando Coluna Valor total
ALTER TABLE vendas
ADD COLUMN ValorTotal DECIMAL(10,2);

--Verificando
SELECT * FROM vendas
LIMIT 10;

-- Calculando ValorTotal
UPDATE vendas
SET ValorTotal = ValorProduto * Quantidade;

--Verificando
SELECT * FROM vendas
LIMIT 10;

-- Agregando Valor Total de Vendas por Produto
SELECT
    Produto, SUM(ValorTotal) as TotalVendas
FROM vendas
GROUP BY Produto
ORDER BY 2 DESC;

DROP TABLE vendas;