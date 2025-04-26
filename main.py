import pandas as pd
from time import sleep
import os

"""
    As inconsistências que listei foram então:
    
    - SE transaction_type == "Deposito" ENTÃO account_origin == "Caixa Eletronico/Guiche" 
    - SE transaction_type == "Saque" ENTÃO account_destination == "Caixa Eletronico"
    - SE transaction_type == "Pagamento Imposto" ENTÃO account_destination == "Governo Federal - Impostos"
    - SE amount <= 0
    - SE currency != "BRL"
    - SE account_origin E account_destination E transaction_type NOT IN description
"""

# Lendo os arquivos.
while True:
    try:
        arquivo = str(input("Digite o caminho do arquivo: "))
        df = pd.read_csv(arquivo, sep=",", encoding="utf-8")
        break
    except FileNotFoundError:
        print("Arquivo não encontrado. Tente novamente.")
        sleep(1)
    except Exception as e:
        print(f"Erro inesperado: {e}. Tente novamente.")
        sleep(1)

print(f'Arquivo "{arquivo}" lido com sucesso!')

# Verificando se o arquivo está no formato correto
try:
    colunas = df.columns.tolist()
    if colunas != ['transaction_id', 'timestamp', 'account_origin', 'account_destination', 'amount', 'currency', 'transaction_type', 'location', 'description']:
        raise ValueError(f"As colunas do arquivo {arquivo} não estão corretas. Verifique.")
    
    else:
        # Criando uma lista para armazenar as inconsistências
        inconsistencias_list = []

        # Iterando sobre as linhas
        for index, row in df.iterrows():

            try:
                # Vou instanciar uma variável para cada coluna
                id = row['transaction_id']
                account_origin = row['account_origin']
                account_destination = row['account_destination']
                valor = row['amount']
                currency = row['currency']
                transaction_type = row['transaction_type']
                description = row['description']

                # Verificando se há campos nulos
                campos = ['transaction_id', 'timestamp', 'account_origin', 'account_destination', 'amount', 'currency', 'transaction_type', 'location', 'description']
                nulos = [campo for campo in campos if pd.isna(row[campo])]
                if nulos:
                    print(f"Id: {id}; Campos nulos: {nulos}")
                    inconsistencia = [id, "Há valores nulos na linha. Verifique", nulos]
                    inconsistencias_list.append(inconsistencia)

                # Verificando inconsistências
                if transaction_type == "Deposito" and account_origin != "Caixa Eletronico/Guiche":
                    print(f"Id: {id}; Transação: {transaction_type}; Conta de origem: {account_origin}")
                    inconsistencia = [id, "Transação Deposito com conta de origem diferente de 'Caixa Eletronico/Guiche'.", account_origin]
                    inconsistencias_list.append(inconsistencia)
                
                if transaction_type == "Saque" and account_destination != "Caixa Eletronico":
                    print(f"Id: {id}; Transação: {transaction_type}; Conta de destino: {account_destination}")
                    inconsistencia = [id, "Transação Saque com conta de destino diferente de 'Caixa Eletronico'.", account_destination]
                    inconsistencias_list.append(inconsistencia)

                if transaction_type == "Pagamento Imposto" and account_destination != "Governo Federal - Impostos":
                    print(f"Id: {id}; Transação: {transaction_type}; Conta de destino: {account_destination}")
                    inconsistencia = [id, "Transação Pagamento Imposto com conta de destino diferente de 'Governo Federal - Impostos'.", account_destination]
                    inconsistencias_list.append(inconsistencia)
                
                if valor <= 0:
                    print(f"Id: {id}; Transação: {transaction_type}; Valor: {valor}")
                    inconsistencia = [id, "Valor menor ou igual a zero.", f"Valor: {valor} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if currency != "BRL":
                    print(f"Id: {id}; Transação: {transaction_type}; Moeda: {currency}")
                    inconsistencia = [id, "Moeda diferente de 'BRL'.", f"Moeda: {currency} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if transaction_type not in description and account_origin not in description and account_destination not in description:
                    print(f"Id: {id}; Transação: {transaction_type}; Conta de origem: {account_origin}; Conta de destino: {account_destination}; Descrição: {description}")
                    inconsistencia = [id, "Descrição da transação não condiz com os dados da transação. Verifique.", f"Transação: {transaction_type} - Conta de origem: {account_origin} - Conta de destino: {account_destination} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if f"de '{account_origin}'" not in description:
                    print(f"Id: {id}; Conta de origem: {account_origin}; Descrição: {description}")
                    inconsistencia = [id, "Descrição da transação não condiz com os dados da transação. Verifique.", f"Transação: {transaction_type} - Conta de origem: {account_origin} - Conta de destino: {account_destination} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if f"para '{account_destination}'" not in description:
                    print(f"Id: {id}; Conta de destino: {account_destination}; Descrição: {description}")
                    inconsistencia = [id, "Descrição da transação não condiz com os dados da transação. Verifique.", f"Transação: {transaction_type} - Conta de origem: {account_origin} - Conta de destino: {account_destination} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

            except Exception as e:
                print(f"Erro ao processar a linha {index}: {e}.")
                print("Parando o processamento.")
                break
        
        # Criando um arquivo para as inconsistências
        try:
            if not inconsistencias_list:
                print(f"Nenhuma inconsistência encontrada no arquivo {arquivo}.")
            else:
                print(f"Total de inconsistências encontradas: {len(inconsistencias_list)}.")
                print("Criando arquivo de inconsistências...")
                inconsistencias_df = pd.DataFrame(inconsistencias_list, columns=['transaction_id', 'Tipo Inconsistência', 'Identificadores'])
                try:
                    nome_arquivo = os.path.basename(arquivo).split('.')[0]
                except Exception as e:
                    print(f"Erro ao criar o nome do arquivo: {e}. Usando 'inconsistencias' como padrão.")
                    nome_arquivo = 'inconsistencias'
                inconsistencias_df.to_excel(f'{nome_arquivo}.xlsx', index=False)
                print("Arquivo de inconsistências criado com sucesso!")

        except Exception as e:
            print(f"Erro ao criar o arquivo de inconsistências: {e}.")

except Exception as e:
    print(f"Erro ao verificar as colunas do arquivo: {e}. Tente com outro arquivo.")

