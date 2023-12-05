from src.espiral import Espiral


class Maquina:

    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        self.qtdEspirais = qtdEspirais
        self.maximoProdutos = maximoProdutos
        self.espirais = [Espiral()] * self.qtdEspirais
        self.saldoCliente = 0.0
        self.faturamento = 0.0

    def getFaturamento(self) -> float:
        return self.faturamento

    def getMaximoProdutos(self) -> int:
        return self.maximoProdutos

    def getSaldoCliente(self) -> float:
        return self.saldoCliente

    def getSizeEspirais(self) -> int:
        return len(self.espirais)

    def getEspiral(self, indice: int) -> Espiral:
        if 0 <= indice < self.getSizeEspirais():
            return self.espirais[indice]

    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.saldoCliente += value
            return True
        return False

    def receberTroco(self) -> float:
        troco = self.saldoCliente
        self.saldoCliente = 0
        return troco

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        espiral = self.getEspiral(indice)
        if espiral and quantidade <= self.getMaximoProdutos():
            espiral.setNomeDoProduto(nome)
            espiral.setQuantidade(quantidade)
            espiral.setPreco(preco)
            return True
        else:
            return False

    def limparEspiral(self, indice: int) -> bool:
        espiral = self.getEspiral(indice)
        if espiral:
            espiral.setNomeDoProduto(" - ")
            espiral.setQuantidade(0)
            espiral.setPreco(0)
            return True
        else:
            return False

    def vender(self, indice: int) -> bool:
        espiral = self.getEspiral(indice)

        if espiral and espiral.getQuantidade() > 0 and self.saldoCliente >= espiral.getPreco():
            # Verifica se há saldo suficiente e se ainda há quantidade disponível na espiral

            if self.saldoCliente >= espiral.getPreco():
                # Suficiente saldo para a compra

                self.saldoCliente -= espiral.getPreco()
                self.faturamento += espiral.getPreco()
                espiral.setQuantidade(espiral.getQuantidade() - 1)

                if espiral.getQuantidade() == 0:
                    self.limparEspiral(indice)

                return True

        return False

# git commit -m "first commit"
#   git branch -M main
#   git remote add origin https://github.com/Suziane90/junkfood-master.git
#   git push -u origin main

# git remote add origin https://github.com/Suziane90/junkfood-master.git
#   git branch -M main
#   git push -u origin main
