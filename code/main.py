import sys, os, random
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from gameScreen import Ui_MainWindow

class Blackjack(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.baralho = self.criar_baralho()
        self.mao_jogador = []
        self.mao_dealer = []
        self.iniciar_jogo()
        # self.jogar = QPushButton('jogar')
        # self.jogar.clicked.connect(self.iniciar_jogo())
        self.ui.btnComprar.clicked.connect(self.comprar)
        self.ui.btnParar.clicked.connect(self.parar)
        self.c2 = '../baralhos/2C.png'
        self.ui.labelCarta.setPixmap(QPixmap(self.c2))
        self.str1 = "Alucina"
        self.str2 = "Não faz mal"
        self.stingConc = self.str1 + self.str2 + ".png"
        print(self.stingConc)

        # Diretório onde as imagens das cartas estão armazenadas
        caminho_baralho = "../baralhos"

        # Criar um dicionário para armazenar as cartas
        cartas = {}

        # Percorrer os arquivos na pasta
        for arquivo in os.listdir(caminho_baralho):
            if arquivo.endswith(".png"):                   # Certifique-se de carregar apenas imagens
                nome_carta = os.path.splitext(arquivo)[0]  # Remove a extensão (.png)
                cartas[nome_carta] = os.path.join(caminho_baralho, arquivo)

        # Exemplo de acesso a uma carta específica
        print(cartas["2C"])  # Saída: ../baralhos/2C.png


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
        self.ui.labelJogador.setText(f'Mão do Jogador: {mao_jogador_str} (Valor: {self.calcular_valor_mao(self.mao_jogador)})')
        self.ui.labelDealer.setText(f'Mão do Dealer: {mao_dealer_str} (Valor: {self.calcular_valor_mao(self.mao_dealer)})')

    def iniciar_jogo(self):
        """Distribui as cartas iniciais e reembaralha caso necessário"""
        if len(self.baralho) < 4:  # Verifica se há cartas suficientes no baralho
            self.baralho = self.criar_baralho()  # Recria e embaralha o baralho
        
        self.mao_jogador = [self.baralho.pop(), self.baralho.pop()]
        self.mao_dealer = [self.baralho.pop(), self.baralho.pop()]
        
        self.exibir_mao()
    
    def addImgCarta(self, carta):
        caminho_imagem = f"../baralhos/{carta}.png"
        self.ui.labelCarta.setPixmap(QPixmap(caminho_imagem))
    
    def getFirstLetter(self,carta):
        valor = str(carta[0][0])
        naipe = str(carta[1][0])
        print(valor, naipe)
        cartaFull = str(valor+naipe)
        return cartaFull        
    
    def comprar(self):
        carta_comprada = self.baralho.pop()  # Remove a carta do baralho e armazena
        self.mao_jogador.append(carta_comprada)  # Adiciona à mão do jogador
        self.addImgCarta(self.getFirstLetter(carta_comprada))

        print(carta_comprada)  # Agora imprime a carta correta
        print(self.mao_jogador)  # Exibe a mão do jogador corretamente

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