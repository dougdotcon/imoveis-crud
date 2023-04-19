import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('imoveis.db')

c = conn.cursor()

# Criar tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS imoveis (
                id INTEGER PRIMARY KEY,
                tipo_negociacao TEXT NOT NULL,
                status TEXT NOT NULL,
                endereco TEXT NOT NULL,
                tipo_imovel TEXT NOT NULL,
                caracteristicas TEXT NOT NULL,
                preco REAL,
                condicoes TEXT,
                observacoes TEXT
            )''')

conn.commit()

def inserir_dados():
    # Inserir imóvel no banco de dados
    if (cb_tipo_negociacao.get() == '' or
        cb_status.get() == '' or
        txt_endereco.get('1.0', 'end-1c') == '' or
        cb_tipo_imovel.get() == '' or
        txt_caracteristicas.get('1.0', 'end-1c') == ''
        ):
        messagebox.showerror('Erro', 'Todos os campos são obrigatórios.')
        return

    dados = (cb_tipo_negociacao.get(),
             cb_status.get(),
             txt_endereco.get('1.0', 'end-1c'),
             cb_tipo_imovel.get(),
             txt_caracteristicas.get('1.0', 'end-1c'),
             txt_preco.get('1.0', 'end-1c'),
             txt_condicoes.get('1.0', 'end-1c'),
             txt_observacoes.get('1.0', 'end-1c')
             )

    c.execute('''INSERT INTO imoveis (tipo_negociacao, status, endereco,
                                      tipo_imovel, caracteristicas, preco,
                                      condicoes, observacoes)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', dados)

    conn.commit()

    # Exibe mensagem de sucesso e limpa formulário
    messagebox.showinfo('Sucesso', 'Imóvel cadastrado com sucesso!')
    limpar_formulario()


def limpar_formulario():
    cb_tipo_negociacao.set('')
    cb_status.set('')
    txt_endereco.delete('1.0', 'end')
    cb_tipo_imovel.set('')
    txt_caracteristicas.delete('1.0', 'end')
    txt_preco.delete('1.0', 'end')
    txt_condicoes.delete('1.0', 'end')
    txt_observacoes.delete('1.0', 'end')

# Criar janela principal
janela = tk.Tk()
janela.title('Cadastro/Consulta de Imóveis')

# Tipo de negociação
lbl_tipo_negociacao = tk.Label(janela, text='Tipo de negociação:')
lbl_tipo_negociacao.grid(row=0, column=0, sticky='e')
cb_tipo_negociacao = tk.StringVar(janela)
opcoes_cb_tipo_negociacao = ('Venda', 'Locação', 'Venda/Locação')
menu_tipo_negociacao = tk.OptionMenu(janela, cb_tipo_negociacao, *opcoes_cb_tipo_negociacao)
menu_tipo_negociacao.config(width=10)
menu_tipo_negociacao.grid(row=0, column=1, sticky='w')

# Status
lbl_status = tk.Label(janela, text='Status:')
lbl_status.grid(row=1, column=0, sticky='e')
cb_status = tk.StringVar(janela)
opcoes_cb_status = ('Disponível', 'Locado', 'Vendido', 'À liberar')
menu_status = tk.OptionMenu(janela, cb_status, *opcoes_cb_status)
menu_status.config(width=10)
menu_status.grid(row=1, column=1, sticky='w')

# Endereço
lbl_endereco = tk.Label(janela, text='Endereço:')
lbl_endereco.grid(row=2, column=0, sticky='e')
txt_endereco = tk.Text(janela, height=2, width=30)
txt_endereco.grid(row=2, column=1)

# Tipo do imóvel
lbl_tipo_imovel = tk.Label(janela, text='Tipo do imóvel:')
lbl_tipo_imovel.grid(row=3, column=0, sticky='e')
cb_tipo_imovel = tk.StringVar(janela)
opcoes_cb_tipo_imovel = ('Apartamento', 'Casa', 'Terreno')
menu_tipo_imovel = tk.OptionMenu(janela, cb_tipo_imovel, *opcoes_cb_tipo_imovel)
menu_tipo_imovel.config(width=10)
menu_tipo_imovel.grid(row=3, column=1, sticky='w')

# Características
lbl_caracteristicas = tk.Label(janela, text='Características:')
lbl_caracteristicas.grid(row=4, column=0, sticky='e')
txt_caracteristicas = tk.Text(janela, height=4, width=30)
txt_caracteristicas.grid(row=4, column=1)

# Preço
lbl_preco = tk.Label(janela, text='Preço:')
lbl_preco.grid(row=5, column=0, sticky='e')
txt_preco = tk.Text(janela, height=1, width=30)
txt_preco.grid(row=5, column=1)

# Condições
lbl_condicoes = tk.Label(janela, text='Condições:')
lbl_condicoes.grid(row=6, column=0, sticky='e')
txt_condicoes = tk.Text(janela, height=4, width=30)
txt_condicoes.grid(row=6, column=1)

# Observações
lbl_observacoes = tk.Label(janela, text='Observações:')
lbl_observacoes.grid(row=7, column=0, sticky='e')
txt_observacoes = tk.Text(janela, height=4, width=30)
txt_observacoes.grid(row=7, column=1)

# Botão 'Cadastrar'
btn_cadastrar = tk.Button(janela, text='Cadastrar', command=inserir_dados)
btn_cadastrar.grid(row=8, column=0, sticky='e')

# Botão 'Limpar'
btn_limpar = tk.Button(janela, text='Limpar', command=limpar_formulario)
btn_limpar.grid(row=8, column=1, sticky='w')

# Exibir a janela
janela.mainloop()