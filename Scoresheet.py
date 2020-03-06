import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QGroupBox, QGridLayout, QVBoxLayout

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
        q#Point = Dropdown for point value of Question

        '''

        #Question 1

        self.q1Label = QLabel("01", self)
        self.q1Point = QComboBox(self)
        
        self.createDropDown(1, self.q1Label, self.q1Point)

        #Question 2
        self.q2Label = QLabel("02", self)
        self.q2Point = QComboBox(self)
        
        self.createDropDown(2, self.q2Label, self.q2Point)
        
        #Question 3
        self.q3Label = QLabel("03", self)
        self.q3Point = QComboBox(self)
        
        self.createDropDown(3, self.q3Label, self.q3Point)

        #Question 4
        self.q4Label = QLabel("04", self)
        self.q4Point = QComboBox(self)

        self.createDropDown(4, self.q4Label, self.q4Point)

        #Question 5
        self.q5Label = QLabel("05", self)
        self.q5Point = QComboBox(self)

        self.createDropDown(5, self.q5Label, self.q5Point)
        
        #Question 6
        self.q6Label = QLabel("06", self)
        self.q6Point = QComboBox(self)
        
        self.createDropDown(6, self.q6Label, self.q6Point)

        #Question 7
        self.q7Label = QLabel("07", self)
        self.q7Point = QComboBox(self)

        self.createDropDown(7, self.q7Label, self.q7Point)

        #Question 8
        self.q8Label = QLabel("08", self)
        self.q8Point = QComboBox(self)

        self.createDropDown(8, self.q8Label, self.q8Point)
        
        #Question 9
        self.q9Label = QLabel("09", self)
        self.q9Point = QComboBox(self)

        self.createDropDown(9, self.q9Label, self.q9Point)

        #Question 10
        self.q10Label = QLabel("10", self)
        self.q10Point = QComboBox(self)

        self.createDropDown(10, self.q10Label, self.q10Point)

        #Question 11
        self.q11Label = QLabel("11", self)
        self.q11Point = QComboBox(self)

        self.createDropDown(11, self.q11Label, self.q11Point)

        #Question 12
        self.q12Label = QLabel("12", self)
        self.q12Point = QComboBox(self)

        self.createDropDown(12, self.q12Label, self.q12Point)

        #Question 13
        self.q13Label = QLabel("13", self)
        self.q13Point = QComboBox(self)

        self.createDropDown(13, self.q13Label, self.q13Point)

        #Question 14
        self.q14Label = QLabel("14", self)
        self.q14Point = QComboBox(self)

        self.createDropDown(14, self.q14Label, self.q14Point)

        #Question 15
        self.q15Label = QLabel("15", self)
        self.q15Point = QComboBox(self)

        self.createDropDown(15, self.q15Label, self.q15Point)

        #Question 16
        self.q16Label = QLabel("16", self)
        self.q16Point = QComboBox(self)

        self.createDropDown(16, self.q16Label, self.q16Point)

        #Question 17
        self.q17Label = QLabel("17", self)
        self.q17Point = QComboBox(self)

        self.createDropDown(17, self.q17Label, self.q17Point)

        #Question 18
        self.q18Label = QLabel("18", self)
        self.q18Point = QComboBox(self)

        self.createDropDown(18, self.q18Label, self.q18Point)

        #Question 19
        self.q19Label = QLabel("19", self)
        self.q19Point = QComboBox(self)

        self.createDropDown(19, self.q19Label, self.q19Point)

        #Question 20
        self.q20Label = QLabel("20", self)
        self.q20Point = QComboBox(self)

        self.createDropDown(20, self.q20Label, self.q20Point)

        #OT 1
        self.ot1Label = QLabel("OT1", self)
        self.ot1Point = QLabel("10", self)

        self.createDropDown(21, self.ot1Label, self.ot1Point)

        #OT 2
        self.ot2Label = QLabel("OT2", self)
        self.ot2Point = QLabel("10", self)
        
        self.createDropDown(22, self.ot2Label, self.ot2Point)

        #OT 3
        self.ot3Label = QLabel("OT3", self)
        self.ot3Point = QLabel("10", self)

        self.createDropDown(23, self.ot3Label, self.ot3Point)

        self.scoreBox.setLayout(self.scoreLayout)
    
    def createDropDown(self, position, qLabel, qPoint=None):
        qPoints = [" ", "10", "20", "30"]
        if not position > 20:
            qPoint.addItems(qPoints)
        self.scoreLayout.addWidget(qLabel, 1, position)
        self.scoreLayout.addWidget(qPoint, 2, position)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scoresheet()
    sys.exit(app.exec_())
