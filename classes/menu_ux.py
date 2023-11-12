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
from util_ux import *
from ttkbootstrap.tableview import Tableview
from classes.vendedor import Vendedor
from classes.comprador import Comprador

class Login:
    
    def __init__(self, root):
        
        self.root = root
        self.root.minsize(500,500)
        self.ux()
        
    def fun_entrar(self):
        destruir_elementos(self.root)
        Pagina_inicial(self.root)
        
        
    def ux(self):
        
        frm_principal = ttk.Frame(self.root); frm_principal.pack(fill="both", expand=True,padx=20,pady=20)
        
        ttk.Label(frm_principal, text="Login", font=(None,16)).pack()
        
        frm_usuario = ttk.Frame(frm_principal); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Usuário").pack(anchor="w")
        ttk.Entry(frm_usuario).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_usuario, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_principal); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Senha").pack(anchor="w")
        ttk.Entry(frm_senha).pack(fill="x")
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


    def entrar(self):
        on_closing(self.root, self.master)
        destruir_elementos(self.master)
        Pagina_inicial(self.master)
        
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

            self.entrar()

            
            
            

            

        
        
        
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
        self.ux()

    def tabela_comprador(self):

        frm_tabela = ttk.Frame(self.frm_principal); frm_tabela.pack(fill="x")

        coldata = [
            {"text": "LicenseNumber", "stretch": False},
            "CompanyName",
            {"text": "UserCount", "stretch": False},
        ]

        rowdata = [
            ('A123', 'IzzyCo', 12),
            ('A136', 'Kimdee Inc.', 45),
            ('A158', 'Farmadding Co.', 36)
        ]

        dt = Tableview(
            master=frm_tabela,
            coldata=coldata,
            rowdata=rowdata,
            paginated=True,
            searchable=False,
            bootstyle="primary"
        )
        dt.pack(fill="both", expand=True, padx=10, pady=10)


    def barra_superior_comprador(self):
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
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", expand=True)
        if self.tipo == "Comprador":
            self.barra_superior_comprador()
            self.tabela_comprador()
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    
    root = ttk.Window()
    #Login(root)
    Pagina_inicial(root, "Comprador")
    root.mainloop()
        
    