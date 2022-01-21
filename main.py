# Import Modules
import sys
import os


# Import QtCore
from qt_core import *
from gui.windows.main_window.ui_main_window import UiMainWindow


# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set Window title
        self.setWindowTitle("Padaria Mi Sabores")

        # Remove Window Title Bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Setup MainWindow
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        # Toggle Button
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Home Button
        self.ui.btn_1.clicked.connect(self.home_page)

        # Cadastros Button
        self.ui.btn_2.clicked.connect(self.cadastros)

        # Cadastrar Produto Button
        self.ui.cadastrar_produto.clicked.connect(self.cadastrarProduto)

        # Cadastro Produtos Pag2
        self.ui.ui_pages.pushButton_7.clicked.connect(self.cadastroProdutos2)

        # Cadastro Produtos Pag1
        self.ui.ui_pages.pushButton_8.clicked.connect(self.cadastroProdutos1)

        # Vendas Button
        self.ui.btn_3.clicked.connect(self.vendas)
        
        # Financeiro Button
        self.ui.btn_4.clicked.connect(self.financeiro)

        # Min button function
        self.ui.minim_button.clicked.connect(lambda: self.showMinimized())

        # Max button function
        self.ui.maxim_button.clicked.connect(lambda: self.show_or_maximize_window())

        # Close button function
        self.ui.close_button.clicked.connect(lambda: self.close())

        # Sizegrip button
        #self.ui.size_grip.clicked.connect(lambda: self.size_grip())


        # Move the Window
        def move_window(e):
            #Detecta se a janela não está expandida
            if self.isMaximized() is False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.pos())
                    e.accept()
        

        self.ui.top_bar.mouseMoveEvent = move_window
    
        # Size_grip
        self.ui.size_grip.grabMouse = QSizeGrip(self.ui.size_grip)
        self.ui.size_grip.setStyleSheet(
            "background-color: {btn_color};"
            )

        # Exibe a aplicação
        self.show()


    # Início
    def home_page(self):
        self.reset_selection()
        self.ui.btn_1.set_active(True)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
    

    # Cadastros
    def cadastros(self):
        self.reset_selection()
        self.ui.btn_2.set_active(True)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)

    
    # Cadastrar Produto
    def cadastrarProduto(self):
        self.ui.ui_pages.stackedWidget.setCurrentIndex(1)

    
    # Cadastro de Produtos Pag2
    def cadastroProdutos2(self):
        # Avançar   
        self.ui.ui_pages.stackedWidget.setCurrentIndex(2)
    

    # Cadastro de Produtos Pag1
    def cadastroProdutos1(self):
        # Voltar
        self.ui.ui_pages.stackedWidget.setCurrentIndex(1)


    # Vendas
    def vendas(self):
        self.reset_selection()
        self.ui.btn_3.set_active(True)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)

    # Financeiro
    def financeiro(self):
        self.reset_selection()
        self.ui.btn_4.set_active(True)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)

    def show_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def toggle_button(self):
        # Get Menu Width
        menu_width = self.ui.left_menu.width()

        # Check with
        width = 50
        if menu_width == 50:
            width = 150
        
        # Menu Animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.InBack)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    