import pandas as pd
from time import sleep
import os


class analise():
    """
        - Total de transações por dia (quantidade e valor);
        - Total de transações por tipo (quantidade, valor e percentual);
        - Total de transações por localidade (quantidade e percentual);
        - Conta que mais/menos originou transações (filtro por quantidade, mostrando valor);
        - Conta que mais/menos recebeu transações (filtro por quantidade, mostrando valor);
        - Operações (combinação de conta origem e destino);
        - Operações (combinação de conta origem e tipo);
        - Operações (combinado de conta destino e tipo)
    """

    # Total de transações por dia (quantidade e valor)
    def transaction_for_day(df):
        try:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors="coerce")
            # Total de transações por dia (quantidade e valor)
            resultado = df.groupby(df['timestamp'].dt.to_period('D')).agg(
                transacoes = ('transaction_id', 'count'),
                valor_total = ('amount', 'sum'),
                media = ('amount', 'mean')
            ).reset_index()

            resultado['valor_total'] = resultado['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            resultado['media'] = resultado['media'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            result = resultado.sort_values('timestamp')
            return result
        
        except Exception as e:
            print(f"Não foi possível analisar as transações diárias: {e}")

    # Total de transações por tipo (quantidade, valor e percentual)
    def transaction_for_type(df):
        try:
            resultado = df.groupby(df['transaction_type']).agg(
                transacoes = ('transaction_id', 'count'),
                valor_total = ('amount', 'sum'),
                media = ("amount", 'mean')
            ).reset_index()

            resultado['porcentagem'] = (resultado['transacoes'] / resultado['transacoes'].sum()) * 100
            resultado['porcentagem'] = resultado['porcentagem'].apply(lambda x: f"{x:.2f}%")
            resultado['valor_total'] = resultado['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            resultado['media'] = resultado['media'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            result = resultado.sort_values('transacoes')
            return result

        except Exception as e:
            print(f"Não foi possível analisar as transações por tipo: {e}")

    # Total de transações por localidade (quantidade e percentual)
    def transaction_for_location(df):
        try:
            resultado = df.groupby(df['location']).agg(
                transacoes = ('transaction_id', 'count'),
                valor_total = ('amount', 'sum'),
                media = ('amount', 'mean')
            ).reset_index()

            resultado['porcentagem'] = (resultado['transacoes'] / resultado['transacoes'].sum()) * 100
            resultado['porcentagem'] = resultado['porcentagem'].apply(lambda x: f"{x:.2f}%")
            resultado['valor_total'] = resultado['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            resultado['media'] = resultado['media'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            result = resultado.sort_values('transacoes')
            return result

        except Exception as e:
            print(f"Não foi possível analisar as transações por local: {e}")

    # Conta que mais/menos originou transações (filtro por quantidade, mostrando valor)
    def transaction_for_origin(df):
        try:
            resultado = df.groupby(df['account_origin']).agg(
                transacoes = ('transaction_id', 'count'),
                valor_total = ('amount', 'sum'),
                media = ('amount', 'mean')
            ).reset_index()

            resultado['valor_total'] = resultado['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            resultado['media'] = resultado['media'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            result = resultado.sort_values('transacoes')
            return result

        except Exception as e:
            print(f"Não foi possível analisar as transações por conta de origem: {e}")

    # Conta que mais/menos recebeu transações (filtro por quantidade, mostrando valor) 
    def transaction_for_destination(df):
        try:
            resultado = df.groupby(df['account_destination']).agg(
                transacoes = ('transaction_id', 'count'),
                valor_total = ('amount', 'sum'),
                media = ('amount', 'mean')
            ).reset_index()

            resultado['valor_total'] = resultado['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            resultado['media'] = resultado['media'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            result = resultado.sort_values('transacoes')
            return result

        except Exception as e:
            print(f"Não foi possível analisar as transações por conta de destino: {e}")

    # Operações (combinação de conta origem e destino)
    def combination_origin_destination(df):
        try:
            resultado = df.groupby([df['account_origin'], df['account_destination']]).agg(
                transacoes = ('transaction_id', 'count'),
                valor_total = ('amount', 'sum'),
                media = ('amount', 'mean')
            ).reset_index()

            resultado['valor_total'] = resultado['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            resultado['media'] = resultado['media'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            result = resultado.sort_values('transacoes')
            return result

        except Exception as e:
            print(f"Não foi possível analisar as transações por combinação de conta de origem e destino: {e}")

    # Operações (combinação de conta origem e tipo)
    def combination_origin_type(df):
        try:
            resultado = df.groupby([df['account_origin'], df['transaction_type']]).agg(
                transacoes = ('transaction_id', 'count'),
                valor_total = ('amount', 'sum'),
                media = ('amount', 'mean')
            ).reset_index()

            resultado['valor_total'] = resultado['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            resultado['media'] = resultado['media'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            result = resultado.sort_values('transacoes')
            return result

        except Exception as e:
            print(f"Não foi possível analisar as transações por combinação de conta de origem e tipo: {e}")

    # Operações (combinado de conta destino e tipo)
    def combination_destination_type(df):
        try:
            resultado = df.groupby([df['account_destination'], df['transaction_type']]).agg(
                transacoes = ('transaction_id', 'count'),
                valor_total = ('amount', 'sum'),
                media = ('amount', 'mean')
            ).reset_index()

            resultado['valor_total'] = resultado['valor_total'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            resultado['media'] = resultado['media'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            result = resultado.sort_values('transacoes')
            return result

        except Exception as e:
            print(f"Não foi possível analisar as transações por combinação de conta de destino e tipo: {e}")

"""
    As inconsistências que listei foram então:
    
    - Verificar se tem algum valor NULL na linha analisado
    - SE transaction_type == "Deposito" ENTÃO account_origin == "Caixa Eletronico/Guiche" 
    - SE transaction_type == "Saque" ENTÃO account_destination == "Caixa Eletronico"
    - SE transaction_type == "Pagamento Imposto" ENTÃO account_destination == "Governo Federal - Impostos"
    - SE location == "Online" E transaction_type == "Saque" OU "Deposito"
    - SE amount <= 0
    - SE currency != "BRL"
    - SE account_origin E account_destination E transaction_type NOT IN description
    - SE account_origin == account_destination
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
        print("Verificando se há inconsistências. Aguarde, esse processo pode demorar um pouco...")
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
                location = row["location"]
                description = row['description']

                # Verificando se há campos nulos
                campos = ['transaction_id', 'timestamp', 'account_origin', 'account_destination', 'amount', 'currency', 'transaction_type', 'location', 'description']
                nulos = [campo for campo in campos if pd.isna(row[campo])]
                if nulos:
                    inconsistencia = [id, "Há valores nulos na linha. Verifique", nulos]
                    inconsistencias_list.append(inconsistencia)

                # Verificando inconsistências
                if transaction_type == "Deposito" and account_origin != "Caixa Eletronico/Guiche":
                    inconsistencia = [id, "Transação Deposito com conta de origem diferente de 'Caixa Eletronico/Guiche'.", account_origin]
                    inconsistencias_list.append(inconsistencia)
                
                if transaction_type == "Saque" and account_destination != "Caixa Eletronico":
                    inconsistencia = [id, "Transação Saque com conta de destino diferente de 'Caixa Eletronico'.", account_destination]
                    inconsistencias_list.append(inconsistencia)

                if transaction_type == "Pagamento Imposto" and account_destination != "Governo Federal - Impostos":
                    inconsistencia = [id, "Transação Pagamento Imposto com conta de destino diferente de 'Governo Federal - Impostos'.", account_destination]
                    inconsistencias_list.append(inconsistencia)

                if location == "Online" and transaction_type in ("Deposito", "Saque"):
                    inconsistencia = [id, "Saque/Deposito feito de forma online, verificar.", f"Transação: {transaction_type} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)
                
                if valor <= 0:
                    inconsistencia = [id, "Valor menor ou igual a zero.", f"Valor: {valor} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if currency != "BRL":
                    inconsistencia = [id, "Moeda diferente de 'BRL'.", f"Moeda: {currency} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if account_destination == account_origin:
                    inconsistencia = [id, "Conta de Destino igual a conta de Origem, verifique.", f"Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if transaction_type not in description and account_origin not in description and account_destination not in description:
                    inconsistencia = [id, "Descrição da transação não condiz com os dados da transação. Verifique.", f"Transação: {transaction_type} - Conta de origem: {account_origin} - Conta de destino: {account_destination} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if f"de '{account_origin}'" not in description:
                    inconsistencia = [id, "Descrição da transação não condiz com os dados da transação. Verifique.", f"Transação: {transaction_type} - Conta de origem: {account_origin} - Conta de destino: {account_destination} - Descrição: {description}"]
                    inconsistencias_list.append(inconsistencia)

                if f"para '{account_destination}'" not in description:
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
                inconsistencias_df.to_excel(f'inconsistencias_{nome_arquivo}.xlsx', index=False)
                print("Arquivo de inconsistências criado com sucesso! Favor verificar as inconsistências encontradas.")
                sleep(2)

                # validando se o usuário deseja remover as inconsistências do arquivo original
                while True:
                    try:
                        booleano = int(input("Deseja remover as incosistências do arquivo original ? Responda com 1 para 'Sim' e 0 para 'Não': "))
                        if booleano == 1:
                            print("Retirando inconsistências do arquivo original...")
                            ids = inconsistencias_df['transaction_id'].tolist()
                            # filtrando o df com os ids das inconsistências
                            df_filtrado = df[~df['transaction_id'].isin(ids)]
                            break
                        elif booleano == 0:
                            print("Faremos então a análise considerando as inconsistências....")
                            df_filtrado = df
                            break
                        else:
                            print("Essa não é uma resposta válida, tente novamente.")
                    except Exception:
                        print("Essa não é uma resposta válida, tente novamente.")
                
                # Fazendo a análise do arquivo
                print("Analisando arquivo. Aguarde, esse processo pode demorar...")
                transaction_day = analise.transaction_for_day(df_filtrado)
                transaction_type = analise.transaction_for_type(df_filtrado)
                transaction_location = analise.transaction_for_location(df_filtrado)
                print("Aguarde mais um pouco, estamos terminando...")
                transaction_origin = analise.transaction_for_origin(df_filtrado)
                transaction_destinate = analise.transaction_for_destination(df_filtrado)
                print("Apenas mais alguns instantes...")
                combination = analise.combination_origin_destination(df_filtrado)
                combination_origin = analise.combination_origin_type(df_filtrado)
                combination_destination = analise.combination_destination_type(df_filtrado)
                print("Análise finalizada! Criando arquivo com a análise...")

                # Exportando o arquivo da análise
                try:
                    with pd.ExcelWriter(f"analise_{nome_arquivo}.xlsx", engine='xlsxwriter') as writer:
                        transaction_day.to_excel(writer, sheet_name="Trans. dia", index=False)
                        transaction_type.to_excel(writer, sheet_name="Trans. tipo", index=False)
                        transaction_location.to_excel(writer, sheet_name="Trans. local", index=False)
                        transaction_origin.to_excel(writer, sheet_name="Trans. origem", index=False)
                        transaction_destinate.to_excel(writer, sheet_name="Trans. destino", index=False)
                        combination.to_excel(writer, sheet_name="Combinação origem-destino", index=False)
                        combination_origin.to_excel(writer, sheet_name="Combinação origem-tipo", index=False)
                        combination_destination.to_excel(writer, sheet_name="Combinação destino-tipo", index=False)

                        print("Arquivo com a análise criado.")
                        print("Encerrando programa...")
                except Exception as e:
                    print(f"Não foi possível criar o arquivo com a análise feita: {e}")

        except Exception as e:
            print(f"Erro ao criar o arquivo de inconsistências: {e}.")

except Exception as e:
    print(f"Erro ao verificar as colunas do arquivo: {e}. Tente com outro arquivo.")
