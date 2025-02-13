import sys
import random
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