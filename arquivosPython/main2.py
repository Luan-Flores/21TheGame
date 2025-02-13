import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox

class Blackjack(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.baralho = self.criar_baralho()
        self.mao_jogador = []
        self.mao_dealer = []
        self.iniciar_jogo()

    def initUI(self):
        self.setWindowTitle('Blackjack')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label_jogador = QLabel('Mão do Jogador: ')
        self.layout.addWidget(self.label_jogador)

        self.label_dealer = QLabel('Mão do Dealer: ')
        self.layout.addWidget(self.label_dealer)

        self.btn_comprar = QPushButton('Comprar')
        self.btn_comprar.clicked.connect(self.comprar)
        self.layout.addWidget(self.btn_comprar)

        self.btn_parar = QPushButton('Parar')
        self.btn_parar.clicked.connect(self.parar)
        self.layout.addWidget(self.btn_parar)

        self.setLayout(self.layout)

    def criar_baralho(self):
        naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']
        baralho = [(valor, naipe) for valor in valores for naipe in naipes]
        random.shuffle(baralho)
        return baralho

    def calcular_valor_mao(self, mao):
        valor = 0
        ases = 0
        for carta in mao:
            if carta[0] in ['Valete', 'Dama', 'Rei']:
                valor += 10
            elif carta[0] == 'Ás':
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
        self.label_jogador.setText(f'Mão do Jogador: {mao_jogador_str} (Valor: {self.calcular_valor_mao(self.mao_jogador)})')
        self.label_dealer.setText(f'Mão do Dealer: {mao_dealer_str} (Valor: {self.calcular_valor_mao(self.mao_dealer)})')

    def iniciar_jogo(self):
        self.mao_jogador = [self.baralho.pop(), self.baralho.pop()]
        self.mao_dealer = [self.baralho.pop(), self.baralho.pop()]
        self.exibir_mao()

    def comprar(self):
        self.mao_jogador.append(self.baralho.pop())
        if self.calcular_valor_mao(self.mao_jogador) > 21:
            self.exibir_mao()
            QMessageBox.information(self, 'Resultado', 'Você estourou! O dealer ganhou.')
            self.iniciar_jogo()
        else:
            self.exibir_mao()

    def parar(self):
        while self.calcular_valor_mao(self.mao_dealer) < 17:
            self.mao_dealer.append(self.baralho.pop())
        self.exibir_mao()
        valor_jogador = self.calcular_valor_mao(self.mao_jogador)
        valor_dealer = self.calcular_valor_mao(self.mao_dealer)

        if valor_dealer > 21 or valor_jogador > valor_dealer:
            QMessageBox.information(self, 'Resultado', 'Você ganhou!')
        elif valor_jogador < valor_dealer:
            QMessageBox.information(self, 'Resultado', 'O dealer ganhou!')
        else:
            QMessageBox.information(self, 'Resultado', 'Empate!')
        
        self.iniciar_jogo()  # Reinicia o jogo após o resultado

if __name__ == '__main__':
    app = QApplication(sys.argv)
    jogo = Blackjack()
    jogo.show()
    sys.exit(app.exec_())