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

        self.h1qPoints  = QComboBox(self)
        self.h1sPoints  = QComboBox(self)
        self.h2qPoints  = QComboBox(self)
        self.h2sPoints  = QComboBox(self)
        self.h3qPoints  = QComboBox(self)
        self.h3sPoints  = QComboBox(self)

        self.a1qPoints  = QComboBox(self)
        self.a1sPoints  = QComboBox(self)
        self.a2qPoints  = QComboBox(self)
        self.a2sPoints  = QComboBox(self)
        self.a3qPoints  = QComboBox(self)
        self.a3sPoints  = QComboBox(self)
        
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
        
        self.h1qPoints.addItems(pointList_ind)
        self.h1sPoints.addItems(pointList_ind)
        self.h2qPoints.addItems(pointList_ind)
        self.h2sPoints.addItems(pointList_ind)
        self.h3qPoints.addItems(pointList_ind)
        self.h3sPoints.addItems(pointList_ind)

        self.a1qPoints.addItems(pointList_ind)
        self.a1sPoints.addItems(pointList_ind)
        self.a2qPoints.addItems(pointList_ind)
        self.a2sPoints.addItems(pointList_ind)
        self.a3qPoints.addItems(pointList_ind)
        self.a3sPoints.addItems(pointList_ind)



        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedWidth(55)
        self.points.setFixedWidth(55)
        self.types.setFixedWidth(55)
        self.parts.setFixedWidth(55)
        self.notes.setFixedWidth(55)
        self.h1qPoints.setFixedWidth(55)
        self.h1sPoints.setFixedWidth(55)
        self.h2qPoints.setFixedWidth(55)
        self.h2sPoints.setFixedWidth(55)
        self.h3qPoints.setFixedWidth(55)
        self.h3sPoints.setFixedWidth(55)

        
