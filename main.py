import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from random import randint

SCREEN_SIZE = [400, 400]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.do_it = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.do_it = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_it:
            qp = QPainter()
            qp.begin(self)
            self.draw_squares(qp)
            qp.end()

    def draw_squares(self, qp):
        pen = QPen(Qt.yellow, 2)
        qp.setPen(pen)
        for i in range(5):
            r = randint(10, 100)
            x = randint(r, SCREEN_SIZE[0] - r)
            y = randint(r, SCREEN_SIZE[1] - r)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
