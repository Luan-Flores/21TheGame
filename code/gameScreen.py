# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1341, 811))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagens/Apresentação de Slides Corporativo Preto e Amarelo (2).jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.labelCarta = QtWidgets.QLabel(self.centralwidget)
        self.labelCarta.setGeometry(QtCore.QRect(30, 460, 141, 231))
        self.labelCarta.setText("")
        self.labelCarta.setPixmap(QtGui.QPixmap("baralhos/4C.png"))
        self.labelCarta.setScaledContents(True)
        self.labelCarta.setObjectName("labelCarta")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 470, 141, 221))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("baralhos/2P.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 470, 141, 221))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("baralhos/5C.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 470, 141, 221))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("baralhos/RO.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(790, 470, 141, 221))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("baralhos/AC.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(980, 470, 141, 221))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("baralhos/5E.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1170, 470, 141, 221))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("baralhos/JE.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 340, 391, 141))
        font = QtGui.QFont()
        font.setPointSize(29)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#ffffff;")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(770, 270, 91, 81))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("imagens/maozinha.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(220, 740, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#ffffff;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(640, 730, 131, 61))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 140, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color:#0ba4eb;\n"
"color:#ffffff;\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 210, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color:#0ba4eb;\n"
"color:#ffffff;\n"
"border-radius:20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1190, 730, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color:#ff0000;\n"
"color:#ffffff;\n"
"border-radius:20px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(680, 740, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:#ffffff;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(360, 740, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:#ffffff;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(830, 740, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:#ffffff;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("../../PROJETO JOGO 21/unnamed.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 280, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color:#0ba4eb;\n"
"color:#ffffff;\n"
"border-radius:20px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.labelJogador = QtWidgets.QLabel(self.centralwidget)
        self.labelJogador.setGeometry(QtCore.QRect(10, 30, 1151, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.labelJogador.setFont(font)
        self.labelJogador.setStyleSheet("color:#ffffff;")
        self.labelJogador.setObjectName("labelJogador")
        self.labelDealer = QtWidgets.QLabel(self.centralwidget)
        self.labelDealer.setGeometry(QtCore.QRect(10, 80, 1151, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.labelDealer.setFont(font)
        self.labelDealer.setStyleSheet("color:#ffffff;")
        self.labelDealer.setObjectName("labelDealer")
        self.btnComprar = QtWidgets.QPushButton(self.centralwidget)
        self.btnComprar.setGeometry(QtCore.QRect(444, 202, 421, 181))
        self.btnComprar.setStyleSheet("background-color: rgba(139, 255, 223, 0);")
        self.btnComprar.setText("")
        self.btnComprar.setObjectName("btnComprar")
        self.btnParar = QtWidgets.QPushButton(self.centralwidget)
        self.btnParar.setGeometry(QtCore.QRect(610, 110, 101, 51))
        self.btnParar.setObjectName("btnParar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "CLICK PARA COMPRAR"))
        self.label_11.setText(_translate("MainWindow", "Soma:"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.setText(_translate("MainWindow", "Perfil"))
        self.pushButton_4.setText(_translate("MainWindow", "Sair"))
        self.label_13.setText(_translate("MainWindow", "Score:"))
        self.label_14.setText(_translate("MainWindow", "Resultado da soma aqui"))
        self.label_15.setText(_translate("MainWindow", "Resultado do seu score"))
        self.pushButton_5.setText(_translate("MainWindow", "Como jogar"))
        self.labelJogador.setText(_translate("MainWindow", "Mão do jogador:"))
        self.labelDealer.setText(_translate("MainWindow", "Mão do dealer:"))
        self.btnParar.setText(_translate("MainWindow", "Parar"))
