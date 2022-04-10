from main import *


class CadastroProdutos(MainWindow):
    def __init__(self):
        super().__init__()
        self.ui.ui_pages.pushButton_7.clicked.connect(self.cadastro_produtos2)

    def cadastro_produtos2(self):
        # Cadastro de Produtos 2
        self.ui.ui_pages.stackedWidget.setCurrentIndex(1)
