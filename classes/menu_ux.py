# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:36:29 2023

@author: raulg
"""
from util_ux import *
from classes.login_ux import Login
        
        
if __name__ == "__main__":
    root = ttk.Window()
    localization.initialize_localities()
    msgcat.MessageCatalog.locale("pt_br")
    Login(root)
    #Pagina_inicial(root, "Comprador")
    root.mainloop()
        
    