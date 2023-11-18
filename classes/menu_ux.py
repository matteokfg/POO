# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:36:29 2023

@author: raulg
"""

import sys
import os

# Obtém o caminho absoluto para o diretório pai de "classes_ux"
projeto_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adiciona o diretório pai ao sys.path
sys.path.append(projeto_path)

import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox
from util_ux import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.dialogs import Querybox
from ttkbootstrap.localization import msgcat
from classes.vendedor import Vendedor
from classes.comprador import Comprador
from classes.produto import Produto
from classes.connector import Connector
from util import path_banco




class Login:
    
    def __init__(self, root):
        
        self.root = root
        self.root.minsize(500,500)
        self.inicializa_variaveis()
        self.ux()

    def inicializa_variaveis(self):

        self.var_nome = ttk.StringVar()
        self.var_senha = ttk.StringVar()
        
    def fun_entrar(self):
        for pessoa in Connector(path_banco).listar_tabela("Comprador"):
            if self.var_nome.get() == pessoa["nome"] and self.var_senha.get() == pessoa["senha"]:
                destruir_elementos(self.root)
                Pagina_inicial(self.root, "Comprador")
                return
        messagebox.showerror('','Nome ou senha inválidos!')
        
        
        
    def ux(self):
        
        frm_principal = ttk.Frame(self.root); frm_principal.pack(fill="both", expand=True,padx=20,pady=20)
        
        ttk.Label(frm_principal, text="Login", font=(None,16)).pack()
        
        frm_usuario = ttk.Frame(frm_principal); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Usuário").pack(anchor="w")
        ttk.Entry(frm_usuario, textvariable=self.var_nome).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_usuario, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_principal); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Senha").pack(anchor="w")
        ttk.Entry(frm_senha, textvariable=self.var_senha, show="*").pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_botoes = ttk.Frame(frm_principal); frm_botoes.pack(pady=10, fill="x")
        ttk.Button(frm_botoes, text="Entrar", bootstyle="success-outline", command=self.fun_entrar).pack(pady=10, fill="x")
        ttk.Button(frm_botoes, text="Sair", bootstyle="secondary-outline").pack(pady=10, fill="x")
        
        frm_cadastro = ttk.Frame(frm_principal); frm_cadastro.pack(pady=10, anchor="center")
        ttk.Label(frm_cadastro, text="Ainda não tem conta?").pack(side="left")
        #ttk.Button(frm_cadastro, text="Cadastrar", bootstyle="secondary-link").pack(side="left")
        mb=ttk.Menubutton(frm_cadastro,text='Cadastrar-se', bootstyle="secondary-outline");  mb.pack(side="left")
        mb.menu=ttk.Menu(mb)
        mb['menu']=mb.menu
        mb.menu.add_command(label='Sou comprador', command=lambda:Cadastro_Pessoa(ttk.Toplevel(), self.root, "Comprador"))
        mb.menu.add_command(label='Sou vendedor', command=lambda:Cadastro_Pessoa(ttk.Toplevel(), self.root, "Vendedor"))
        
class Cadastro_Pessoa:
    
    def __init__(self, root, master, tipo):
        
        self.root = root
        self.master = master
        self.root.grab_set()
        self.root.minsize(800,600)
        self.tipo = tipo
        self.inicializa_variaveis()
        self.ux()

    def inicializa_variaveis(self):
        # Comprador/vendedor
        self.var_codigo = ttk.IntVar()
        self.var_nome = ttk.StringVar()
        self.var_senha = ttk.StringVar()
        self.var_data_nascimento = ttk.StringVar()
        self.var_email = ttk.StringVar()
        #Endereço
        self.var_logradouro = ttk.StringVar()
        self.var_numero = ttk.IntVar()
        self.var_complemento = ttk.StringVar()
        self.var_cidade = ttk.StringVar()
        self.var_uf = ttk.StringVar()
        self.var_cep = ttk.StringVar()
        self.var_cpf = ttk.StringVar()
        self.var_rg = ttk.StringVar()
        self.var_cartao = ttk.StringVar()


    def fun_entrar(self):
        on_closing(self.root, self.master)
        destruir_elementos(self.master)
        Pagina_inicial(self.master, "Comprador")
        
    def fun_cadastrar(self):

        if self.tipo == "Vendedor":

            vendedor = Vendedor(codigo=0,
                     nome=self.var_nome.get(),
                     senha=self.var_senha.get(),
                     data_nascimento=self.var_data_nascimento.get(),
                     email=self.var_email.get(),
                     is_ativo=True,
                     codigo_loja=0)
            
            params_vendedor = dict(
                  nome = vendedor.nome,
                  senha = vendedor.senha,
                  data_de_nascimento = vendedor.data_de_nascimento,
                  email = vendedor.email,
                  is_ativo = vendedor.is_ativo,
                  codigo_loja = vendedor.codigo_loja)
            
            for dado in params_vendedor:
                if params_vendedor[dado] == None:
                    return

            vendedor.criar("Vendedor", **params_vendedor)

            self.entrar()

        elif self.tipo == "Comprador":

            comprador = Comprador(codigo=0,
                        nome=self.var_nome.get(),
                        senha=self.var_senha.get(),
                        data_de_nascimento=self.var_data_nascimento.get(),
                        email=self.var_email.get(),
                        is_ativo=True,
                        logradouro=self.var_logradouro.get(),
                        numero=self.var_numero.get(),
                        complemento=self.var_complemento.get(),
                        cidade=self.var_cidade.get(),
                        uf=self.var_uf.get(),
                        cep=self.var_cep.get(),
                        cpf=self.var_cpf.get(),
                        rg=self.var_rg.get(),
                        cartao=self.var_cartao.get())
            
            params_comprador = dict(
                  nome = comprador.nome,
                  senha = comprador.senha,
                  data_de_nascimento = comprador.data_de_nascimento,
                  email = comprador.email,
                  is_ativo = comprador.is_ativo,
                  logradouro = comprador.logradouro,
                  numero = comprador.numero,
                  complemento = comprador.complemento,
                  cidade = comprador.cidade,
                  uf = comprador.uf,
                  cep = comprador.cep,
                  cpf = comprador.cpf,
                  rg = comprador.rg,
                  cartao = comprador.cartao)
            
            for dado in params_comprador:
                if params_comprador[dado] == None:
                    return
                
            
            comprador.criar("Comprador", **params_comprador)

            self.fun_entrar()

            
            
            

            

        
        
        
    def ux_informacoes_gerais(self):
        
        frm_informacoes_gerais = ttk.Frame(self.notebook); frm_informacoes_gerais.pack(fill="both", expand=True)
        frm_informacoes= ttk.Frame(frm_informacoes_gerais); frm_informacoes.pack(fill="both", expand=True, padx=50)
        
        frm_usuario = ttk.Frame(frm_informacoes); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Código").pack(anchor="w")
        ttk.Entry(frm_usuario, textvariable=self.var_codigo).pack(fill="x")
        
        frm_usuario = ttk.Frame(frm_informacoes); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Nome").pack(anchor="w")
        ttk.Entry(frm_usuario, textvariable=self.var_nome).pack(fill="x")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Senha").pack(anchor="w")
        ttk.Entry(frm_senha, textvariable=self.var_senha, show="*").pack(fill="x")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Data de nascimento").pack(anchor="w")
        ent_date = ttk.DateEntry(frm_senha); ent_date.pack(fill="x")
        ent_date.entry.configure(textvariable=self.var_data_nascimento)
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Email").pack(anchor="w")
        ttk.Entry(frm_senha, textvariable=self.var_email).pack(fill="x")

        if self.tipo == "Comprador":

            frm_cpf_rg = ttk.Frame(frm_informacoes); frm_cpf_rg.pack(pady=10, fill="x")
            frm_cpf = ttk.Frame(frm_cpf_rg); frm_cpf.pack(side='left', fill="x", expand=True)
            ttk.Label(frm_cpf, text="CPF").pack(anchor="w")
            ttk.Entry(frm_cpf, textvariable=self.var_cpf).pack(fill="x", expand=True)
            frm_rg = ttk.Frame(frm_cpf_rg); frm_rg.pack(side='left', fill="x", expand=True, padx=(10,0))
            ttk.Label(frm_rg, text="RG").pack(anchor="w")
            ttk.Entry(frm_rg, textvariable=self.var_rg).pack(fill="x", expand=True)

            frm_cartao = ttk.Frame(frm_informacoes); frm_cartao.pack(pady=10, fill="x")
            ttk.Label(frm_cartao, text="Cartão").pack(anchor="w")
            ttk.Entry(frm_cartao, textvariable=self.var_cartao).pack(fill="x")
        
        self.notebook.add(frm_informacoes_gerais, text='Informações gerais')
        
    def ux_endereco(self):
        
        frm_informacoes_gerais = ttk.Frame(self.notebook); frm_informacoes_gerais.pack(fill="both", expand=True)
        frm_informacoes= ttk.Frame(frm_informacoes_gerais); frm_informacoes.pack(fill="both", expand=True, padx=50)
        
        frm_logradouro = ttk.Frame(frm_informacoes); frm_logradouro.pack(pady=10, fill="x")
        ttk.Label(frm_logradouro, text="Logradouro").pack(anchor="w")
        ttk.Entry(frm_logradouro, textvariable=self.var_logradouro).pack(fill="x")
        
        frm_numero = ttk.Frame(frm_informacoes); frm_numero.pack(pady=10, fill="x")
        ttk.Label(frm_numero, text="Número").pack(anchor="w")
        ttk.Entry(frm_numero, textvariable=self.var_numero).pack(fill="x")
        
        frm_complemento = ttk.Frame(frm_informacoes); frm_complemento.pack(pady=10, fill="x")
        ttk.Label(frm_complemento, text="Complemento").pack(anchor="w")
        ttk.Entry(frm_complemento, textvariable=self.var_complemento).pack(fill="x")
        
        frm_cidade = ttk.Frame(frm_informacoes); frm_cidade.pack(pady=10, fill="x")
        ttk.Label(frm_cidade, text="Cidade").pack(anchor="w")
        ttk.Entry(frm_cidade, textvariable=self.var_cidade).pack(fill="x")
        
        frm_uf = ttk.Frame(frm_informacoes); frm_uf.pack(pady=10, fill="x")
        ttk.Label(frm_uf, text="UF").pack(anchor="w")
        ttk.Entry(frm_uf, textvariable=self.var_uf).pack(fill="x")
        
        frm_cep = ttk.Frame(frm_informacoes); frm_cep.pack(pady=10, fill="x")
        ttk.Label(frm_cep, text="CEP").pack(anchor="w")
        ttk.Entry(frm_cep, textvariable=self.var_cep).pack(fill="x")
        
        self.notebook.add(frm_informacoes_gerais, text='Endereço')
        
    def ux(self):
        
        frm_principal = ttk.Frame(self.root); frm_principal.pack(fill="both", expand=True,padx=20,pady=20)
        
        ttk.Label(frm_principal, text=self.tipo, font=(None,16)).pack()
        
        
        self.notebook = ttk.Notebook(frm_principal)
        self.notebook.pack(expand=True, fill="both")
        
        self.ux_informacoes_gerais()
        if self.tipo == "Comprador":
            self.ux_endereco()
            
        frm_botoes = ttk.Frame(frm_principal); frm_botoes.pack(pady=10, fill="x")
        ttk.Button(frm_botoes, text="Cadastrar", bootstyle="success-outline", command=self.fun_cadastrar).pack(pady=10, fill="x")
        ttk.Button(frm_botoes, text="Sair", bootstyle="secondary-outline", command=self.root.destroy).pack(pady=10, fill="x")
            
        
            
            
class Pagina_inicial:
    
    def __init__(self, root, tipo):
        
        self.root = root
        self.root.grab_set()
        self.root.state("zoomed")
        self.tipo = tipo
        self.inicializa_variaveis()
        self.ux()

    def inicializa_variaveis(self):
        self.var_codigo_produto = ttk.IntVar()
        self.var_nome = ttk.StringVar()
        self.var_descricao = ttk.StringVar()
        self.var_tipo = ttk.StringVar()
        self.var_marca = ttk.StringVar()
        self.var_loja = ttk.StringVar()
        self.var_quantidade = ttk.StringVar()
        self.var_preco = ttk.DoubleVar()

    def bind_atualiza_campos(self):
        for lin in self.dt.get_rows(selected=True):
            self.var_codigo_produto.set(lin.values[0])
            self.var_nome.set(lin.values[1])
            self.var_descricao.set(lin.values[2])
            self.var_tipo.set(lin.values[3])
            self.var_marca.set(lin.values[4])
            self.var_loja.set(lin.values[5])
            self.var_quantidade.set(lin.values[6])
            self.var_preco.set(lin.values[7])

    def fun_adicionar_ao_carrinho(self):
        quantidade = Querybox.get_float(prompt="Informe a quantidade", title="Adicionar ao carrinho", initialvalue=1, minvalue=1, maxvalue=int(self.var_quantidade.get()))
        if quantidade != None:
            print("Adicionado ao carrinho!")

    def ux_dados_produto(self):

        frm_dados_produto = ttk.Frame(self.frm_principal); frm_dados_produto.pack(anchor="n", fill="both", padx=150, pady=20)
        lblfrm_dados_produto = ttk.LabelFrame(frm_dados_produto, text="Dados do Produto"); lblfrm_dados_produto.pack(fill="both", expand=True)

        frm_imagem = ttk.LabelFrame(lblfrm_dados_produto, text="Imagem"); frm_imagem.pack(side='left', fill="y", padx=20, pady=20)
        ttk.Frame(frm_imagem, width=275, height=275, bootstyle='primary').pack()


        frm_campos = ttk.Frame(lblfrm_dados_produto); frm_campos.pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Código", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_codigo_produto).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto, text="Nome", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_nome).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Descrição", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_descricao).pack(fill="x", expand=True)
        
        frm_campos = ttk.Frame(lblfrm_dados_produto); frm_campos.pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Tipo", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_tipo).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto, text="Marca", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_marca).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Loja", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_loja).pack(fill="x", expand=True)

        frm_campos = ttk.Frame(lblfrm_dados_produto); frm_campos.pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Quantidade disponível", font=(None,12,'bold')).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,18), textvariable=self.var_quantidade).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto, text="Preço (R$)", font=(None,12,'bold')).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,18), textvariable=self.var_preco).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto).pack(anchor="w")
        tk.Button(frm_codigo_produto, text="Adicionar ao carrinho", autostyle=False, font=(None,14), background='white', foreground='black', cursor='hand2', command=self.fun_adicionar_ao_carrinho).pack(fill="x", expand=True)



    def ux_tabela_comprador(self):

        frm_tabela = ttk.Frame(self.frm_principal); frm_tabela.pack(anchor="n", fill="both", padx=150)

        produto = Produto(codigo=0,
                          nome="Nome",
                          descricao="Descricao",
                          imagem="a",
                          preco_unitario=2.0,
                          tipo_produto="tipo",
                          marca="marca",
                          quantidade=0,
                          codigo_loja=0)

        coldata = [
            "Código",
            "Nome",
            "Descrição",
            "Tipo",
            "Marca",
            "Loja",
            "Quantidade",
            "Preço unitário"
        ]

        rowdata = []

        for prod in produto.listar():
            rowdata.append((prod["Codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],prod["quantidade"],prod["preco_unitario"]))


        self.dt = Tableview(
            master=frm_tabela,
            coldata=coldata,
            rowdata=rowdata,
            paginated=False,
            searchable=False,
            bootstyle="primary",
            height=20
        )
        self.dt.pack(side='left', fill='x', expand=True, anchor="w")

        verscrlbar = ttk.Scrollbar(frm_tabela, 
                           orient ="vertical", 
                           command = self.dt.view.yview)
        verscrlbar.pack(side='right', fill='y')
        self.dt.view.configure(yscrollcommand = verscrlbar.set)
        self.dt.view.bind("<<TreeviewSelect>>", lambda e: self.bind_atualiza_campos())


    def ux_barra_superior_comprador(self):
        frm_barra = ttk.Frame(self.frm_principal); frm_barra.pack(expand=True, anchor="n", pady=20)
        ttk.Label(frm_barra, text="Pesquisar por: ", font=(None, 16)).pack(side="left", padx=10)
        cbb_pesquisar = ttk.Combobox(frm_barra); cbb_pesquisar.pack(side="left", padx=10)
        ent_pesquisar = ttk.Entry(frm_barra, width=50); ent_pesquisar.pack(side="left", padx=10)
        ttk.Label(frm_barra, text="Filtros: ", font=(None, 16)).pack(side="left", padx=10)
        cbb_filtros = ttk.Combobox(frm_barra); cbb_filtros.pack(side="left", padx=10)
        mb=ttk.Menubutton(frm_barra,text='Meu perfil', bootstyle="dark-outline");  mb.pack(side="left")
        mb.menu=ttk.Menu(mb)
        mb['menu']=mb.menu
        mb.menu.add_command(label='Meus dados')
        mb.menu.add_command(label='Carrinho')
        mb.menu.add_command(label='Sair', command=self.root.destroy)
        
    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        if self.tipo == "Comprador":
            self.ux_barra_superior_comprador()
            self.ux_tabela_comprador()
            self.ux_dados_produto()
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    
    root = ttk.Window()
    msgcat.MessageCatalog.locale("pt_br")
    Login(root)
    #Pagina_inicial(root, "Comprador")
    root.mainloop()
        
    