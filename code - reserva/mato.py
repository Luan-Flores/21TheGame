import sys
import random
<<<<<<< HEAD:code/mato.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from TwentyOne import Ui_MainWindow  # Importa a interface gerada

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        self.Adicionar.clicked.connect(self.addMeta)
        self.Remover.clicked.connect(self.removeMeta)


# Função para criar um baralho
def criar_baralho():
    naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']
    baralho = [(valor, naipe) for valor in valores for naipe in naipes]
    random.shuffle(baralho)
    return baralho

# Função para calcular o valor da mão
def calcular_valor_mao(mao):
    valor = 0
    ases = 0
    for carta in mao:
        if carta[0] in ['Valete', 'Dama', 'Rei']:
            valor += 10
        elif carta[0] == 'Ás':
            ases += 1
            valor += 11  # Considera o Ás como 11 inicialmente
        else:
            valor += int(carta[0])
    
    # Ajusta o valor dos ases se necessário
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    
    return valor

# Função para exibir a mão
def exibir_mao(mao, nome):
    cartas = ', '.join([f"{valor} de {naipe}" for valor, naipe in mao])
    print(f"{nome}: {cartas} (Valor: {calcular_valor_mao(mao)})")

# Função principal do jogo
def jogar_blackjack():
    baralho = criar_baralho()
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_dealer = [baralho.pop(), baralho.pop()]

    while True:
        exibir_mao(mao_jogador, "Jogador")
        exibir_mao(mao_dealer[:1], "Dealer")  # Mostra apenas uma carta do dealer

        if calcular_valor_mao(mao_jogador) == 21:
            print("Blackjack! Você ganhou!")
            return

        acao = input("Deseja 'comprar' ou 'parar'? ").strip().lower()
        if acao == 'comprar':
            mao_jogador.append(baralho.pop())
            if calcular_valor_mao(mao_jogador) > 21:
                exibir_mao(mao_jogador, "Jogador")
                print("Você estourou! O dealer ganhou.")
                return
        elif acao == 'parar':
            break
        else:
            print("Ação inválida. Tente novamente.")

    while calcular_valor_mao(mao_dealer) < 17:
        mao_dealer.append(baralho.pop())

    exibir_mao(mao_jogador, "Jogador")
    exibir_mao(mao_dealer, "Dealer")

    valor_jogador = calcular_valor_mao(mao_jogador)
    valor_dealer = calcular_valor_mao(mao_dealer)

    if valor_dealer > 21 or valor_jogador > valor_dealer:
        print("Você ganhou!")
    elif valor_jogador < valor_dealer:
        print("O dealer ganhou!")
    else:
        print("Empate!")

# Iniciar o jogo
if __name__ == "__main__":
    jogar_blackjack()
=======
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

class Jogo21(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jogo 21 de Cartas")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        self.layout = QVBoxLayout()

        # Lista de labels para as cartas
        self.cartas_labels = [QLabel(self) for _ in range(7)]
        for label in self.cartas_labels:
            label.setFixedSize(100, 150)  # Tamanho das cartas
            self.layout.addWidget(label)

        # Botão para comprar carta
        self.botao_comprar = QPushButton("Comprar Carta", self)
        self.botao_comprar.clicked.connect(self.comprar_carta)
        self.layout.addWidget(self.botao_comprar)

        # Widget central
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # Baralho de cartas (exemplo com 52 cartas)
        self.baralho = [f'carta_{i}.png' for i in range(1, 53)]  # Substitua pelos nomes das suas imagens

    def comprar_carta(self):
        # Seleciona uma carta aleatória
        carta = random.choice(self.baralho)
        # Encontra um label vazio para mostrar a carta
        for label in self.cartas_labels:
            if label.pixmap() is None:  # Verifica se o label está vazio
                label.setPixmap(QPixmap(carta))
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jogo = Jogo21()
    jogo.show()
    sys.exit(app.exec_())
>>>>>>> a541626c55f157e2820e0ddd630f06d476b34219:main.py
