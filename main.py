# Import Modules
import sys

from gui.windows.main_window.ui_main_window import UiMainWindow
# Import QtCore
from qt_core import *


# Main Window
# noinspection PyArgumentList
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set Window title
        self.animation = None
        self.setWindowTitle("Padaria Mi Sabores")

        # Remove Window Title Bar
        # noinspection PyTypeChecker
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
        self.ui.cadastrar_produto.clicked.connect(self.cadastrar_produto)

        # Cadastro Produtos Pag2
        self.ui.ui_pages.pushButton_7.clicked.connect(self.cadastro_produtos2)

        # Cadastro Produtos Pag1
        self.ui.ui_pages.pushButton_8.clicked.connect(self.cadastro_produtos1)

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
        # self.ui.size_grip.clicked.connect(lambda: self.size_grip())

        # Move the Window
        def mouse_press_event(self):
            p = self.globalPosition()
            globalPos = p.toPoint()
            self.dragPos = globalPos

        def move_window(event):
            # Detecta se a janela não está expandida
            if self.isMaximized() is False:
                if event.buttons() == Qt.LeftButton:
                    self.move(event.pos() + self.pos())

        self.mouseMoveEvent = move_window

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
    def cadastrar_produto(self):
        self.ui.ui_pages.stackedWidget.setCurrentIndex(1)

    # Cadastro de Produtos Pag2
    def cadastro_produtos2(self):
        # Avançar   
        self.ui.ui_pages.stackedWidget.setCurrentIndex(2)

    # Cadastro de Produtos Pag1
    def cadastro_produtos1(self):
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
            except Exception:
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
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec())
