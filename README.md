Desafio de Avaliação de Aptidão Técnica - InUp Contabilidade

Victor Augusto Gomes Costa - (32) 988201668

Foi me proposto então, que eu desenvolva um sistema capaz de analisar dados de extratos de transações financeiras, de forma que avalie a qualidade desses dados e, após isso, faça uma análise dos dados "filtrados".

A linguagem que eu mais domino hoje é o próprio Python. Por isso, escolhi ela para complementar esse teste.

1º Fase:
Primeiramente, me dediquei a analisar os arquivos enviados afim de entender o que desejamos validar, e o que vale a pena validar. 
Na coluna de data não encontrei nenhuma possíbilidade de validar. Até pensei em validar Horário Comercial / dia útil para Saques/Depósitos; mas existem diversos caixas 24hrs que já não faz mais sentido.
A conta de origem podemos validar para quando transaction_type for igual a Deposito ser sempre "Caixa Eletronico/Guiche".
Da mesma maneira, sempre que transaction_type for igual a Pagamento Impostos, account_destination será Governo Federal - Impostos.
A coluna amount não pode nunca ser um valor menor que zero.
Acho interessante apontar também sempre que a coluna currency for diferente de BRL.
A coluna description tem que ser, literalmente, a descrição da transação. Então, acho válido verificar se na descrição a transaction_type, account_origin e a account_destination estão presentes e no lugar certo. Não acho interessante validar a location na descrição, pois notei que é uma informação opcional nessa base de dados.
Já quando estava desenvolvendo, também identifique que sempre que transaction_type == "Saque" account_destination == "Caixa Eletrônico". Decide validar isso também.
Desenvolvendo, também decidi verificar se existe algum valor nulo.
Desenvolvendo, também identifiquei que Saque e Depósito não podem ser Online, e resolvi verificar também se existem transferências que utilizam a mesma conta como origem e destino.

Com essa análise dos dados, acredito que, após apontar as inconsistências encontradas, consigo fazer uma análise consistente e que retrate a realidade dos fatos.

2º Fase:
Já fiz a primeira análise dos dados, agora vou pensar em como quero desenvolver o projeto e o que eu quero que ele faça. A essa altura, já criei o repositório no github e já ativei uma venv para centralizar as importações.
Com o desenvolvimento, pretendo entregar um projeto que seja capaz de:
    - abrir e ler os arquivos '.csv' enviados;
    - iterar sobre cada linha do arquivo e verificar se ela não se encaixa em nenhuma das inconsistências identificadas (uma linha pode ser pega em mais de uma inconsistência);
    - montar, para cada arquivo, um arquivo com as inconsistências encontradas para que o usuário as análise;
    - se o usuário desejar, gerar um novo arquivo sem as inconsistências;
    - realizar a análise sumária dos dados remanescentes.

Vou usar a lib do pandas para desenvolver esse projeto.

3º Fase:
Depois de decidir o que fazer e como fazer, comecei a desenvolver de fato o projeto. 
Comecei lendo o arquivo, e já iterando sobre suas linhas. Depois parti para verificar as incosistências pensadas.
Até essa parte (2º commit) não encontrei nenhuma dificuldade. Já conhecia bastante o pandas e a lógica dos ifs. Apenas consultei a biblioteca do pandas (https://pandas.pydata.org/docs) e pedi ao chatgpt pra me ajudar a encontrar um jeito de verificar se os campos estão nulos e quais campos. O chat me deu a ideia de criar uma lista com os campos e iterar sobre a lista. Adaptei o código que ele me passou e deu super certo.
Depois de aplicar as verificações no código, voltei tratando algumas partes, como a leitura do arquivo, para deixar o código mais robusto, menos propicio a erro e mais escalonável.
Desenvolvi a lógica de criar o arquivo com as inconsistências. Pensei em criar uma lista que vai conter todas as inconsistências, e pra cada inconsistência eu crio uma outra lista que vai compor a maior, que mais tarde vai ser transformada em uma planilha. Aqui eu precisei de ajuda para pegar apenas o nome do arquivo, desconhecia o metodo basename, do os. Uma simples busca na web já me ajudou.

4º Fase:
Para analisar o arquivo, primeiro tenho que decidir quais as métricas que vou utilizar. São elas:
    - Total de transações por dia (quantidade e valor);
    - Total de transações por tipo (quantidade, valor e percentual);
    - Total de transações por localidade (quantidade e percentual);
    - Conta que mais/menos originou transações (filtro por quantidade, mostrando valor);
    - Conta que mais/menos recebeu transações (filtro por quantidade, mostrando valor);
    - Operações (combinação de conta origem e destino);
    - Operações (combinação de conta origem e tipo);
    - Operações (combinado de conta destino e tipo)

