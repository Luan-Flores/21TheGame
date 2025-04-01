import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QDate
from home import Ui_MainWindow as HomeUI
from comojogar import Ui_MainWindow as ComoJogarUI
from cadastroUsuario import Ui_MainWindow as CadastroUsuarioUI
from mesajogo import Ui_MainWindow as MesaJogoUI

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = HomeUI()
        self.ui.setupUi(self)

        self.ui.pushButtonJogar.clicked.connect(self.jogar)
        self.ui.pushButtonComoJogar.clicked.connect(self.como_jogar)
        self.ui.pushButtonCadastrar.clicked.connect(self.cadastrar)

    def jogar(self):
        self.mesa_jogo = MesaJogo(self)
        self.mesa_jogo.show()
        self.close()

  
    def como_jogar(self):
        self.como_jogar = ComoJogar(self)
        self.como_jogar.show()
        self.close()
        
    def cadastrar(self):
        self.cadastrar = Cadastrar(self)
        self.cadastrar.show()
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


class Cadastrar(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.ui = CadastroUsuarioUI()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.pushButtonVoltar.clicked.connect(self.voltar_home)
        self.ui.pushButtonEnviar.clicked.connect(self.salvar_dados) 
        
    def voltar_home(self):
        self.main_window.show()
        self.close()
        
    def salvar_dados(self):
        nome = self.ui.lineEditNome.text()
        data_nascimento = self.ui.dateEditDataNascimento.date().toString("dd-MM-yyyy")
        email = self.ui.lineEditEmail.text()
        telefone = self.ui.lineEditTelefone.text()

        dados_usuario = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "email": email,
            "telefone": telefone
        }
        
        try:
            with open("cadastro_usuario.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados_usuario, arquivo, indent=4, ensure_ascii=False)

            self.exibir_mensagem_sucesso()
            self.limpar_campos()
        except Exception as e:
            self.exibir_mensagem_erro(str(e))
    
    def exibir_mensagem_sucesso(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Sucesso")
        msg.setText("Cadastro salvo com sucesso!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def exibir_mensagem_erro(self, erro):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")
        msg.setText(f"Ocorreu um erro ao salvar o cadastro:\n{erro}")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    def limpar_campos(self):
        self.ui.lineEditNome.clear()
        self.ui.lineEditEmail.clear()
        self.ui.lineEditTelefone.clear()
        self.ui.dateEditDataNascimento.setDate(QDate(2000, 1, 1)) 
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec_())