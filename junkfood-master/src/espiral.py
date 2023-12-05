class Espiral:
    def __init__(self, nome_produto=' - ', quantidade=0, preco=0.0):
        self.Preco = preco
        self.nome_produto = nome_produto
        self.quantidade = quantidade

    def getNomeDoProduto(self):
        return self.nome_produto

    def setNomeDoProduto(self, nome_produto):
        self.nome_produto = nome_produto

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getPreco(self):
        return self.Preco

    def setPreco(self, preco):
        self.Preco = preco
