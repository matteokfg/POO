from util_ux import *
from classes.principal_ux import Pagina_inicial


class Cadastro_Pessoa:
    
    def __init__(self, root, master, tipo, **kwargs):
        
        self.root = root
        self.master = master
        self.root.grab_set()
        self.root.minsize(800,600)
        self.tipo = tipo
        self.inicializa_variaveis()
        self.ux()

        if "perfil" in kwargs:
            self.perfil = kwargs["perfil"]
            self.carregar()

    def alterar_dados(self):
        
        if self.tipo == "Comprador":

            params_comprador = dict(
                                    codigo = self.var_codigo.get(),
                                    nome = self.var_nome.get(),
                                    senha = self.var_senha.get(),
                                    data_de_nascimento = self.var_data_nascimento.get(),
                                    email = self.var_email.get(),
                                    is_ativo = True,
                                    logradouro = self.var_logradouro.get(),
                                    numero = self.var_numero.get(),
                                    complemento = self.var_complemento.get(),
                                    cidade = self.var_cidade.get(),
                                    uf = self.var_uf.get(),
                                    cep = self.var_cep.get(),
                                    cpf = self.var_cpf.get(),
                                    rg = self.var_rg.get(),
                                    cartao = self.var_cartao.get())

            if self.perfil.atualizar(self.tipo, **params_comprador) != None:
                messagebox.showinfo('','Clique em OK para fazer Login novamente')
                from classes.login_ux import Login
                self.root.destroy()
                destruir_elementos(self.master)
                self.master.state('normal')
                Login(self.master)


    def carregar(self):

        self.btn_success["text"] = "Salvar e sair"
        self.btn_success["command"] = self.alterar_dados

        if self.tipo == "Comprador":

            # Comprador/vendedor
            self.var_codigo.set(self.perfil.codigo)
            self.var_nome.set(self.perfil.nome)
            self.var_senha.set(self.perfil.senha)
            self.var_data_nascimento.set(self.perfil.data_de_nascimento)
            self.var_email.set(self.perfil.email)
            #Endereço
            self.var_logradouro.set(self.perfil.logradouro)
            self.var_numero.set(self.perfil.numero)
            self.var_complemento.set(self.perfil.complemento)
            self.var_cidade.set(self.perfil.cidade)
            self.var_uf.set(self.perfil.uf)
            self.var_cep.set(self.perfil.cep)
            self.var_cpf.set(self.perfil.cpf)
            self.var_rg.set(self.perfil.rg)
            self.var_cartao.set(self.perfil.cartao)

    def inicializa_variaveis(self):
        # Comprador/vendedor
        self.var_codigo = ttk.IntVar()
        self.var_nome = ttk.StringVar()
        self.var_senha = ttk.StringVar()
        self.var_data_nascimento = ttk.StringVar()
        self.var_email = ttk.StringVar()
        #Endereço
        self.var_logradouro = ttk.StringVar()
        self.var_numero = ttk.IntVar()
        self.var_complemento = ttk.StringVar()
        self.var_cidade = ttk.StringVar()
        self.var_uf = ttk.StringVar()
        self.var_cep = ttk.StringVar()
        self.var_cpf = ttk.StringVar()
        self.var_rg = ttk.StringVar()
        self.var_cartao = ttk.StringVar()
        #Loja
        self.var_codigo_loja = ttk.IntVar()
        self.var_cnpj = ttk.StringVar()
        self.var_nome_loja = ttk.StringVar()
        self.var_email_loja = ttk.StringVar()


    def fun_entrar(self, perfil):
        on_closing(self.root, self.master)
        destruir_elementos(self.master)
        Pagina_inicial(self.master, self.tipo, perfil)
        
    def fun_cadastrar(self):

        if self.tipo == "Vendedor":

            loja = Loja(codigo_loja=0,
                        cnpj=self.var_cnpj.get(),
                        nome=self.var_nome_loja.get(),
                        email=self.var_email_loja.get())
            
            params_loja = dict(cnpj=loja.cnpj,
                               nome=loja.nome,
                               email=loja.email)

            vendedor = Vendedor(codigo=0,
                     nome=self.var_nome.get(),
                     senha=self.var_senha.get(),
                     data_de_nascimento=self.var_data_nascimento.get(),
                     email=self.var_email.get(),
                     is_ativo=True,
                     codigo_loja=0)
            
            params_vendedor = dict(
                  nome = vendedor.nome,
                  senha = vendedor.senha,
                  data_de_nascimento = vendedor.data_de_nascimento,
                  email = vendedor.email,
                  is_ativo = vendedor.is_ativo,
                  codigo_loja = vendedor.codigo_loja)
            
            for dado in params_vendedor:
                if params_vendedor[dado] == None:
                    return
                
            for dado in params_loja:
                if params_loja[dado] == None:
                    return
                
            loja.criar("Loja", **params_loja); codigo_loja = loja.codigo_inserido
            params_vendedor["codigo_loja"] = codigo_loja
            vendedor.criar(self.tipo, **params_vendedor)

            self.fun_entrar(vendedor)

        elif self.tipo == "Comprador":

            comprador = Comprador(codigo=0,
                        nome=self.var_nome.get(),
                        senha=self.var_senha.get(),
                        data_de_nascimento=self.var_data_nascimento.get(),
                        email=self.var_email.get(),
                        is_ativo=True,
                        logradouro=self.var_logradouro.get(),
                        numero=self.var_numero.get(),
                        complemento=self.var_complemento.get(),
                        cidade=self.var_cidade.get(),
                        uf=self.var_uf.get(),
                        cep=self.var_cep.get(),
                        cpf=self.var_cpf.get(),
                        rg=self.var_rg.get(),
                        cartao=self.var_cartao.get())
            
            endereco = Endereco(codigo=0,)
            
            params_comprador = dict(
                  nome = comprador.nome,
                  senha = comprador.senha,
                  data_de_nascimento = comprador.data_de_nascimento,
                  email = comprador.email,
                  is_ativo = comprador.is_ativo,
                  cpf = comprador.cpf,
                  rg = comprador.rg,
                  cartao = comprador.cartao)
            

            for dado in params_comprador:
                if params_comprador[dado] == None:
                    return
                
            comprador.criar(self.tipo, **params_comprador)
            
            params_endereco = dict(logradouro = comprador.logradouro,
                                   numero = comprador.numero,
                                   complemento = comprador.complemento,
                                   cidade = comprador.cidade,
                                   uf = comprador.uf,
                                   cep = comprador.cep,
                                   codigo_comprador = comprador.codigo_inserido
                                   )
                
            for dado in params_endereco:
                if params_endereco[dado] == None:
                    return
                
            
                

            


            self.fun_entrar(comprador)

            
            
            

            

        
        
        
    def ux_informacoes_gerais(self):
        
        frm_informacoes_gerais = ttk.Frame(self.notebook); frm_informacoes_gerais.pack(fill="both", expand=True)
        frm_informacoes= ttk.Frame(frm_informacoes_gerais); frm_informacoes.pack(fill="both", expand=True, padx=50)
        
        frm_usuario = ttk.Frame(frm_informacoes); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Código").pack(anchor="w")
        ttk.Entry(frm_usuario, textvariable=self.var_codigo, state="readonly").pack(fill="x")
        
        frm_usuario = ttk.Frame(frm_informacoes); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Nome").pack(anchor="w")
        ttk.Entry(frm_usuario, textvariable=self.var_nome).pack(fill="x")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Senha").pack(anchor="w")
        ttk.Entry(frm_senha, textvariable=self.var_senha, show="*").pack(fill="x")
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Data de nascimento").pack(anchor="w")
        ent_date = ttk.DateEntry(frm_senha); ent_date.pack(fill="x")
        ent_date.entry.configure(textvariable=self.var_data_nascimento)
        
        frm_senha = ttk.Frame(frm_informacoes); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Email").pack(anchor="w")
        ttk.Entry(frm_senha, textvariable=self.var_email).pack(fill="x")

        if self.tipo == "Comprador":

            frm_cpf_rg = ttk.Frame(frm_informacoes); frm_cpf_rg.pack(pady=10, fill="x")
            frm_cpf = ttk.Frame(frm_cpf_rg); frm_cpf.pack(side='left', fill="x", expand=True)
            ttk.Label(frm_cpf, text="CPF").pack(anchor="w")
            ttk.Entry(frm_cpf, textvariable=self.var_cpf).pack(fill="x", expand=True)
            frm_rg = ttk.Frame(frm_cpf_rg); frm_rg.pack(side='left', fill="x", expand=True, padx=(10,0))
            ttk.Label(frm_rg, text="RG").pack(anchor="w")
            ttk.Entry(frm_rg, textvariable=self.var_rg).pack(fill="x", expand=True)

            frm_cartao = ttk.Frame(frm_informacoes); frm_cartao.pack(pady=10, fill="x")
            ttk.Label(frm_cartao, text="Cartão").pack(anchor="w")
            ttk.Entry(frm_cartao, textvariable=self.var_cartao).pack(fill="x")
        
        self.notebook.add(frm_informacoes_gerais, text='Informações gerais')

    def ux_loja(self):

        frm_informacoes_gerais = ttk.Frame(self.notebook); frm_informacoes_gerais.pack(fill="both", expand=True)
        frm_informacoes= ttk.Frame(frm_informacoes_gerais); frm_informacoes.pack(fill="both", expand=True, padx=50)
        
        frm_codigo_loja = ttk.Frame(frm_informacoes); frm_codigo_loja.pack(pady=10, fill="x")
        ttk.Label(frm_codigo_loja, text="Código").pack(anchor="w")
        ttk.Entry(frm_codigo_loja, textvariable=self.var_codigo_loja, state="readonly").pack(fill="x")
        
        frm_cnpj = ttk.Frame(frm_informacoes); frm_cnpj.pack(pady=10, fill="x")
        ttk.Label(frm_cnpj, text="CNPJ").pack(anchor="w")
        ttk.Entry(frm_cnpj, textvariable=self.var_cnpj).pack(fill="x")
        
        frm_nome_loja = ttk.Frame(frm_informacoes); frm_nome_loja.pack(pady=10, fill="x")
        ttk.Label(frm_nome_loja, text="Nome").pack(anchor="w")
        ttk.Entry(frm_nome_loja, textvariable=self.var_nome_loja).pack(fill="x")
        
        frm_email_loja = ttk.Frame(frm_informacoes); frm_email_loja.pack(pady=10, fill="x")
        ttk.Label(frm_email_loja, text="Email").pack(anchor="w")
        ttk.Entry(frm_email_loja, textvariable=self.var_email_loja).pack(fill="x")
        
        self.notebook.add(frm_informacoes_gerais, text='Loja')

        
    def ux_endereco(self):
        
        frm_informacoes_gerais = ttk.Frame(self.notebook); frm_informacoes_gerais.pack(fill="both", expand=True)
        frm_informacoes= ttk.Frame(frm_informacoes_gerais); frm_informacoes.pack(fill="both", expand=True, padx=50)
        
        frm_logradouro = ttk.Frame(frm_informacoes); frm_logradouro.pack(pady=10, fill="x")
        ttk.Label(frm_logradouro, text="Logradouro").pack(anchor="w")
        ttk.Entry(frm_logradouro, textvariable=self.var_logradouro).pack(fill="x")
        
        frm_numero = ttk.Frame(frm_informacoes); frm_numero.pack(pady=10, fill="x")
        ttk.Label(frm_numero, text="Número").pack(anchor="w")
        ttk.Entry(frm_numero, textvariable=self.var_numero).pack(fill="x")
        
        frm_complemento = ttk.Frame(frm_informacoes); frm_complemento.pack(pady=10, fill="x")
        ttk.Label(frm_complemento, text="Complemento").pack(anchor="w")
        ttk.Entry(frm_complemento, textvariable=self.var_complemento).pack(fill="x")
        
        frm_cidade = ttk.Frame(frm_informacoes); frm_cidade.pack(pady=10, fill="x")
        ttk.Label(frm_cidade, text="Cidade").pack(anchor="w")
        ttk.Entry(frm_cidade, textvariable=self.var_cidade).pack(fill="x")
        
        frm_uf = ttk.Frame(frm_informacoes); frm_uf.pack(pady=10, fill="x")
        ttk.Label(frm_uf, text="UF").pack(anchor="w")
        ttk.Entry(frm_uf, textvariable=self.var_uf).pack(fill="x")
        
        frm_cep = ttk.Frame(frm_informacoes); frm_cep.pack(pady=10, fill="x")
        ttk.Label(frm_cep, text="CEP").pack(anchor="w")
        ttk.Entry(frm_cep, textvariable=self.var_cep).pack(fill="x")
        
        self.notebook.add(frm_informacoes_gerais, text='Endereço')
        
    def ux(self):
        
        frm_principal = ttk.Frame(self.root); frm_principal.pack(fill="both", expand=True,padx=20,pady=20)
        
        ttk.Label(frm_principal, text=self.tipo, font=(None,16)).pack()
        
        
        self.notebook = ttk.Notebook(frm_principal)
        self.notebook.pack(expand=True, fill="both")
        
        self.ux_informacoes_gerais()
        if self.tipo == "Comprador":
            self.ux_endereco()
        elif self.tipo == "Vendedor":
            self.ux_loja()
            
        frm_botoes = ttk.Frame(frm_principal); frm_botoes.pack(pady=10, fill="x")
        self.btn_success = ttk.Button(frm_botoes, text="Cadastrar", bootstyle="success-outline", command=self.fun_cadastrar); self.btn_success.pack(pady=10, fill="x")
        ttk.Button(frm_botoes, text="Sair", bootstyle="secondary-outline", command=self.root.destroy).pack(pady=10, fill="x")
            
        
            
            
