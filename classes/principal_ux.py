from util_ux import *
from classes.carrinho_ux import Tela_carrinho
from classes.comentario_ux import Tela_comentario


class Pagina_inicial:
    
    def __init__(self, root, tipo, perfil):
        
        self.root = root
        self.root.grab_set()
        self.root.state("zoomed")
        self.tipo = tipo
        self.perfil = perfil
        self.filtros = {"Código": "codigo",
                        "Nome": "nome",
                        "Descrição": "descricao",
                        "Tipo": "tipo",
                        "Marca": "marca",
                        "Loja": "loja"}
        self.carrinho = Carrinho(codigo=0,
                                codigos_produtos=[],
                                quantidades=[],
                                codigo_comprador=self.perfil.codigo,
                                codigos_lojas=[])
        self.params_carrinho = {}
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
        self.var_cod_loja = ttk.IntVar()
        self.var_preco = ttk.DoubleVar()

    def bind_atualiza_campos(self):
        for lin in self.dt.get_rows(selected=True):
            self.var_codigo_produto.set(lin.values[0])
            self.var_nome.set(lin.values[1])
            self.var_descricao.set(lin.values[2])
            self.var_tipo.set(lin.values[3])
            self.var_marca.set(lin.values[4])
            self.var_cod_loja.set(lin.values[5])
            self.var_loja.set(lin.values[6])
            self.var_quantidade.set(lin.values[7])
            self.var_preco.set(lin.values[8])

    def fun_pesquisar(self):

        pass

    def fun_adicionar_ao_carrinho(self):
        quantidade = Querybox.get_integer(prompt="Informe a quantidade", title="Adicionar ao carrinho", initialvalue=1, minvalue=1, maxvalue=int(self.var_quantidade.get()))
        if quantidade != None:

            self.carrinho.adicionar_ao_carrinho(int(self.var_codigo_produto.get()),
                                           quantidade,
                                           int(self.var_cod_loja.get()))
            
            self.params_carrinho = dict(codigo = self.carrinho.codigo,
                                   codigos_produtos = self.carrinho.codigos_produtos,
                                   quantidades=self.carrinho.quantidades,
                                   codigo_comprador=self.carrinho.codigo_comprador,
                                   codigos_lojas=self.carrinho.codigos_lojas)
            
            print(self.params_carrinho)

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
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_cod_loja, width=8).pack(side='left', padx=(0,10))
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_loja).pack(side="left",fill="x", expand=True)

        frm_campos = ttk.Frame(lblfrm_dados_produto); frm_campos.pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Quantidade disponível", font=(None,12,'bold')).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,18), textvariable=self.var_quantidade).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto, text="Preço (R$)", font=(None,12,'bold')).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,18), textvariable=self.var_preco).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto).pack(anchor="w")
        frm_btns = ttk.Frame(frm_codigo_produto); frm_btns.pack(fill="x", expand=True)
        ttk.Button(frm_codigo_produto, text="Comentários", bootstyle="dark-outline", command=lambda: Tela_comentario(ttk.Toplevel(), self.root, "Comentario", codigo_produto=self.var_codigo_produto.get(), codigo_loja=self.var_cod_loja.get(), perfil=self.perfil)).pack(side='left', ipady=5)
        ttk.Button(frm_codigo_produto, text="Adicionar ao carrinho", bootstyle="primary-outline", command=self.fun_adicionar_ao_carrinho).pack(side='left', padx=(10,0), ipady=5)



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
            "Código Loja",
            "Loja",
            "Quantidade",
            "Preço unitário"
        ]

        rowdata = []

        for prod in produto.listar():
            connector = Connector(path_banco)
            result = connector.procurar("Loja", prod["codigo_loja"], coluna="codigo")
            rowdata.append((prod["codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],result["nome"],prod["quantidade"],prod["preco_unitario"]))


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
        self.dt.view['displaycolumns'] = ('0', '1', '2', '3', '4', '6', '7', '8')


    def ux_barra_superior_comprador(self):
        frm_barra = ttk.Frame(self.frm_principal); frm_barra.pack(expand=True, anchor="n", pady=20)
        ttk.Label(frm_barra, text="Pesquisar por: ", font=(None, 16)).pack(side="left", padx=10)
        cbb_pesquisar = ttk.Combobox(frm_barra, values=[*self.filtros.keys()], state="readonly"); cbb_pesquisar.pack(side="left", padx=10); cbb_pesquisar.set("Código")
        ent_pesquisar = ttk.Entry(frm_barra, width=50); ent_pesquisar.pack(side="left", padx=10)
        mb=ttk.Menubutton(frm_barra,text='Meu perfil', bootstyle="dark-outline");  mb.pack(side="left")
        mb.menu=ttk.Menu(mb)
        mb['menu']=mb.menu
        from classes.cadastro_pessoa_ux import Cadastro_Pessoa
        mb.menu.add_command(label='Meus dados', command=lambda: Cadastro_Pessoa(ttk.Toplevel(), self.root, self.tipo, perfil=self.perfil))
        mb.menu.add_command(label='Carrinho', command=lambda: Tela_carrinho(ttk.Toplevel(),self.root, self.params_carrinho))
        mb.menu.add_command(label='Sair', command=self.root.destroy)
        
    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        if self.tipo == "Comprador":
            self.ux_barra_superior_comprador()
            self.ux_tabela_comprador()
            self.ux_dados_produto()