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

        self.createDropDown(8, self.q8Label)
        
        #Question 9
        self.q9Label = QLabel("09", self)

        self.createDropDown(9, self.q9Label)

        #Question 10
        self.q10Label = QLabel("10", self)
        
        self.createDropDown(10, self.q10Label)

        #Question 11
        self.q11Label = QLabel("11", self)
        
        self.createDropDown(11, self.q11Label)

        #Question 12
        self.q12Label = QLabel("12", self)
        
        self.createDropDown(12, self.q12Label)

        #Question 13
        self.q13Label = QLabel("13", self)
        
        self.createDropDown(13, self.q13Label)

        #Question 14
        self.q14Label = QLabel("14", self)
        
        self.createDropDown(14, self.q14Label)

        #Question 15
        self.q15Label = QLabel("15", self)
        
        self.createDropDown(15, self.q15Label)

        #Question 16
        self.q16Label = QLabel("16", self)
        
        self.createDropDown(16, self.q16Label)

        #Question 17
        self.q17Label = QLabel("17", self)
        
        self.createDropDown(17, self.q17Label)

        #Question 18
        self.q18Label = QLabel("18", self)
        
        self.createDropDown(18, self.q18Label)

        #Question 19
        self.q19Label = QLabel("19", self)
        
        self.createDropDown(19, self.q19Label)

        #Question 20
        self.q20Label = QLabel("20", self)
        
        self.createDropDown(20, self.q20Label)

        #OT 1
        self.ot1Label = QLabel("OT1", self)
        
        self.createDropDown(21, self.ot1Label)

        #OT 2
        self.ot2Label = QLabel("OT2", self)
        
        self.createDropDown(22, self.ot2Label)

        #OT 3
        self.ot3Label = QLabel("OT3", self)
        
        self.createDropDown(23, self.ot3Label)

        self.scoreBox.setLayout(self.scoreLayout)
    
    def createDropDown(self, position, qLabel, qPoint=None):
        qPoints = [" ", "10", "20", "30"]
        if not qPoint == None:
            qPoint.addItems(qPoints)

        self.scoreLayout.addWidget(qLabel, 1, position)
        
        if not qPoint == None: 
            self.scoreLayout.addWidget(qPoint, 2, position)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scoresheet()
    sys.exit(app.exec_())
