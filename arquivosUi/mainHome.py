import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from home import Ui_MainWindow as HomeUI
from comojogar import Ui_MainWindow as ComoJogarUI
#from cadastroUsuario import Ui_MainWindow as CadastroUsuarioUI
from mesajogo import Ui_MainWindow as MesaJogoUI

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = HomeUI()
        self.ui.setupUi(self)

        self.ui.pushButtonJogar.clicked.connect(self.jogar)
        self.ui.pushButtonComoJogar.clicked.connect(self.como_jogar)

    def jogar(self):
        self.mesa_jogo = MesaJogo(self)
        self.mesa_jogo.show()
        self.close()

  
    def como_jogar(self):
        self.como_jogar = ComoJogar(self)
        self.como_jogar.show()
        self.close()


class ComoJogar(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.ui = ComoJogarUI()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.home.clicked.connect(self.voltar_home)

    def voltar_home(self):
        self.main_window.show()
        self.close()


class MesaJogo(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.ui = MesaJogoUI()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.pushButton_2.clicked.connect(self.voltar_home)
        self.ui.pushButton_5.clicked.connect(self.como_jogar)

    def como_jogar(self):
        self.como_jogar = ComoJogar(self)
        self.como_jogar.show()
        self.close()

    def voltar_home(self):
        self.main_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec_())