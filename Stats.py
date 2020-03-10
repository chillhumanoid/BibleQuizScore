import sys
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import *

class Stats(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tenRemaining    = 7
        self.twentyRemaining = 9
        self.thirtyRemaining = 3
        
        self.remainingPoints = 340
        self.remainingQuestions = 20
        
        self.h1aTotal = 0
        self.h1bTotal = 0
        self.h2aTotal = 0
        self.h2bTotal = 0
        self.h3aTotal = 0
        self.h3bTotal = 0
        
        self.a1aTotal = 0
        self.a1bTotal = 0
        self.a2aTotal = 0
        self.a2bTotal = 0
        self.a3aTotal = 0
        self.a3bTotal = 0

        self.h1aCanQO = True
        self.h1bCanQO = True
        self.h2aCanQO = True
        self.h2bCanQO = True
        

