from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from gym import Ui_MainWindow  # Importa a interface gerada

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        self.Adicionar.clicked.connect(self.addMeta)
        self.Remover.clicked.connect(self.removeMeta)

    def addMeta(self):
        meta = self.lineEdit.text()
        if meta:
            item = QListWidgetItem(meta)
            item.setCheckState(0)
            
            self.listWidget.addItem(item)
            
            self.lineEdit.clear()

    def removeMeta(self):
        selected_Item = self.listWidget.currentRow()
        if selected_Item >= 0:
            self.listWidget.takeItem(selected_Item)
    
if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    app.exec_()
