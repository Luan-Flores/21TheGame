import sys
import os
import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from gameScreen import Ui_MainWindow

class Blackjack(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inicializa as cartas após a configuração da interface
        self.carta1 = self.ui.labelCarta1
        self.carta2 = self.ui.labelCarta2
        self.carta3 = self.ui.labelCarta3
        self.carta4 = self.ui.labelCarta4
        self.carta5 = self.ui.labelCarta5
        self.carta6 = self.ui.labelCarta6
        self.carta7 = self.ui.labelCarta7
        self.cartasArray = ['self.carta1', 'self.carta2', 'self.carta3', 'self.carta4', 'self.carta5', 'self.carta6', 'self.carta7']


        self.baralho = self.criar_baralho()
        self.mao_jogador = []
        self.mao_dealer = []
        self.iniciar_jogo()

        self.ui.btnComprar.clicked.connect(self.comprar)
        self.ui.btnParar.clicked.connect(self.parar)

        # Diretório onde as imagens das cartas estão armazenadas
        self.caminho_baralho = "../baralhos"
        self.cartas = self.carregar_cartas()

    def carregar_cartas(self):
        cartas = {}
        for arquivo in os.listdir(self.caminho_baralho):
            if arquivo.endswith(".png"):
                nome_carta = os.path.splitext(arquivo)[0]
                cartas[nome_carta] = os.path.join(self.caminho_baralho, arquivo)
        return cartas

    def criar_baralho(self):
        naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'As']
        baralho = [(valor, naipe) for valor in valores for naipe in naipes]
        random.shuffle(baralho)
        return baralho

    def calcular_valor_mao(self, mao):
        valor = 0
        ases = 0
        for carta in mao:
            if carta[0] in ['Valete', 'Dama', 'Rei']:
                valor += 10
            elif carta[0] == 'As':
                ases += 1
                valor += 11
            else:
                valor += int(carta[0])

        while valor > 21 and ases:
            valor -= 10
            ases -= 1

        return valor

    def exibir_mao(self):
        mao_jogador_str = ', '.join([f"{valor} de {naipe}" for valor, naipe in self.mao_jogador])
        mao_dealer_str = ', '.join([f"{valor} de {naipe}" for valor, naipe in self.mao_dealer])
        # self.ui.labelJogador.setText(f'Mão do Jogador: {mao_jogador_str} (Valor: {self.calcular_valor_mao(self.mao_jogador)})')
        # self.ui.labelDealer.setText(f'Mão do Dealer: {mao_dealer_str} (Valor: {self.calcular_valor_mao(self.mao_dealer)})')

    def iniciar_jogo(self):
        if len(self.baralho) < 4:
            self.baralho = self.criar_baralho()
        
        self.mao_jogador = [self.baralho.pop(), self.baralho.pop()]
        self.mao_dealer = [self.baralho.pop(), self.baralho.pop()]
        
        self.exibir_mao()

    def addImgCarta(self, carta, local):
        caminho_imagem = f"../baralhos/{carta}.png"
        # Usa getattr para acessar o atributo dinamicamente
        getattr(self.ui, local).setPixmap(QPixmap(caminho_imagem))

    def clearResult(self):
        caminho_imagem = f"../baralhos/cartaFUNDO.png"
        i=0
        # Usa getattr para acessar o atributo dinamicamente
        for carta in self.cartasArray:
            print(i)
            i+=1
            # Aqui, carta deve ser uma string
            local = f'labelCarta{i}'
            print(local)
            label = getattr(self.ui, local, "Exceptionnnn").setPixmap(QPixmap(caminho_imagem))
            print(f"Carta: {carta} \n Label: {label}")

        self.zerarCounter()
            
            

    def getFirstLetter(self, carta):
        valor = str(carta[0][0])
        naipe = str(carta[1][0])
        cartaFull = str(valor + naipe)
        return cartaFull
    
    def zerarCounter(self):
        self.ui.label_14.setText("0")

    def comprar(self):
        carta_comprada = self.baralho.pop()
        self.mao_jogador.append(carta_comprada)
        valor = self.calcular_valor_mao(self.mao_jogador)
        self.ui.label_14.setText(str(valor))
        

        # Atualiza a imagem da carta comprada
        for i in range(len(self.mao_jogador)):
            # Garante que o índice não ultrapasse o número de cartas disponíveis
            if i < len(self.cartasArray):
                local = f'labelCarta{i + 1}'  # labelCarta1, labelCarta2, etc.
                self.addImgCarta(self.getFirstLetter(self.mao_jogador[i]), local)

        print(f"AAAAAAA {self.mao_jogador}")

        if self.calcular_valor_mao(self.mao_jogador) > 21:
            self.exibir_mao()
            QMessageBox.information(self, 'Resultado', 'Você estourou! O dealer ganhou.')
            self.clearResult()
            self.iniciar_jogo()
        else:
            self.exibir_mao()
        self.vitorias = 0
    def parar(self):
        while self.calcular_valor_mao(self.mao_dealer) < 17:
            self.mao_dealer.append(self.baralho.pop())
        self.exibir_mao()
        valor_jogador = self.calcular_valor_mao(self.mao_jogador)
        valor_dealer = self.calcular_valor_mao(self.mao_dealer)

        if valor_dealer > 21 or valor_jogador > valor_dealer:
            QMessageBox.information(self, 'Resultado', 'Você ganhou!')
            self.vitorias += 1
            self.ui.label_15.setText(str(self.vitorias))
            self.clearResult()
        elif valor_jogador < valor_dealer:
            QMessageBox.information(self, 'Resultado', 'O dealer ganhou!')
            self.clearResult()
        else:
            QMessageBox.information(self, 'Resultado', 'Empate!')
            self.clearResult()
        
        self.iniciar_jogo()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    jogo = Blackjack()
    jogo.show()
    sys.exit(app.exec_())