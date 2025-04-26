import pandas as pd

"""
    As inconsistências que listei foram então:
    
    - SE transaction_type == "Deposito" ENTÃO account_origin == "Caixa Eletronico/Guiche" 
    - SE transaction_type == "Saque" ENTÃO account_destination == "Caixa Eletronico"
    - SE transaction_type == "Pagamento Imposto" ENTÃO account_destination == "Governo Federal - Impostos"
    - SE amount <= 0
    - SE currency != "BRL"
    - SE account_origin E account_destination E transaction_type NOT IN description
"""

# Lendo os arquivos. Pretendo iterar sobre a pasta dos arquivos, se for possível.
arquivo = r"arquivos\transacoes_faker_200.csv"
df = pd.read_csv(arquivo, sep=",", encoding="utf-8")

# Iterando sobre as linhas
for index, row in df.iterrows():

    # Vou instanciar uma variável para cada coluna
    id = row['transaction_id']
    account_origin = row['account_origin']
    account_destination = row['account_destination']
    valor = row['amount']
    currency = row['currency']
    transaction_type = row['transaction_type']
    description = row['description']

    # Verificando inconsistências
    if transaction_type == "Deposito" and account_origin != "Caixa Eletronico/Guiche":
        print(f"Id: {id}; Transação: {transaction_type}; Conta de origem: {account_origin}")
    
    if transaction_type == "Saque" and account_destination != "Caixa Eletronico":
        print(f"Id: {id}; Transação: {transaction_type}; Conta de destino: {account_destination}")

    if transaction_type == "Pagamento Imposto" and account_destination != "Governo Federal - Impostos":
        print(f"Id: {id}; Transação: {transaction_type}; Conta de destino: {account_destination}")
    
    if valor <= 0:
        print(f"Id: {id}; Transação: {transaction_type}; Valor: {valor}")

    if currency != "BRL":
        print(f"Id: {id}; Transação: {transaction_type}; Moeda: {currency}")

    if transaction_type not in description and account_origin not in description and account_destination not in description:
        print(f"Id: {id}; Transação: {transaction_type}; Conta de origem: {account_origin}; Conta de destino: {account_destination}; Descrição: {description}")

    if f"de '{account_origin}'" not in description:
        print(f"Id: {id}; Conta de origem: {account_origin}; Descrição: {description}")

    if f"para '{account_destination}'" not in description:
        print(f"Id: {id}; Conta de destino: {account_destination}; Descrição: {description}")

    campos = ['transaction_id', 'timestamp', 'account_origin', 'account_destination', 'amount', 'currency', 'transaction_type', 'location', 'description']
    nulos = [campo for campo in campos if pd.isna(row[campo])]
    if nulos:
        print(f"Id: {id}; Campos nulos: {nulos}")
     

