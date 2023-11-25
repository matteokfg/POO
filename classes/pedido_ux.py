from util_ux import *
from classes.detalhes_pedido_ux import Tela_detalhes_pedido

class Tela_Pedido:

    def __init__(self, root, master, perfil):
        self.root = root
        self.root.state('zoomed')
        self.master = master
        self.root.grab_set()
        self.tipo = "Pedido"
        self.perfil = perfil
        self.ux()

    def bind_pedido_num(self):

        if len(self.dt.view.get_children()) > 0:
            for lin in self.dt.get_rows(selected=True):
                self.pedido.codigo = lin.values[0]
        
    def fun_pesquisar(self):
        
        self.dt.delete_rows()
        self.dt.reset_table()
        
        for ped in self.pedido.listar():
            if self.perfil.codigo_loja in ped['codigos_lojas']:
                connector = Connector(path_banco)
                result = connector.procurar("Comprador", ped["codigo_comprador"], coluna="codigo")
                self.dt.insert_row("end", values=[ped['codigo'],ped['codigo_comprador'],result['nome'],ped['forma_pagamento']])


        self.dt.load_table_data()
        self.dt.view['displaycolumns'] = ('0', '2', '3')
        
    def fun_deletar_pedido(self):
        
        if len(self.dt.view.get_children()) > 0:
            for lin in self.dt.get_rows(selected=True):
                if self.pedido.deletar("Pedido", int(lin.values[0])) != None:
                    self.fun_pesquisar()
                    self.root.grab_set()
                    return
                

    def ux_tabela_pedido(self):

        frm_tabela = ttk.Frame(self.frm_principal); frm_tabela.pack(anchor="n", padx=150)


        coldata = [
            "Código",
            "Código comprador",
            "Comprador",
            "Forma pagamento"
        ]
        
        self.pedido = Pedido(codigo=0, 
                        codigos_produtos=[0], 
                        quantidades=[0], 
                        codigo_comprador=0, 
                        codigos_lojas=[0], 
                        forma_pagamento="Boleto")
        
        rowdata = []
        
        for ped in self.pedido.listar():
            if self.perfil.codigo_loja in ped['codigos_lojas']:
                connector = Connector(path_banco)
                result = connector.procurar("Comprador", ped["codigo_comprador"], coluna="codigo")
                rowdata.append([ped['codigo'],ped['codigo_comprador'],result['nome'],ped['forma_pagamento']])



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
        self.dt.view['displaycolumns'] = ('0', '2', '3')
        self.dt.view.bind("<<TreeviewSelect>>", lambda e: self.bind_pedido_num())

        frm_btns = ttk.Frame(self.frm_principal); frm_btns.pack(pady=20)
        ttk.Button(frm_btns, text="Voltar", bootstyle="dark-outline", command=self.root.destroy).pack(side="left")
        ttk.Button(frm_btns, text="Excluir pedido selecionado", bootstyle="danger-outline", command=self.fun_deletar_pedido).pack(side="left", padx=10)
        ttk.Button(frm_btns, text="Ver detalhes", bootstyle="primary", command=lambda: Tela_detalhes_pedido(ttk.Toplevel(), self.root, self.pedido, self.perfil)).pack(side="left")
        
        

    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        ttk.Label(self.frm_principal, text="Pedidos", font=(None,16)).pack()
        self.ux_tabela_pedido()

        