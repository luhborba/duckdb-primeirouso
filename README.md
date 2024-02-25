# Projeto de Geração e Tratamento de Dados

A ideia do projeto é gerar dados de acordo com o desejo do usuário, para que possamos simular uma situação real de utilização de dados, para tratamento usando diversas tecnologias e ferramentas.

## Stack Utilizada no Projeto

- Python
- Pandas
- Faker
- DuckDB
- Pyarrow
- Fastparquet
- TQDM
- Taskipy
- Polars
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
poetry run mkdocs serve
```

6. Gerando dados:
>Para gerar dados você pode acessar o arquivo gerar e definir os parametros que deseja, os parametros são: Quantidade de Linhas, Quantidade de Clientes e nome do arquivo (que por padrão é dados.csv, caso você mude deve mudar também nós arquivos de teste).

```bash
python gerar.py
```