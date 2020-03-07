import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QGroupBox, QGridLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import *

class Scoresheet(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.scoreBox)
        self.setLayout(windowLayout)
        
        self.show()

    def createGridLayout(self):
        self.scoreBox = QGroupBox()
        self.scoreLayout = QGridLayout()

        '''
        Naming Conventions
        q#Label = Label at the top of each column for the Question number (all single digit numbers have leading 0 for looks. Over time are OT1 OT2 and OT3
        q#Point = Dropdown for point value of Question  (" " = default)
        q#Type  = Dropdown for types of the question (Q? = default)
        q#Part  = Dropdown for parts of the question (" " = default)
        '''

        #Question 1

        self.q1Label = QLabel("01", self)
        self.q1Point = QComboBox(self)
        self.q1Type  = QComboBox(self)
        self.q1Part  = QComboBox(self)
        self.q1Note  = QLineEdit(self)

        self.createDropDown(1, self.q1Label, self.q1Point, self.q1Type, self.q1Part, self.q1Note)

        #Question 2
        self.q2Label = QLabel("02", self)
        self.q2Point = QComboBox(self)
        self.q2Type  = QComboBox(self)
        self.q2Part  = QComboBox(self)
        self.q2Note  = QLineEdit(self)
        
        self.createDropDown(2, self.q2Label, self.q2Point, self.q2Type, self.q2Part, self.q2Note)
        
        #Question 3
        self.q3Label = QLabel("03", self)
        self.q3Point = QComboBox(self)
        self.q3Type  = QComboBox(self)
        self.q3Part  = QComboBox(self)
        self.q3Note  = QLineEdit(self)
        
        self.createDropDown(3, self.q3Label, self.q3Point, self.q3Type, self.q3Part, self.q3Note)

        #Question 4
        self.q4Label = QLabel("04", self)
        self.q4Point = QComboBox(self)
        self.q4Type  = QComboBox(self)
        self.q4Part  = QComboBox(self)
        self.q4Note  = QLineEdit(self)

        self.createDropDown(4, self.q4Label, self.q4Point, self.q4Type, self.q4Part, self.q4Note)

        #Question 5
        self.q5Label = QLabel("05", self)
        self.q5Point = QComboBox(self)
        self.q5Type  = QComboBox(self)
        self.q5Part  = QComboBox(self)
        self.q5Note  = QLineEdit(self)
        
        self.createDropDown(5, self.q5Label, self.q5Point, self.q5Type, self.q5Part, self.q5Note)
        
        #Question 6
        self.q6Label = QLabel("06", self)
        self.q6Point = QComboBox(self)
        self.q6Type  = QComboBox(self)
        self.q6Part  = QComboBox(self)
        self.q6Note  = QLineEdit(self)

        self.createDropDown(6, self.q6Label, self.q6Point, self.q6Type, self.q6Part, self.q6Note)

        #Question 7
        self.q7Label = QLabel("07", self)
        self.q7Point = QComboBox(self)
        self.q7Type  = QComboBox(self)
        self.q7Part  = QComboBox(self)
        self.q7Note  = QLineEdit(self)

        self.createDropDown(7, self.q7Label, self.q7Point, self.q7Type, self.q7Part, self.q7Note)

        #Question 8
        self.q8Label = QLabel("08", self)
        self.q8Point = QComboBox(self)
        self.q8Type  = QComboBox(self)
        self.q8Part  = QComboBox(self)
        self.q8Note  = QLineEdit(self)

        self.createDropDown(8, self.q8Label, self.q8Point, self.q8Type, self.q8Part, self.q8Note)
        
        #Question 9
        self.q9Label = QLabel("09", self)
        self.q9Point = QComboBox(self)
        self.q9Type  = QComboBox(self)
        self.q9Part  = QComboBox(self)
        self.q9Note  = QLineEdit(self)

        self.createDropDown(9, self.q9Label, self.q9Point, self.q9Type, self.q9Part, self.q9Note)

        #Question 10
        self.q10Label = QLabel("10", self)
        self.q10Point = QComboBox(self)
        self.q10Type  = QComboBox(self)
        self.q10Part  = QComboBox(self)
        self.q10Note  = QLineEdit(self)

        self.createDropDown(10, self.q10Label, self.q10Point, self.q10Type, self.q10Part, self.q10Note)

        #Question 11
        self.q11Label = QLabel("11", self)
        self.q11Point = QComboBox(self)
        self.q11Type  = QComboBox(self)
        self.q11Part  = QComboBox(self)
        self.q11Note  = QLineEdit(self)

        self.createDropDown(11, self.q11Label, self.q11Point, self.q11Type, self.q11Part, self.q11Note)

        #Question 12
        self.q12Label = QLabel("12", self)
        self.q12Point = QComboBox(self)
        self.q12Type  = QComboBox(self)
        self.q12Part  = QComboBox(self)
        self.q12Note  = QLineEdit(self)

        self.createDropDown(12, self.q12Label, self.q12Point, self.q12Type, self.q12Part, self.q12Note)

        #Question 13
        self.q13Label = QLabel("13", self)
        self.q13Point = QComboBox(self)
        self.q13Type  = QComboBox(self)
        self.q13Part  = QComboBox(self)
        self.q13Note  = QLineEdit(self)

        self.createDropDown(13, self.q13Label, self.q13Point, self.q13Type, self.q13Part, self.q13Note)

        #Question 14
        self.q14Label = QLabel("14", self)
        self.q14Point = QComboBox(self)
        self.q14Type  = QComboBox(self)
        self.q14Part  = QComboBox(self)
        self.q14Note  = QLineEdit(self)
        
        self.createDropDown(14, self.q14Label, self.q14Point, self.q14Type, self.q14Part, self.q14Note)

        #Question 15
        self.q15Label = QLabel("15", self)
        self.q15Point = QComboBox(self)
        self.q15Type  = QComboBox(self)
        self.q15Part  = QComboBox(self)
        self.q15Note  = QLineEdit(self)

        self.createDropDown(15, self.q15Label, self.q15Point, self.q15Type, self.q15Part, self.q15Note)

        #Question 16
        self.q16Label = QLabel("16", self)
        self.q16Point = QComboBox(self)
        self.q16Type  = QComboBox(self)
        self.q16Part  = QComboBox(self)
        self.q16Note  = QLineEdit(self)

        self.createDropDown(16, self.q16Label, self.q16Point, self.q16Type, self.q16Part, self.q16Note)

        #Question 17
        self.q17Label = QLabel("17", self)
        self.q17Point = QComboBox(self)
        self.q17Type  = QComboBox(self)
        self.q17Part  = QComboBox(self)
        self.q17Note  = QLineEdit(self)

        self.createDropDown(17, self.q17Label, self.q17Point, self.q17Type, self.q17Part, self.q17Note)

        #Question 18
        self.q18Label = QLabel("18", self)
        self.q18Point = QComboBox(self)
        self.q18Type  = QComboBox(self)
        self.q18Part  = QComboBox(self)
        self.q18Note  = QLineEdit(self)

        self.createDropDown(18, self.q18Label, self.q18Point, self.q18Type, self.q18Part, self.q18Note)

        #Question 19
        self.q19Label = QLabel("19", self)
        self.q19Point = QComboBox(self)
        self.q19Type  = QComboBox(self)
        self.q19Part  = QComboBox(self)
        self.q19Note  = QLineEdit(self)

        self.createDropDown(19, self.q19Label, self.q19Point, self.q19Type, self.q19Part, self.q19Note)

        #Question 20
        self.q20Label = QLabel("20", self)
        self.q20Point = QComboBox(self)
        self.q20Type  = QComboBox(self)
        self.q20Part  = QComboBox(self)
        self.q20Note  = QLineEdit(self)

        self.createDropDown(20, self.q20Label, self.q20Point, self.q20Type, self.q20Part, self.q20Note)

        #OT 1
        self.ot1Label = QLabel("OT1", self)
        self.ot1Point = QLabel("10", self)                                          #not a dropdown because it's always 10 points
        self.ot1Type  = QComboBox(self)
        self.ot1Part  = QComboBox(self)
        self.ot1Note  = QLineEdit(self)

        self.createDropDown(21, self.ot1Label, self.ot1Point, self.ot1Type, self.ot1Part, self.ot1Note)

        #OT 2
        self.ot2Label = QLabel("OT2", self)
        self.ot2Point = QLabel("10", self)
        self.ot2Type  = QComboBox(self)
        self.ot2Part  = QComboBox(self)
        self.ot2Note  = QLineEdit(self)

        self.createDropDown(22, self.ot2Label, self.ot2Point, self.ot2Type, self.ot2Part, self.ot2Note)

        #OT 3
        self.ot3Label = QLabel("OT3", self)
        self.ot3Point = QLabel("10", self)
        self.ot3Type  = QComboBox(self)
        self.ot3Part  = QComboBox(self)
        self.ot3Note  = QLineEdit(self)

        self.createDropDown(23, self.ot3Label, self.ot3Point, self.ot3Type, self.ot3Part, self.ot3Note)

        self.scoreBox.setLayout(self.scoreLayout)
    
    def createDropDown(self, position, qLabel, qPoint, qType, qPart, qNote = None):
        points = [" ", "10", "20", "30"]                                         #Point value list
        types  = ["Q?", "QQ", "QC", "CA", "ST", "SAQ", "EQ",
                "ECQ", "STQQ", "STA"]                                            #Question types, Q? being the default, meaning none given. 
        parts  = [" ", "2A", "2Q2A", "2Q3A", "2Q4A", "2Q5A", 
                  "2Q6A", "3A", "3Q3A", "3Q4A", "3Q5A", "3Q6A",
                  "4A", "5A", "6A", "7A", "8A", "9A", "10A",
                  "11A", "12A", "13A", "14A", "15A", "16A",
                  "17A", "18A", "19A", "20A"]                                    #Question parts, " " being the default

        if not position > 20:                                                    #Position 21, 22, and 23 are OT and are always 10
            qPoint.addItems(points)                                              #if not overtime, add point value to dropdown
        
        
        qType.addItems(types)
        qPart.addItems(parts)
        
        qLabel.setFixedWidth(55)
        qLabel.setAlignment(Qt.AlignCenter)

        #add widgets to layout
        self.scoreLayout.addWidget(qLabel, 1, position)                          
        self.scoreLayout.addWidget(qPoint, 2, position)
        self.scoreLayout.addWidget(qType,  3, position)
        self.scoreLayout.addWidget(qPart,  4, position)
        if not qNote == None:
            self.scoreLayout.addWidget(qNote,  5, position)  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scoresheet()
    sys.exit(app.exec_())
