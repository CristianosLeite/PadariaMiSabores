from main import *


class CadastroProdutos(MainWindow):
    def __init__(self):


        self.ui.ui_pages.pushButton_7.clicked.connect(self.cadastroProdutos2)
    
    

    def cadastroProdutos2(self):
        # Cadastro de Produtos 2
        self.ui.ui_pages.stackedWidget.setCurrentIndex(1)
