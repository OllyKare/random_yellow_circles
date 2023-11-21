import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(320, 410)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)


    def paintEvent(self, event):
            if self.do_paint:
                qp = QPainter()
                qp.begin(self)
                self.draw_circle(qp)
                qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        m = random.randrange(1, 6)
        for i in range(m):
            r = random.randrange(5, 50)
            qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
            qp.drawEllipse(random.randrange(100, 700), random.randrange(100, 500), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
