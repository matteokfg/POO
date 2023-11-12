import os
import time
import json
from tkinter import messagebox
from datetime import datetime

banco = "..\\banco_de_dados.json"

def validate_inteiro(inteiro):
    try:
        int(inteiro)
        return True
    except ValueError:
        messagebox.showerror('',"Apenas são permitidos valores inteiros")
        return False

def validate_float(decimal):
    try:
        float(decimal)
        return True
    except ValueError:
        messagebox.showerror('',"Apenas são permitidos valores decimais")
        return False


def validate_data(date_text):
    date_format='%d/%m/%Y'
    try:
        datetime.strptime(date_text, date_format)
        return True
    except ValueError:
        messagebox.showerror('',"Data não válida")
        return False
    
def validate_bool(booleano):
    if booleano == False or booleano == True:
        return True
    else:
        messagebox.showerror('',"Status não válido")
        return False

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def validate_email(novo_email):
    if(re.fullmatch(regex, novo_email)):
        return True
    else:
        messagebox.showerror('',"Email Inválido!")
        return False
    
def validate_string(frase):
    if type(frase) == type("_"):
        return True
    else:
        messagebox.showerror('',"Apenas são permitidos valores do tipo String!")
        return False
    
def validate_cep(cep):
    if validate_string(cep):
        if len(cep) == 8:
            padrao_cep = re.compile(r'(\d){5}(\d){3}')

            match = padrao_cep.match(cep)
            if match:
                return True
    messagebox.showerror('',"Apenas são permitidos valores do tipo CEP!")
    return False