import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import *

class Question(QWidget):
    def __init__(self, questionLabel, overtime):
        super().__init__()
        self.label  = QLabel(questionLabel, self)
        self.overtime = overtime
        if overtime:
            self.value  = 10
            self.points = QLabel("10", self)
        else:
            self.value  = 0
            self.points = QComboBox(self)
        
        self.types      = QComboBox(self)
        self.parts      = QComboBox(self)
        self.notes      = QLineEdit(self)
        
        self.h1a        = 0
        self.h1b        = 0
        self.h2a        = 0
        self.h2b        = 0
        self.h3a        = 0
        self.h3b        = 0

        self.a1a        = 0
        self.a1b        = 0
        self.a2a        = 0
        self.a2b        = 0
        self.a3a        = 0
        self.a3b        = 0

        self.h1aPoints  = QComboBox(self)
        self.h1bPoints  = QComboBox(self)
        self.h2aPoints  = QComboBox(self)
        self.h2bPoints  = QComboBox(self)
        self.h3aPoints  = QComboBox(self)
        self.h3bPoints  = QComboBox(self)

        self.a1aPoints  = QComboBox(self)
        self.a1bPoints  = QComboBox(self)
        self.a2aPoints  = QComboBox(self)
        self.a2bPoints  = QComboBox(self)
        self.a3aPoints  = QComboBox(self)
        self.a3bPoints  = QComboBox(self)
        
        if not overtime:
            self.points.currentIndexChanged[int].connect(self.changePoints)
        
        self.setDropdowns()

    def setDropdowns(self):
        pointList = [" ", "10", "20", "30"]
        typeList  = ["Q?", "QQ", "QC", "CA", "ST", "SAQ", "EQ",
                "ECQ", "STQQ", "STA"]
        partList = [" ", "2A", "2Q2A", "2Q3A", "2Q4A", "2Q5A", 
                  "2Q6A", "3A", "3Q3A", "3Q4A", "3Q5A", "3Q6A",
                  "4A", "5A", "6A", "7A", "8A", "9A", "10A",
                  "11A", "12A", "13A", "14A", "15A", "16A",
                  "17A", "18A", "19A", "20A"]

        if self.overtime:
            pointList_ind = [" ", "10", "-5"]
            self.points.setAlignment(Qt.AlignCenter)
        else:
            pointList_ind = [" ", "+", "-"]
            self.points.addItems(pointList)
        
        self.types.addItems(typeList)
        self.parts.addItems(partList)
        
        self.h1aPoints.addItems(pointList_ind)
        self.h1bPoints.addItems(pointList_ind)
        self.h2aPoints.addItems(pointList_ind)
        self.h2bPoints.addItems(pointList_ind)
        self.h3aPoints.addItems(pointList_ind)
        self.h3bPoints.addItems(pointList_ind)

        self.a1aPoints.addItems(pointList_ind)
        self.a1bPoints.addItems(pointList_ind)
        self.a2aPoints.addItems(pointList_ind)
        self.a2bPoints.addItems(pointList_ind)
        self.a3aPoints.addItems(pointList_ind)
        self.a3bPoints.addItems(pointList_ind)


        self.label.setAlignment(Qt.AlignCenter)
        
        self.label.setFixedWidth(55)
        self.points.setFixedWidth(55)
        self.types.setFixedWidth(55)
        self.parts.setFixedWidth(55)
        self.notes.setFixedWidth(55)
        
        self.h1aPoints.setFixedWidth(55)
        self.h1bPoints.setFixedWidth(55)
        self.h2aPoints.setFixedWidth(55)
        self.h2bPoints.setFixedWidth(55)
        self.h3aPoints.setFixedWidth(55)
        self.h3bPoints.setFixedWidth(55)
        
        self.a1aPoints.setFixedWidth(55)
        self.a1bPoints.setFixedWidth(55)
        self.a2aPoints.setFixedWidth(55)
        self.a2bPoints.setFixedWidth(55)
        self.a3aPoints.setFixedWidth(55)
        self.a3bPoints.setFixedWidth(55)

    def changePoints(self, i):
        if i == 0:
            pointList = [" ", "+", "-"]
        elif i == 1:
            pointList = [" ", "10", "-5"]
        elif i == 2:
            pointList = [" ", "20", "-10"]
        elif i == 3:
            pointList = [" ", "30", "-15"]

        self.clearTeam(self.h1aPoints, self.h1bPoints, self.h2aPoints,
                       self.h2bPoints, self.h3aPoints, self.h3bPoints)
        
        self.clearTeam(self.a1aPoints, self.a1bPoints, self.a2aPoints,
                       self.a2bPoints, self.a3aPoints, self.a3bPoints)

        self.addPoints(pointList, self.h1aPoints, self.h1bPoints,
                       self.h2aPoints, self.h2bPoints, self.h3aPoints,
                       self.h3bPoints)

        self.addPoints(pointList, self.a1aPoints, self.a1bPoints,
                       self.a2aPoints, self.a2bPoints, self.a3aPoints,
                       self.a3bPoints)

    def clearTeam(self, a1, b1, a2, b2, a3, b3):
        a1.clear()
        b1.clear()
        a2.clear()
        b2.clear()
        a3.clear()
        b3.clear()

    def addPoints(self, pointList, a1, b1, a2, b2, a3, b3):
        a1.addItems(pointList)
        b1.addItems(pointList)
        a2.addItems(pointList)
        b2.addItems(pointList)
        a3.addItems(pointList)
        b3.addItems(pointList)

