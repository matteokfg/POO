import os
import time
import json
from datetime import datetime

dados_comprador = "banco_de_dados\\comprador.json"

def increment_id(identifier):
    return identifier + 1


def validate_inteiro(inteiro):
        try:
            int(inteiro)
            return True
        except ValueError:
            print("Apenas são permitidos valores inteiros")
            return False


def validate_data(date_text):
    date_format='%d/%m/%Y'
    try:
        datetime.strptime(date_text, date_format)
        return True
    except ValueError:
        print("Data não válida")
        return False
    
def validate_bool(booleano):
    if booleano == False or booleano == True:
        return True
    else:
        print("Status não válido")
        return False

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def validate_email(novo_email):
    if(re.fullmatch(regex, novo_email)):
        return True
    else:
        print("Email Inválido!")
        return False
    
def validate_string(frase):
    if type(frase) == type("_"):
        return True
    else:
        print("Apenas são permitidos valores do tipo String!")
        return False