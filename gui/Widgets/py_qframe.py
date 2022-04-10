import os
from qt_core import *


class PyQFrame(QFrame):
    def __init__(
            self,
            heigth=500,
            minimum_width=500,
            maximum_width=500,
            icon_path="",
            icon_color="#c3ccdf",
    ):
        super().__init__()

        # Parametros padrão dos botões
        self.setMaximumHeight(heigth)
        self.setMinimumHeight(heigth)
        self.setMaximumWidth(maximum_width)

        # Parametros customizaveis
        self.minimum_width = minimum_width
        self.maximum_width = maximum_width
        self.icon_path = icon_path
        self.icon_color = icon_color

    def paintEvent(self, event):
        # Retorna Style anterior
        QFrame.paintEvent(self, event)

        # Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.maximum_width, self.height())
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    @staticmethod
    def draw_icon(qp, image, rect, color):
        # Format  Path
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Draw icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 3,
            (rect.height() - icon.height()) / 10,
            icon
        )
        painter.end()
