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
from classes.vendedor import Vendedor

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
        self.var_codigo = ttk.IntVar()
        self.var_nome = ttk.StringVar()
        self.var_senha = ttk.StringVar()
        self.var_data_nascimento = ttk.StringVar()
        self.var_email = ttk.StringVar()
        
    def fun_cadastrar(self):

        if self.tipo == "Vendedor":

            vendedor = Vendedor(codigo=0,
                     nome=self.var_nome.get(),
                     senha=self.var_senha.get(),
                     data_nascimento=self.var_data_nascimento.get(),
                     email=self.var_email.get(),
                     is_ativo=True,
                     codigo_loja=0)
            
            vendedor.criar("Vendedor",
                  codigo = vendedor.codigo,
                  nome = vendedor.nome,
                  senha = vendedor.senha,
                  data_de_nascimento = vendedor.data_de_nascimento,
                  email = vendedor.email,
                  is_ativo = vendedor.is_ativo,
                  codigo_loja = vendedor.codigo_loja)
            
            

        on_closing(self.root, self.master)
        destruir_elementos(self.master)
        Pagina_inicial(self.master)

        
        
        
    def ux_informacoes_gerais(self):
        
        frm_informacoes_gerais = ttk.Frame(self.notebook); frm_informacoes_gerais.pack(fill="both", expand=True)
        frm_informacoes= ttk.Frame(frm_informacoes_gerais); frm_informacoes.pack(fill="both", expand=True, padx=50)
        
        frm_usuario = ttk.Frame(frm_informacoes); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Código").pack(anchor="w")
        ttk.Entry(frm_usuario, textvariable=self.var_codigo).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_usuario, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_usuario = ttk.Frame(frm_informacoes); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Nome").pack(anchor="w")
        ttk.Entry(frm_usuario, textvariable=self.var_nome).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_usuario, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Senha").pack(anchor="w")
        ttk.Entry(frm_senha, textvariable=self.var_senha, show="*").pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Data de nascimento").pack(anchor="w")
        ent_date = ttk.DateEntry(frm_senha); ent_date.pack(fill="x")
        ent_date.entry.configure(textvariable=self.var_data_nascimento)
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Email").pack(anchor="w")
        ttk.Entry(frm_senha, textvariable=self.var_email).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        self.notebook.add(frm_informacoes_gerais, text='Informações gerais')
        
    def ux_endereco(self):
        
        frm_informacoes_gerais = ttk.Frame(self.notebook); frm_informacoes_gerais.pack(fill="both", expand=True)
        frm_informacoes= ttk.Frame(frm_informacoes_gerais); frm_informacoes.pack(fill="both", expand=True, padx=50)
        
        frm_usuario = ttk.Frame(frm_informacoes); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Logradouro").pack(anchor="w")
        ttk.Entry(frm_usuario).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_usuario, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_usuario = ttk.Frame(frm_informacoes); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Número").pack(anchor="w")
        ttk.Entry(frm_usuario).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_usuario, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Complemento").pack(anchor="w")
        ttk.Entry(frm_senha).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Cidade").pack(anchor="w")
        ttk.DateEntry(frm_senha).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="UF").pack(anchor="w")
        ttk.Entry(frm_senha).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="CEP").pack(anchor="w")
        ttk.Entry(frm_senha).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
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
    
    def __init__(self, root):
        
        self.root = root
        self.root.grab_set()
        self.root.state("zoomed")
        ttk.Frame(self.root,bootstyle="danger").pack(fill="both", expand=True)
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    
    root = ttk.Window()
    Login(root)
    root.mainloop()
        
    