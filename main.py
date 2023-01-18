import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class mainPage(QDialog):
    def __init__(self):
        super(mainPage,self).__init__()
        loadUi("mainPage.ui", self)
        self.computeButton.clicked.connect(self.computeFunction)

    def computeFunction(self):
        gridWidth = self.gridWidthText.text()
        gridHeight = self.gridHeightText.text()
        print("Success", gridWidth, " ", gridHeight)

app = QApplication(sys.argv)
mainwindow = mainPage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
app.exec_()