# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:01:59 2023

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
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.dialogs import Querybox
from ttkbootstrap.localization import msgcat
from classes.vendedor import Vendedor
from classes.comprador import Comprador
from classes.produto import Produto
from classes.connector import Connector
from classes.carrinho import Carrinho
from ttkbootstrap import localization
from util import path_banco



def on_closing(root, master):
    
    root.destroy()
    master.grab_set()
    
def destruir_elementos(root):
    for w in root.winfo_children():
        w.destroy()