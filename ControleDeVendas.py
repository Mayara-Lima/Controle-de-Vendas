class Produto:
    __codigo = 0
    __nome = ""
    __preco = 0.0
    __tipo = ""

    def __init__(self, nome, codigo, preco, tipo):
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__tipo = tipo
        print("O produto com código {} foi criado com sucesso! ☑".format(self.__nome))

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self.__tipo = novo_tipo

    def __calcular_total(self, num_unidades):
        valor_total = num_unidades * self.__preco
        print("O valor total do produto código {} é: ".format(self.__nome), valor_total, "euros.")
        return valor_total

    @property
    def calcular_total(self):
        return self.__calcular_total

    @calcular_total.setter
    def calcular_total(self, calcular_total):
        self.__calcular_total = calcular_total

    def __mostrar_calcular_total(self, num_unidades):
        valor_total = num_unidades * self.__preco
        return valor_total

    @property
    def mostrar_calcular_total(self):
        return self.__mostrar_calcular_total

    @mostrar_calcular_total.setter
    def mostrar_calcular_total(self, mostrar_calcular_total):
        self.__mostrar_calcular_total = mostrar_calcular_total


class Pedido:
    __produtos = []
    __quantidade = []

    def __init__(self, produtos=[], quantidade=[]):
        self.__produtos = produtos
        self.__quantidade = quantidade
        print("O pedido foi criado com sucesso! ☑")

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, produtos):
        self.__produtos = produtos

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def add_produto(self, Produto):
        self.produtos.append(Produto)
        print("O produto com código {} foi adicionado com sucesso! ☑".format(Produto.nome))

    def add_quantidade(self, qnt):
        self.quantidade.append(qnt)
        print("A quantidade foi adicionada com sucesso ao produto! ☑".format(Produto.nome))

    def __str__(self):
        return ("O Pedido tem os seguintes produtos {}, e as seguintes quantidades {}".formata(self.__produtos,
                                                                                               self.__quantidades))

    def total_pedido(self):
        montante_total = 0
        for produto, qnt in zip(self.__produtos, self.__quantidade):
            montante_total += produto.mostrar_calcular_total(qnt)
        return montante_total

    def __mostrar_pedido(self):
        total_produtos = sum(self.__quantidade)
        print("--------------O pedido completo é:---------------")
        print("-------------------------------------------------")
        for produto, qnt in zip(self.__produtos, self.__quantidade):
            print("{} = código {}, {} unidades.".format(produto.codigo, produto.nome, qnt))
        print("A quantidade total de produtos é: {} unidades.".format(total_produtos))
        print("O valor total do pedido é: {} euros.".format(self.total_pedido()))
        print("-------------------------------------------------")

    @property
    def mostrar_pedido(self):
        return self.__mostrar_pedido

    @mostrar_pedido.setter
    def mostrar_pedido(self, mostrar_pedido):
        self.__mostrar_pedido = mostrar_pedido


pedido_1 = Pedido([], [])
pedido_1.add_produto(Produto(123, "Caneta", 1, "com ponta fina"))
pedido_1.add_produto(Produto(456, "Caderno", 2, "de capa dura"))
pedido_1.add_produto(Produto(789, "Caneca", 3, "de porcelana"))
pedido_1.add_produto(Produto(100, "Lanyards", 4, "com fecho de segurança"))
pedido_1.add_quantidade(34)
pedido_1.add_quantidade(3)
pedido_1.add_quantidade(4)
pedido_1.add_quantidade(6)
pedido_1.total_pedido()
pedido_1.mostrar_pedido()