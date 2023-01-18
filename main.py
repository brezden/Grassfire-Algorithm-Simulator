import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox, QApplication, QVBoxLayout, QGroupBox, QVBoxLayout, QGridLayout, QPushButton
from PyQt5.uic import loadUi
import numpy as np
from PIL import Image

class mainPage(QDialog):
    def __init__(self):
        super(mainPage,self).__init__()
        loadUi("mainPage.ui", self)
        self.computeButton.clicked.connect(self.computeFunction)

    def randomGridValue(max):
        return np.random.randint(0, max)

    def computeFunction(self):
        gridWidth = int(self.gridWidthText.text())
        gridHeight = int(self.gridHeightText.text())
        obstaclePercent = int(self.obstacleText.text()) / 100
        white = np.array([255, 255, 255])
        black = np.array([0, 0, 0])
        green = np.array([71, 181, 69])
        red = np.array([214, 71, 49])

        # Generate 10x10 grid of random colours
        grid = np.random.randint(255,256, (gridHeight, gridWidth, 3), dtype=np.uint8)

        startY = mainPage.randomGridValue(gridHeight)
        startX = mainPage.randomGridValue(gridWidth)

        grid[startY, startX] = 71, 181, 69 #Green

        endY = np.random.randint(0, gridHeight)

        while True:
            endX = np.random.randint(0, gridWidth)

            if (startX != endX):
                break
        
        grid[endY, endX] = 214, 71, 49 #Red

        amountOfObstacles = round((gridHeight * gridWidth) * obstaclePercent)

        while (amountOfObstacles != 0):
            obsX = mainPage.randomGridValue(gridWidth)
            obsY = mainPage.randomGridValue(gridHeight)
            
            if not(np.array_equal(grid[obsY, obsX], black) or np.array_equal(grid[obsY, obsX], green) or np.array_equal(grid[obsY, obsX], red)):
                grid[obsY, obsX] =  black
                amountOfObstacles -= 1
            
        # Make into PIL Image and scale up using Nearest Neighbour
        im = Image.fromarray(grid).resize((1600,1600), resample=Image.NEAREST)
        im.save('result.png')

app = QApplication(sys.argv)
mainwindow = mainPage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
app.exec_()