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
A coluna location penso em validar também o transaction_type "boleto", já que não da pra fazer um boleto online.
A coluna description tem que ser, literalmente, a descrição da transação. Então, acho válido verificar se na descrição a transaction_type, account_origin e a account_destination estão presentes e no lugar certo. Não acho interessante validar a location na descrição, pois notei que é uma informação opcional nessa base de dados.

Com essa análise dos dados, acredito que, após apontar as inconsistências encontradas, consigo fazer uma análise consistente e que retrate a realidade dos fatos.

2º Fase:
Já fiz a primeira análise dos dados, agora vou começar a desenvolver essas validações. A essa altura, já criei o repositório no github e já ativei uma venv para centralizar as importações.
Com o desenvolvimento, pretendo entregar um projeto que seja capaz:
    - abrir e ler os arquivos '.csv' enviados;
    - iterar sobre cada linha do arquivo e verificar se ela não se encaixa em nenhuma das inconsistências identificadas (uma linha pode ser pega em mais de uma inconsistência);
    - montar, para cada arquivo, um arquivo com as inconsistências encontradas para que o usuário as análise;
    - se o usuário desejar, gerar um novo arquivo sem as inconsistências;
    - realizar a análise sumária dos dados remanescentes.
