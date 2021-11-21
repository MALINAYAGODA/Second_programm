import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint

SCREEN_SIZE = [400, 400]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pushButton.clicked.connect(self.run)
        self.do_it = False
        color = []
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def initUI(self):
        self.setGeometry(150, 150, *SCREEN_SIZE)
        self.setWindowTitle('Рисуем чудо')
        self.pushButton = QPushButton(self)
        self.pushButton.move(10, 10)
        self.pushButton.setText('Кнопка')

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

        for i in range(5):
            pen = QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), 2)
            qp.setPen(pen)
            r = randint(10, 100)
            x = randint(r, SCREEN_SIZE[0] - r)
            y = randint(r, SCREEN_SIZE[1] - r)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
