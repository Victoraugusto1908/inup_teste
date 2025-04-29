Desafio de Avaliação de Aptidão Técnica - InUp Contabilidade
Candidato: Victor Augusto Gomes Costa
Contato: (32) 98820-1668

Descrição do Desafio
Desenvolver um sistema capaz de:

Analisar dados de extratos de transações financeiras.

Avaliar a qualidade dos dados (identificar inconsistências).

Realizar uma análise sumária dos dados filtrados.

Tecnologia escolhida: Python (por ser a linguagem que mais domino atualmente).

Diário de Bordo
1ª Fase: Análise dos Dados
Iniciei o projeto analisando os arquivos enviados para entender quais validações seriam relevantes. Minhas conclusões:

Data: Não realizei validações. Pensei em validar dia e horária de saque/depósito, mas logo caiu por terra, pois saques/depósitos podem ocorrer em caixas 24h.

Conta de Origem/Destino:

transaction_type == "Depósito" → account_origin deve ser "Caixa Eletrônico/Guichê".

transaction_type == "Pagamento Impostos" → account_destination deve ser "Governo Federal - Impostos".

transaction_type == "Saque" → account_destination deve ser "Caixa Eletrônico".

Valor: A coluna amount nunca pode ser negativa.

Moeda: Apontar sempre que currency for diferente de BRL.

Descrição: Verificar se transaction_type, account_origin e account_destination estão presentes corretamente na description.

Campos Nulos: Validar se existem campos nulos.

Transações Online: Saques e depósitos não podem ser realizados online.

Transferências Internas: Verificar se existem transações com a mesma conta como origem e destino.

2ª Fase: Planejamento do Projeto
Defini o escopo do sistema:

Ler arquivos .csv.

Verificar inconsistências linha a linha (uma linha pode apresentar múltiplas inconsistências).

Gerar, para cada arquivo:

Um relatório de inconsistências.

Realizar uma análise sumária dos dados válidos, podendo ser com as inconsistências ou sem.

Biblioteca principal utilizada: pandas

3ª Fase: Desenvolvimento
Comecei implementando:

A leitura dos arquivos e a iteração sobre suas linhas.

As verificações de inconsistências conforme definido.

A geração do arquivo das inconsistências.

Observações durante o desenvolvimento:

Em resumo, não houve grandes dificuldades para verificar as inconsistências, nem gerar o arquivo. A lógica utilizada foi simples, apesar de muito funcional, e já tenho um conhecimento relevante na biblioteca pandas, então ler um arquivo e gerar outro não foi um problema.

Utilizei IA para pegar o nome do arquivo utilizado, não conhecia o método que usei aqui:

try:
    nome_arquivo = os.path.basename(arquivo).split('.')[0]

4ª Fase: Desenvolvimento da Análise de Dados
Métricas escolhidas para a análise sumária:

Total de transações por dia (quantidade e valor).

Total de transações por tipo (quantidade, valor e percentual).

Total de transações por localidade (quantidade e percentual).

Conta que mais/menos originou transações (quantidade e valor).

Conta que mais/menos recebeu transações (quantidade e valor).

Combinações:

Conta origem + conta destino.

Conta origem + tipo de transação.

Conta destino + tipo de transação.

Dificuldades enfrentadas:

Mesmo utilizando a documentação do pandas e IA, não consegui remover o warning do pandas ao transformar a coluna 'timestamp' em datetime. O código está 100% funcional, apesar desse aviso, funciona muito bem. Acredito que seja algo a ver com versão da lib.

Formatação de colunas de valores e percentuais, não conhecia os métodos, então recorri ao ChatGPT..

A separação da análise em funções específicas facilita a execução parcial e futura expansão.

Considerações Finais
Performance: Mesmo com arquivos de 1 milhão de linhas, o tempo de processamento não ultrapassou 6 minutos.

Escalabilidade: A estrutura do projeto facilita a adição de novas validações e análises.

Melhorias Futuras:

Permitir que o usuário selecione quais inconsistências deseja validar.

Possibilitar a exclusão seletiva de inconsistências por tipo ou linha específica.