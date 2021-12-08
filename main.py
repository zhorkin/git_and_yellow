import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from random import randint


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('git2.ui', self)
        self.pushButton.clicked.connect(self.paintcircle)
        self.should_paint_circle = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            diametr = randint(0, 300)
            painter.drawEllipse(randint(0, 700), randint(0, 500), diametr, diametr)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


app = QApplication(sys.argv)
ex = Form()
ex.show()
sys.exit(app.exec_())