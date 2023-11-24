from util_ux import *
from classes.comentario_ux import Tela_comentario
from classes.carrinho_ux import Tela_carrinho
from classes.pedido_ux import Tela_Pedido


class Pagina_inicial:
    
    def __init__(self, root, tipo, perfil):
        
        self.root = root
        self.root.grab_set()
        self.root.state("zoomed")
        self.tipo = tipo
        self.perfil = perfil
        self.filtros = {"Código Produto": "codigo",
                        "Nome": "nome",
                        "Descrição": "descricao",
                        "Tipo": "tipo_produto",
                        "Marca": "marca",
                        "Código Loja": "codigo_loja"}
        if self.tipo == "Vendedor":
            del self.filtros["Código Loja"]
        self.carrinho = Carrinho(codigo=0,
                                codigos_produtos=[],
                                quantidades=[],
                                codigo_comprador=self.perfil.codigo,
                                codigos_lojas=[])
        self.params_carrinho = {}
        self.inicializa_variaveis()
        self.ux()
        self.bind_atualiza_campos()
        self.root.bind("<F5>", lambda e: self.bind_limpar_campos())

    def inicializa_variaveis(self):
        self.var_pesquisa = ttk.StringVar(); self.var_pesquisa.trace("w", self.fun_pesquisar)
        self.var_codigo_produto = ttk.IntVar()
        self.var_nome = ttk.StringVar()
        self.var_descricao = ttk.StringVar()
        self.var_tipo = ttk.StringVar()
        self.var_marca = ttk.StringVar()
        self.var_loja = ttk.StringVar()
        self.var_quantidade = ttk.StringVar()
        self.var_cod_loja = ttk.IntVar()
        self.var_preco = ttk.DoubleVar()
        
    def bind_limpar_campos(self):
        campos = [self.var_codigo_produto,
                    self.var_nome,
                    self.var_descricao,
                    self.var_tipo,
                    self.var_marca,
                    self.var_quantidade,
                    self.var_preco]
        limpar_campos(campos)

    def bind_atualiza_campos(self):
        if len(self.dt.view.get_children()) > 0:
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
        else:
            campos = [self.var_codigo_produto,
                        self.var_nome,
                        self.var_descricao,
                        self.var_tipo,
                        self.var_marca,
                        self.var_cod_loja,
                        self.var_loja,
                        self.var_quantidade,
                        self.var_preco]
            limpar_campos(campos)
        if self.tipo == "Vendedor":
            self.var_cod_loja.set(self.perfil.codigo_loja)
            connector = Connector(path_banco)
            result = connector.procurar("Loja", self.perfil.codigo_loja, coluna="codigo")
            self.var_loja.set(result["nome"])
            
    def fun_incluir_produto(self, window):
        
        self.produto = Produto(codigo=0,
                          nome=self.var_nome.get(),
                          descricao=self.var_descricao.get(),
                          imagem="",
                          preco_unitario=float(self.var_preco.get()),
                          tipo_produto=self.var_tipo.get(),
                          marca=self.var_marca.get(),
                          quantidade=int(self.var_quantidade.get()),
                          codigo_loja=int(self.var_cod_loja.get()))
        
        params_produto = dict(
                              nome=self.produto.nome,
                              descricao=self.produto.descricao,
                              imagem=self.produto.imagem,
                              preco_unitario=self.produto.preco_unitario,
                              tipo_produto=self.produto.tipo_produto,
                              marca=self.produto.marca,
                              quantidade=self.produto.quantidade,
                              codigo_loja=self.produto.codigo_loja)
        
        for dado in params_produto:
            if params_produto[dado] == None:
                return

        self.produto.criar("Produto", **params_produto)
        window.destroy()
        self.fun_pesquisar()
        
    def fun_alterar_produto(self, window):
        
        params_produto = dict(
                              codigo=int(self.var_codigo_produto.get()),
                              nome=self.var_nome.get(),
                              descricao=self.var_descricao.get(),
                              imagem="",
                              preco_unitario=float(self.var_preco.get()),
                              tipo_produto=self.var_tipo.get(),
                              marca=self.var_marca.get(),
                              quantidade=int(self.var_quantidade.get()),
                              codigo_loja=int(self.var_cod_loja.get()))

        if self.produto.atualizar("Produto", **params_produto) != None:
            window.destroy()
            self.fun_pesquisar()
            
    def fun_deletar_produto(self, window):
        
        if self.produto.deletar("Produto", int(self.var_codigo_produto.get())) != None:
            window.destroy()
            self.fun_pesquisar()
            
            
    def fun_pesquisar(self, *args):

        self.dt.delete_rows()
        self.bind_atualiza_campos()
        self.dt.reset_table()
        
        for prod in self.produto.listar():
            connector = Connector(path_banco)
            result = connector.procurar("Loja", prod["codigo_loja"], coluna="codigo")
            if self.var_pesquisa.get() == "":
                if self.tipo == "Vendedor":
                    if self.perfil.codigo_loja == prod["codigo_loja"]:
                        self.dt.insert_row("end", values=[prod["codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],result["nome"],prod["quantidade"],prod["preco_unitario"]])
                else:
                    self.dt.insert_row("end", values=[prod["codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],result["nome"],prod["quantidade"],prod["preco_unitario"]])
            else:
                if str(prod[self.filtros[self.cbb_pesquisar.get()]]).upper().startswith(self.var_pesquisa.get().upper()):
                    if self.tipo == "Vendedor":
                        if self.perfil.codigo_loja == prod["codigo_loja"]:
                            self.dt.insert_row("end", values=[prod["codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],result["nome"],prod["quantidade"],prod["preco_unitario"]])
                    else:
                        self.dt.insert_row("end", values=[prod["codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],result["nome"],prod["quantidade"],prod["preco_unitario"]])


        self.dt.load_table_data()
        self.dt.view.selection_set(self.dt.view.get_children()[0])
        
    def fun_acao(self):
        
        root2 = ttk.Toplevel()
        root2.grab_set()
        
        frm_btns = ttk.Frame(root2); frm_btns.pack(fill="both", padx=20,pady=20)
        ttk.Label(frm_btns, text="O que deseja fazer?", font=(None,16)).pack()
        ttk.Button(frm_btns, text="Incluir produto com os dados informados", bootstyle="primary-outline" ,width=80, command=lambda: self.fun_incluir_produto(root2)).pack(pady=10)
        ttk.Button(frm_btns, text="Alterar produto selecionado com os dados informados", bootstyle="warning-outline", width=80, command=lambda: self.fun_alterar_produto(root2)).pack(pady=10)
        ttk.Button(frm_btns, text="Excluir produto selecionado", bootstyle="danger-outline", width=80, command=lambda: self.fun_deletar_produto(root2)).pack(pady=10)
        

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
        
        if self.tipo == "Comprador":
            estado = "readonly"
        elif self.tipo == "Vendedor":
            estado = "normal"

        frm_dados_produto = ttk.Frame(self.frm_principal); frm_dados_produto.pack(anchor="n", fill="both", padx=80, pady=20)
        lblfrm_dados_produto = ttk.LabelFrame(frm_dados_produto, text="Dados do Produto"); lblfrm_dados_produto.pack(fill="both", expand=True)

        frm_imagem = ttk.LabelFrame(lblfrm_dados_produto, text="Imagem"); frm_imagem.pack(side='left', fill="y", padx=20, pady=20)
        ttk.Frame(frm_imagem, width=275, height=275, bootstyle='primary').pack()


        frm_campos = ttk.Frame(lblfrm_dados_produto); frm_campos.pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Código", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_codigo_produto, state="readonly").pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto, text="Nome", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_nome, state=estado).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Descrição", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_descricao, state=estado).pack(fill="x", expand=True)
        
        frm_campos = ttk.Frame(lblfrm_dados_produto); frm_campos.pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Tipo", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_tipo, state=estado).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto, text="Marca", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_marca, state=estado).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Loja", font=(None,12)).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_cod_loja, width=8, state="readonly").pack(side='left', padx=(0,10))
        tk.Entry(frm_codigo_produto, font=(None,12), textvariable=self.var_loja, state="readonly").pack(side="left",fill="x", expand=True)

        frm_campos = ttk.Frame(lblfrm_dados_produto); frm_campos.pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left')
        ttk.Label(frm_codigo_produto, text="Quantidade disponível", font=(None,12,'bold')).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,18), textvariable=self.var_quantidade, state=estado).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto, text="Preço (R$)", font=(None,12,'bold')).pack(anchor="w")
        tk.Entry(frm_codigo_produto, font=(None,18), textvariable=self.var_preco, state=estado).pack(fill="x", expand=True)
        frm_codigo_produto = ttk.Frame(frm_campos); frm_codigo_produto.pack(fill="x", expand=True, side='left', padx=20)
        ttk.Label(frm_codigo_produto).pack(anchor="w")
        frm_btns = ttk.Frame(frm_codigo_produto); frm_btns.pack(fill="x", expand=True)
        ttk.Button(frm_codigo_produto, text="Comentários", bootstyle="dark-outline", command=lambda: Tela_comentario(ttk.Toplevel(), self.root, "Comentario", codigo_produto=self.var_codigo_produto.get(), codigo_loja=self.var_cod_loja.get(), perfil=self.perfil, tipo_perfil=self.tipo)).pack(side='left', ipady=5)
        if self.tipo == "Comprador":
            ttk.Button(frm_codigo_produto, text="Adicionar ao carrinho", bootstyle="primary-outline", command=self.fun_adicionar_ao_carrinho).pack(side='left', padx=(10,0), ipady=5)
        elif self.tipo == "Vendedor":
            ttk.Button(frm_codigo_produto, text="Ação", bootstyle="primary-outline", command=self.fun_acao).pack(side='left', padx=(10,0), ipady=5)
            ttk.Label(lblfrm_dados_produto, text="F5 - Limpar campos").pack(anchor= "w")
        



    def ux_tabela(self):

        frm_tabela = ttk.Frame(self.frm_principal); frm_tabela.pack(anchor="n", fill="both", padx=80)

        self.produto = Produto(codigo=0,
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

        for prod in self.produto.listar():
            connector = Connector(path_banco)
            result = connector.procurar("Loja", prod["codigo_loja"], coluna="codigo")
            if self.tipo == "Vendedor":
                if self.perfil.codigo_loja == prod["codigo_loja"]:
                    rowdata.append((prod["codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],result["nome"],prod["quantidade"],prod["preco_unitario"]))
            else:      
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


    def ux_barra_superior(self):
        frm_barra = ttk.Frame(self.frm_principal); frm_barra.pack(expand=True, anchor="n", pady=20)
        ttk.Label(frm_barra, text="Pesquisar por: ", font=(None, 16)).pack(side="left", padx=10)
        self.cbb_pesquisar = ttk.Combobox(frm_barra, values=[*self.filtros.keys()], state="readonly"); self.cbb_pesquisar.pack(side="left", padx=10); self.cbb_pesquisar.set("Código Produto")
        ent_pesquisar = ttk.Entry(frm_barra, width=50, textvariable=self.var_pesquisa); ent_pesquisar.pack(side="left", padx=10)
        mb=ttk.Menubutton(frm_barra,text='Meu perfil', bootstyle="dark-outline");  mb.pack(side="left")
        mb.menu=ttk.Menu(mb)
        mb['menu']=mb.menu
        from classes.cadastro_pessoa_ux import Cadastro_Pessoa
        mb.menu.add_command(label='Meus dados', command=lambda: Cadastro_Pessoa(ttk.Toplevel(), self.root, self.tipo, perfil=self.perfil))
        if self.tipo == "Comprador":
            mb.menu.add_command(label='Carrinho', command=lambda: Tela_carrinho(ttk.Toplevel(),self.root,self.params_carrinho, self.perfil))
        elif self.tipo == "Vendedor":
            mb.menu.add_command(label='Pedidos', command=lambda: Tela_Pedido(ttk.Toplevel(),self.root, self.perfil))
        mb.menu.add_command(label='Sair', command=self.root.destroy)
        
    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        if self.tipo == "Comprador":
            self.ux_barra_superior()
            self.ux_tabela()
            self.ux_dados_produto()
        elif self.tipo == "Vendedor":
            self.ux_barra_superior()
            self.ux_tabela()
            self.ux_dados_produto()
            
            
    