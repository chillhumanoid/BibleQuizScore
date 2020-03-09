import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QGroupBox, QGridLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import *
from Question import Question


class Scoresheet(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scoreBox = QGroupBox()
        self.homeTeam = QGroupBox()
        self.awayTeam = QGroupBox()
        
        self.scoreLayout = QGridLayout()
        self.homeLayout  = QGridLayout()
        self.awayLayout  = QGridLayout()

        self.createGridLayout()
        
        self.scoreBox.setLayout(self.scoreLayout)
        self.homeTeam.setLayout(self.homeLayout)
        self.awayTeam.setLayout(self.awayLayout)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.scoreBox)
        windowLayout.addWidget(self.homeTeam)
        windowLayout.addWidget(self.awayTeam)
        self.setLayout(windowLayout)
        
        self.show()


    def createGridLayout(self):
        self.question1  = Question("01", False)
        self.question2  = Question("02", False)
        self.question3  = Question("03", False)
        self.question4  = Question("04", False)
        self.question5  = Question("05", False)
        self.question6  = Question("06", False)
        self.question7  = Question("07", False)
        self.question8  = Question("08", False)
        self.question9  = Question("09", False)
        self.question10 = Question("10", False)
        self.question11 = Question("11", False)
        self.question12 = Question("12", False)
        self.question13 = Question("13", False)
        self.question14 = Question("14", False)
        self.question15 = Question("15", False)
        self.question16 = Question("16", False)
        self.question17 = Question("17", False)
        self.question18 = Question("18", False)
        self.question19 = Question("19", False)
        self.question20 = Question("20", False)
        self.questiono1 = Question("OT 1", True)
        self.questiono2 = Question("OT 2", True)
        self.questiono3 = Question("OT 3", True)

        self.createDropDown(1, self.question1)
        
        self.createDropDown(2, self.question2)
        
        self.createDropDown(3, self.question3)

        self.createDropDown(4, self.question4)

        self.createDropDown(5, self.question5)
        
        self.createDropDown(6, self.question6)

        self.createDropDown(7, self.question7)

        self.createDropDown(8, self.question8)
        
        self.createDropDown(9, self.question9)

        self.createDropDown(10, self.question10)

        self.createDropDown(11, self.question11)

        self.createDropDown(12, self.question12)

        self.createDropDown(13, self.question13)

        self.createDropDown(14, self.question14)

        self.createDropDown(15, self.question15)

        self.createDropDown(16, self.question16)
        
        self.createDropDown(17, self.question17)

        self.createDropDown(18, self.question18)

        self.createDropDown(19, self.question19)
        
        self.createDropDown(20, self.question20)

        self.createDropDown(21, self.questiono1)

        self.createDropDown(22, self.questiono2)

        self.createDropDown(23, self.questiono3)

    
    def createDropDown(self, position, question):
        self.scoreLayout.addWidget(question.label, 1, position)                          
        self.scoreLayout.addWidget(question.points, 2, position)
        self.scoreLayout.addWidget(question.types,  3, position)
        self.scoreLayout.addWidget(question.parts,  4, position)
        self.scoreLayout.addWidget(question.notes,  5, position)
        
        self.homeLayout.addWidget(question.h1qPoints, 1, position)
        self.homeLayout.addWidget(question.h1sPoints, 2, position)
        self.homeLayout.addWidget(question.h2qPoints, 3, position)
        self.homeLayout.addWidget(question.h2sPoints, 4, position)
        self.homeLayout.addWidget(question.h3qPoints, 5, position)
        self.homeLayout.addWidget(question.h3sPoints, 6, position)
        
        self.awayLayout.addWidget(question.a1qPoints, 1, position)
        self.awayLayout.addWidget(question.a1sPoints, 2, position)
        self.awayLayout.addWidget(question.a2qPoints, 3, position)
        self.awayLayout.addWidget(question.a2sPoints, 4, position)
        self.awayLayout.addWidget(question.a3qPoints, 5, position)
        self.awayLayout.addWidget(question.a3sPoints, 6, position)
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scoresheet()
    sys.exit(app.exec_())
