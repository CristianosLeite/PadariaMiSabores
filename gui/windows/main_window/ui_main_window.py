# Import QtCore
from qt_core import *

# Import Pages
from gui.ui_pages import UiStackedWidget

# Import custom widgets
from gui.Widgets.py_push_button import PyPushButton
from gui.Widgets.py_qframe import PyQFrame


# MainWindow
class UiMainWindow(object):
    def __init__(self):
        self.cadastrar_produto = None
        self.pesquisar_produto = None
        self.logo = None
        self.ui_pages = None
        self.pages = None
        self.bottom_right_label = None
        self.size_grip = None
        self.bottom_center_spacer = None
        self.bottom_left_label = None
        self.bottom_bar_layout = None
        self.bottom_bar = None
        self.top_right_label = None
        self.user_button = None
        self.top_center_spacer = None
        self.close_button = None
        self.maxim_button = None
        self.minim_button = None
        self.top_left_label = None
        self.top_bar_layout = None
        self.content_layout = None
        self.top_bar = None
        self.left_menu_label_version = None
        self.settings_btn = None
        self.left_menu_bottom_layout = None
        self.left_menu_bottom_frame = None
        self.left_menu_spacer = None
        self.btn_4 = None
        self.btn_3 = None
        self.btn_2 = None
        self.btn_1 = None
        self.toggle_button = None
        self.left_menu_top_layout = None
        self.left_menu_top_frame = None
        self.left_menu_layout = None
        self.content = None
        self.left_menu = None
        self.main_layout = None
        self.central_frame = None

    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Parametros iniciais
        parent.resize(1080, 580)
        parent.setMinimumSize(1000, 550)

        # Central Widget
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #44475a")

        # Set Central Widget
        parent.setCentralWidget(self.central_frame)

        # Main layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left Menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a; border-radius: 16px;")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(40)

        # Left Menu Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #FFFAFA")

        # Left Menu layout
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Top Frame Menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)

        # Top Frame layout
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # Menu Buttons
        self.toggle_button = PyPushButton(
            text="Ocultar menu",
            cursor=Qt.PointingHandCursor,
            maximum_width=240, heigth=50,
            icon_path="icon_menu"
        )
        self.btn_1 = PyPushButton(
            text="Início",
            cursor=Qt.PointingHandCursor,
            maximum_width=240,
            icon_path="cil-home",
            is_active=True
        )
        self.btn_2 = PyPushButton(
            text="Cadastros",
            cursor=Qt.PointingHandCursor,
            maximum_width=240,
            icon_path="cil-notes",
        )
        self.btn_3 = PyPushButton(
            text="Vendas",
            cursor=Qt.PointingHandCursor,
            maximum_width=240,
            icon_path="cil-cart"
        )
        self.btn_4 = PyPushButton(
            text="Financeiro",
            cursor=Qt.PointingHandCursor,
            maximum_width=240,
            icon_path="cil-chart"
        )

        # Menu Spacer
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Bottom Frame Menu
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)

        # Bottom Frame layout
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # Bottom Button
        self.settings_btn = PyPushButton(
            text="Configurações",
            cursor=Qt.PointingHandCursor,
            maximum_width=240,
            icon_path="icon_settings"
        )

        # Label Version
        self.left_menu_label_version = QLabel("v1.0.0")
        # noinspection PyTypeChecker
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        # TopBar
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(50)
        self.top_bar.setMaximumHeight(50)
        self.top_bar.setStyleSheet("background-color: #28232d; color: #6272a4")

        # TopBar Content
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # TopBar layout
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(0, 0, 0, 0)

        # Left TopLabel
        self.top_left_label = QLabel("Padaria MI Sabores")

        # Min Button
        self.minim_button = PyPushButton(
            text="min",
            heigth=30,
            maximum_width=30,
            btn_color="#28232d",
            icon_path="icon_minimize"
        )

        # Max Button
        self.maxim_button = PyPushButton(
            text="max",
            heigth=30,
            maximum_width=30,
            btn_color="#28232d",
            icon_path="icon_maximize"
        )

        # Close Button
        self.close_button = PyPushButton(
            text="close",
            heigth=30,
            maximum_width=30,
            btn_color="#28232d",
            icon_path="icon_close"
        )

        # Top center Spacer
        self.top_center_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # User Button
        self.user_button = PyPushButton(
            cursor=Qt.PointingHandCursor,
            maximum_width=30, heigth=30,
            btn_color="#28232d",
            icon_path="cil-user"
        )
        self.user_button.setStyleSheet("border-radius: 20px;")

        # Right TopLabel
        self.top_right_label = QLabel("Bem vindo, User")
        self.top_right_label.setStyleSheet("font: 700 9pt 'segoe UI'")

        # Bottombar
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #28232d; color: #6272a4")

        # BottomBar layout
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(0, 0, 0, 0)

        # Left BottomLabel
        self.bottom_left_label = QLabel("By: Cristiano Leite")

        # Bottom center Spacer
        self.bottom_center_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Sizegripe
        self.size_grip = PyPushButton(
            maximum_width=10,
            icon_path="cil-size-grip"

        )
        # self.size_gripe.setStyleSheet("")

        # Right BottomLabel
        self.bottom_right_label = QLabel("© 2021")
        self.bottom_right_label.setStyleSheet("font: 700 9pt 'segoe UI'")

        # Application Pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #6272a4")
        self.ui_pages = UiStackedWidget()
        self.ui_pages.setup_ui(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)

        # Logo inicial
        self.logo = PyQFrame(
            heigth=600,
            maximum_width=1200,
            icon_path="Logo2",
            icon_color="rgb"
        )

        # Cadastro Produtos / Pesquisar Produtos
        self.pesquisar_produto = PyPushButton(
            text="Pesquisar",
            heigth=200,
            minimum_width=200,
            maximum_width=200,
            icon_path="cil-magnifying-glass"
        )

        # Cadastro Produtos / Cadastrar Produtos
        self.cadastrar_produto = PyPushButton(
            text="Cadastrar",
            heigth=200,
            minimum_width=200,
            maximum_width=200,
            icon_path="cil-plus"
        )

        # Add Widgets to App
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
        self.top_bar_layout.addWidget(self.top_left_label)
        self.top_bar_layout.addItem(self.top_center_spacer)
        self.top_bar_layout.addWidget(self.user_button)
        self.top_bar_layout.addWidget(self.top_right_label)
        self.bottom_bar_layout.addWidget(self.bottom_left_label)
        self.bottom_bar_layout.addItem(self.bottom_center_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_right_label)
        self.bottom_bar_layout.addWidget(self.size_grip)
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        self.left_menu_top_layout.addWidget(self.btn_3)
        self.left_menu_top_layout.addWidget(self.btn_4)
        self.left_menu_bottom_layout.addWidget(self.settings_btn)
        self.top_bar_layout.addWidget(self.minim_button)
        self.top_bar_layout.addWidget(self.maxim_button)
        self.top_bar_layout.addWidget(self.close_button)
        self.ui_pages.gridLayout.addWidget(self.logo)
        self.ui_pages.horizontalLayout_39.addWidget(self.pesquisar_produto)
        self.ui_pages.horizontalLayout_40.addWidget(self.cadastrar_produto)
