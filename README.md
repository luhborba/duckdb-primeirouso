# Projeto de Geração e Tratamento de Dados (Pandas vs DuckDB)

A ideia do projeto é gerar dados de acordo com o desejo do usuário, para que possamos simular uma situação real de utilização de dados, para tratamento comparando o desempenho do Pandas e DuckDB

## Regras de Negócio

Para esse projeto o Gestor solicitou que fosse extraido o resultado do total de vendas, como também total de vendas por produtos e por clientes. Para gerar arquivos nos formatos csv e parquet, destas informações para o time de DataViz poder criar incríveis e infaliveis dashboards.

## Resultado da Comparação

Ao utilizar o pandas para o tratamento de dados o mesmo desempenho todas o pipeline de dados em aproximadamente 1.008 segundos (Cerca de 16 minutos), exportando os dados tanto em csv, como também em parquet. Conforme imagem abaixo:

![Image](/docs/assets/img/pandas.png)

Ao utilizar o DuckDB, para realizar o mesmo pipeline de dados ele levou 584,83 segundos (Menos de 10 minutos). Conforme imagem abaixo:

![Imagem](/docs/assets/img/duckdb.png)

-- **O DuckDB teve uma perfomace 72% melhor do que o Pandas**

## Configuração do Computador Utilizado

- Processador: AMD Ryzen 3 5300U with Radeon Graphics 2.6 Ghz
- RAM: 8 GB DDR-4
- SSD Sata: 256 GB
- SO: Windows 11 23H2

## Stack Utilizada no Projeto

- Python
- Pandas
- Faker
- DuckDB
- Pyarrow
- Fastparquet
- TQDM
- Taskipy
- Mkdocs

## Clonando o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/luhborba/duckdb-primeirouso.git
cd duckdb-primeirouso
```

2. Configure a versão correta do Python com `pyenv`
```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

3. Ativando Poetry
```bash
poetry env use 3.12.1
poetry shell
```

4. Insatalando dependências
```bash
poetry install
```

5. Rodando a Documentação
```bash
poetry run task docs
```

6. Gerando dados:
>Para gerar dados você pode acessar o arquivo gerar e definir os parametros que deseja, os parametros são: Quantidade de Linhas, Quantidade de Clientes e nome do arquivo (que por padrão é dados.csv, caso você mude deve mudar também nós arquivos de teste).

```bash
poetry run task gerar
```

7. ETL com Pandas:
```bash
poetry run task pandas
```

8. ETL com DuckDB:
```bash
poetry run task pandas
```

9. Caso realize o ajuste no código use o código abaixo para refatorar segundo biblioteca `BLACK`:
```bash
poetry run task ajust_code
```


