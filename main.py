import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QVBoxLayout, QGroupBox, QVBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import numpy as np
from grid import Grid, GridSearch, GridShortestPath, GridSlowMode
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
        try:
            self.computeButton.setEnabled(False)
            self.distance.setText("Distance From Start: ")
            gridWidth = int(self.gridWidthText.text())
            gridHeight = int(self.gridHeightText.text())
            obstaclePercent = int(self.obstacleText.text()) / 100
            
            if ((8 <= gridWidth <= 1000) and (8 <= gridHeight <= 1000) and (.10 <= obstaclePercent <= .20)):
                Grid.totalDistance = 0
                gridMap = Grid.gridComputation(gridWidth, gridHeight, obstaclePercent)
                mainPage.savePhoto(gridMap, self)
                finalGridMap = GridShortestPath.findShortestPath(self.slowMode.isChecked())
                self.worker = WorkerThread()

                if (self.slowMode.isChecked()):
                    self.worker.start()
                    self.worker.update_progress.connect(self.imageUpdate)
                    self.worker.finished.connect(self.imageFinished)
                else:
                    mainPage.savePhoto(finalGridMap, self)
                    self.distance.setText("Distance From Start: " + str(Grid.distanceValue))
                    self.computeButton.setEnabled(True)
            
        except:
            pass
    
    def imageUpdate(self):
        mainPage.savePhoto(Grid.grid, self)
        self.distance.setText("Distance From Start: " + str(Grid.distanceValue))

    def imageFinished(self):
        self.computeButton.setEnabled(True)

class WorkerThread(QThread):
    update_progress = pyqtSignal()

    def run(self):
        Grid.distanceValue = 0
        
        if (Grid.totalDistance <= 5):
            for i in range(0, (Grid.totalDistance), 1):
                GridSlowMode.printPathStep()
                self.update_progress.emit()
                time.sleep(0.75)
        
        elif (5 < Grid.totalDistance <= 10):
            for i in range(0, (Grid.totalDistance), 1):
                GridSlowMode.printPathStep()
                self.update_progress.emit()
                time.sleep(0.40)
        
        elif (10 < Grid.totalDistance <= 20):
            for i in range(0, (Grid.totalDistance), 1):
                GridSlowMode.printPathStep()
                self.update_progress.emit()
                time.sleep(0.20)
        
        else:
            for i in range(0, (Grid.totalDistance), 1):
                GridSlowMode.printPathStep()
                self.update_progress.emit()
                time.sleep(0.05)

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
widget.setFixedWidth(1200), widget.setFixedHeight(800), widget.show(), widget.addWidget(mainPage()), widget.setWindowTitle('Grassfire Algorithm Solver by Callum Brezden')
app.exec_()