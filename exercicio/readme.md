#Cadastro e Consulta de Imóveis

##Este programa tem como objetivo criar uma aplicação para cadastrar e consultar imóveis. A aplicação é escrita em Python, utilizando a biblioteca Tkinter para a interface gráfica do usuário e SQLite para o gerenciamento do banco de dados.

#Funcionalidades
- Cadastro de imóveis com as seguintes informações:
- Tipo de negociação (Venda, Locação, Venda/Locação)
-Status do imóvel (Disponível, Locado, Vendido, À liberar)
- Endereço do imóvel
- Tipo do imóvel (Apartamento, Casa, Terreno)
- Características do imóvel
- Preço do imóvel
- Condições do imóvel
- Observações sobre o imóvel

#Pré-requisitos
- Python 3.x (recomendável a versão mais recente)
- Tkinter (geralmente vem pré-instalado com o Python)

#Como executar
##Para executar a aplicação:

1. Clone o repositório ou baixe o projeto em seu computador.

2. Navegue até a pasta onde estão os arquivos database.py, functions.py e gui.py (ou main.py).

3. Execute o arquivo gui.py (ou main.py) com o comando:

*python gui.py*

Ou, se você estiver usando uma versão específica do Python:

*python3 gui.py*

Ao executar o programa, a interface gráfica da aplicação de cadastro de imóveis será exibida. Preencha os campos com as informações do imóvel e clique em "Cadastrar" para salvar os dados no banco de dados. Você também pode clicar em "Limpar" para limpar o formulário.

#Estrutura do projeto
##O projeto é dividido nos seguintes arquivos:

- database.py: Responsável pela conexão ao banco de dados SQLite e criação da tabela "imoveis".
- functions.py: Contém as funções auxiliares para inserir dados no banco de dados e limpar o formulário.
- gui.py (ou main.py): Contém a interface gráfica da aplicação usando Tkinter.