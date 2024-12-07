# Cadastro e Consulta de Imóveis

## Visão Geral

Este programa é uma aplicação de cadastro e consulta de imóveis desenvolvida em **Python**, utilizando a biblioteca **Tkinter** para a interface gráfica e **SQLite** para o gerenciamento de banco de dados. A aplicação permite o armazenamento, consulta e gerenciamento de informações sobre imóveis de forma intuitiva e eficiente.

## Funcionalidades

- **Cadastro de Imóveis:**
  - Tipo de negociação: Venda, Locação, Venda/Locação.
  - Status do imóvel: Disponível, Locado, Vendido, À liberar.
  - Endereço do imóvel.
  - Tipo do imóvel: Apartamento, Casa, Terreno.
  - Características do imóvel.
  - Preço do imóvel.
  - Condições do imóvel.
  - Observações adicionais.

- **Interface Intuitiva:**
  - Formulário para entrada de dados.
  - Botão **Cadastrar** para salvar as informações.
  - Botão **Limpar** para limpar o formulário.

- **Banco de Dados:**
  - Conexão com o SQLite.
  - Persistência de dados para consulta posterior.

## Pré-requisitos

- **Python 3.x** (Recomenda-se a versão mais recente)
- **Tkinter** (Geralmente incluído na instalação do Python)

## Como Executar

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/cadastro-imoveis.git
   ```

2. **Navegue até o Diretório do Projeto:**

   ```bash
   cd cadastro-imoveis
   ```

3. **Execute a Aplicação:**

   Utilize o seguinte comando para iniciar o programa:

   ```bash
   python gui.py
   ```

   Ou, caso utilize uma versão específica do Python:

   ```bash
   python3 gui.py
   ```

4. **Utilize a Interface Gráfica:**
   - Preencha os campos necessários.
   - Clique em **Cadastrar** para salvar os dados no banco de dados.
   - Use o botão **Limpar** para apagar os dados do formulário.

## Estrutura do Projeto

O projeto é modular e organizado em três principais arquivos:

- **`database.py`:** Responsável pela conexão com o SQLite e criação da tabela `imoveis`.
- **`functions.py`:** Contém funções auxiliares, como inserção de dados no banco e limpeza do formulário.
- **`gui.py` (ou `main.py`):** Gerencia a interface gráfica e as interações com o usuário usando Tkinter.

## Testando o Código

1. Certifique-se de que o Python está instalado no seu computador.
2. Copie o código ou utilize o repositório para garantir que todos os arquivos necessários estejam presentes.
3. Execute o programa conforme descrito em **Como Executar**.

Caso esteja utilizando **Linux** ou **macOS** e o comando `python` esteja vinculado ao Python 2, substitua por `python3`:

```bash
python3 gui.py
```

Se o programa rodar corretamente, uma janela com os campos e botões será exibida. Você poderá cadastrar e gerenciar imóveis diretamente por essa interface.

## Possíveis Problemas

Caso encontre algum erro durante a execução, por favor:
- Verifique se todas as dependências estão instaladas.
- Confirme que o Python 3.x está configurado corretamente.
- Compartilhe o erro para suporte adicional.

---

*Organize e gerencie informações de imóveis com facilidade usando esta aplicação simples e eficiente!*
