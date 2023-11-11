# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:01:59 2023

@author: raulg
"""

def on_closing(root, master):
    
    root.destroy()
    master.grab_set()
    
def destruir_elementos(root):
    for w in root.winfo_children():
        w.destroy()