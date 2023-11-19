from util_ux import *

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
            return

            carrinho = Carrinho(codigo=0,
                                codigos_produtos=[0],
                                quantidades=[0],
                                codigo_comprador="0",
                                codigos_lojas=[0])
            carrinho.adicionar_ao_carrinho(int(self.var_codigo_produto.get()),
                                           quantidade,
                                           int(self.var_loja.get()))
            
            params_carrinho = dict(codigo = carrinho.codigo,
                                   codigos_produto = carrinho.codigos_produtos,
                                   quantidades=carrinho.quantidades,
                                   codigo_comprador=carrinho.codigo_comprador,
                                   codigos_loja=carrinho.codigos_lojas)
            
            print(params_carrinho)

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
            "Código loja",
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