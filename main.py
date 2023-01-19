import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QVBoxLayout, QGroupBox, QVBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt5.uic import loadUi
import numpy as np
from calculations import Calculations
from PIL import Image

class mainPage(QDialog):
    def __init__(self):
        super(mainPage,self).__init__()
        loadUi("mainPage.ui", self)
        self.computeButton.clicked.connect(self.handleInput)

    def savePhoto(grid, self):
        im = Image.fromarray(grid).resize((550,550), resample=Image.NEAREST).save('result.png')
        gridPhoto = QLabel(self)
        gridPhoto.setPixmap(QPixmap('result.png')), gridPhoto.move(540,150), gridPhoto.show()

    def handleInput(self):
        gridWidth = int(self.gridWidthText.text())
        gridHeight = int(self.gridHeightText.text())
        obstaclePercent = int(self.obstacleText.text()) / 100

        grid = Calculations.grassfireComputation(gridWidth, gridHeight, obstaclePercent)
        print(grid)
        mainPage.savePhoto(grid, self)

#Settings
app = QApplication(sys.argv)

#Error Printing for Console (Ignore)
sys._excepthook = sys.excepthook 
def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback) 
    sys.exit(1) 
sys.excepthook = exception_hook 

widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(1200), widget.setFixedHeight(800), widget.show(), widget.addWidget(mainPage())
app.exec_()