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

        self.scoreBox.setLayout(self.scoreLayout)
    
    def createDropDown(self, position, qLabel, qPoint=None):
        qPoints = [" ", "10", "20", "30"]
        qPoint.addItems(qPoints)

        self.scoreLayout.addWidget(qLabel, 1, position)
        self.scoreLayout.addWidget(qPoint, 2, position)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scoresheet()
    sys.exit(app.exec_())
