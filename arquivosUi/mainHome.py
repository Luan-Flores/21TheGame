import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from home import Ui_MainWindow as home
from comojogar import Ui_MainWindow as comojogar
from cadastroUsuario import Ui_MainWindow as cadastroUsuario
from mesajogo import Ui_MainWindow as mesajogo



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = home()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.jogar)
        self.ui.pushButton_2.clicked.connect(self.cadastrar)
        self.ui.pushButton_3.clicked.connect(self.como_jogar)
        self.ui.pushButton_4.clicked.connect(self.sair)
    
    def jogar(self):
        self.comojogar = mesajogo(self)
        self.comojogar.show()
        self.close()

    def cadastrar(self):
        self.cadastrarnovo = cadastroUsuario(self)
        self.cadastrarnovo = show()
        self.close()
    
    def como_jogar(self):
        self.comoJogar = comojogar(self)
        self.comoJogar = show()
        self.close()
    
    def sair(self):
        self.close()



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec_())