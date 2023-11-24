from util_ux import *

class Tela_carrinho:

    def __init__(self, root, master, params_carrinho, perfil):
        self.root = root
        self.root.state('zoomed')
        self.root.grab_set()
        self.master = master
        self.params_carrinho = params_carrinho
        self.tipo = "Pedido"
        self.perfil = perfil
        self.ux()

    def fun_fazer_pagamento(self, forma_pagamento):

        pedido = Pedido(codigo=0,
                codigos_produtos=self.params_carrinho["codigos_produtos"],
                quantidades=self.params_carrinho["quantidades"],
                codigo_comprador=self.params_carrinho["codigo_comprador"],
                codigos_lojas=self.params_carrinho["codigos_lojas"],
                forma_pagamento=forma_pagamento)
        
        params_pedido = dict(codigos_produtos=pedido.codigos_produtos,
                             quantidades=pedido.quantidades,
                             codigo_comprador=pedido.codigo_comprador,
                             codigos_lojas=pedido.codigos_lojas,
                             forma_pagamento=pedido.forma_pagamento)

        for dado in params_pedido:
            if params_pedido[dado] == None:
                return
            
        pedido.criar(self.tipo, **params_pedido)
        messagebox.showinfo('', f'Pedido {pedido.codigo_inserido} criado!')
        from classes.cadastro_pessoa_ux import Pagina_inicial
        self.root.destroy()
        destruir_elementos(self.master)
        Pagina_inicial(self.master, "Comprador", self.perfil)

    def ux_tabela_carrinho(self):

        frm_tabela = ttk.Frame(self.frm_principal); frm_tabela.pack(anchor="n", fill="both", padx=150)
        preco_total = 0

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
            "Código Loja",
            "Loja",
            "Quantidade",
            "Preço unitário"
        ]

        rowdata = []

        for n, item in enumerate(self.params_carrinho["codigos_produtos"]):

            for prod in produto.listar():
                connector = Connector(path_banco)
                result = connector.procurar("Loja", prod["codigo_loja"], coluna="codigo")
                if self.params_carrinho["codigos_produtos"][n] == prod["codigo"] and self.params_carrinho["codigos_lojas"][n] == prod["codigo_loja"]:
                    rowdata.append((prod["codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],result["nome"],self.params_carrinho["quantidades"][n],prod["preco_unitario"]))
                    preco_total = float(preco_total + (self.params_carrinho["quantidades"][n]*prod["preco_unitario"]))


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
        #self.dt.view.bind("<<TreeviewSelect>>", lambda e: self.bind_atualiza_campos())
        self.dt.view['displaycolumns'] = ('0', '1', '2', '3', '4', '6', '7', '8')

        frm_btns = ttk.Frame(self.frm_principal); frm_btns.pack(anchor="w", fill="x", padx=(150,0), pady=20)
        ttk.Label(frm_btns, text="Preço Total (R$): ", font=(None,16)).pack(side="left")
        ttk.Label(frm_btns, text=f"{preco_total:.2f}".replace('.',','), font=(None,16)).pack(side="left")
        ttk.Button(frm_btns, text="Excluir selecionados", bootstyle="danger-outline").pack(side="left", padx=(50,0))
        ttk.Button(frm_btns, text="Voltar", bootstyle="dark-outline", command=self.root.destroy).pack(side="left", padx=(10,10))
        mb=ttk.Menubutton(frm_btns,text='Fazer pagamento', bootstyle="primary");  mb.pack(side="left")
        mb.menu=ttk.Menu(mb)
        mb['menu']=mb.menu
        mb.menu.add_command(label='Boleto                   ', command=lambda: self.fun_fazer_pagamento("Boleto"))
        mb.menu.add_command(label='Cartão', command=lambda: self.fun_fazer_pagamento("Cartão"))
        mb.menu.add_command(label='Pix', command=lambda: self.fun_fazer_pagamento("Pix"))
        

    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        ttk.Label(self.frm_principal, text="Carrinho", font=(None,16)).pack()
        if len(self.params_carrinho) > 0:
            self.ux_tabela_carrinho()

        else:
            ttk.Label(self.frm_principal, text="Você ainda não tem produtos adicionado ao carrinho!", font=(None,10)).pack(pady=30)
            ttk.Button(self.frm_principal, text="Voltar", bootstyle="secondary-outline" ,command=self.root.destroy).pack()

        