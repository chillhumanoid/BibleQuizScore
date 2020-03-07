import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QGroupBox, QGridLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import *

class Scoresheet(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.createGridLayout()
        self.createHomeTeam()
        self.createAwayTeam()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.scoreBox)
        windowLayout.addWidget(self.homeTeam)
        windowLayout.addWidget(self.awayTeam)
        self.setLayout(windowLayout)
        
        self.show()
    def createHomeTeam(self):
        self.homeTeam = QGroupBox()
        self.homeLayout = QGridLayout()
        '''
        NAMING CONVENTIONS

        h = Home
        # = seat number or question number (seat number first, then question number
        q = quizzer (main quizzer)
        s = substitute
    
        h#q#Point - Point dropdown for home quizzer at seat # for question #
        h#s#Point - Point dropdown for home sub     at seat # for question #
        '''

        #Question 1 
        self.h1q1Point = QComboBox(self)
        self.h1s1Point = QComboBox(self)
        self.h2q1Point = QComboBox(self)
        self.h2s1Point = QComboBox(self)
        self.h3q1Point = QComboBox(self)
        self.h3s1Point = QComboBox(self)

        self.createTeam(1, self.homeLayout, self.h1q1Point, self.h1s1Point, self.h2q1Point,
                        self.h2s1Point, self.h3q1Point, self.h3s1Point)

        #Question 2 
        self.h1q2Point = QComboBox(self)
        self.h1s2Point = QComboBox(self)
        self.h2q2Point = QComboBox(self)
        self.h2s2Point = QComboBox(self)
        self.h3q2Point = QComboBox(self)
        self.h3s2Point = QComboBox(self)

        self.createTeam(2, self.homeLayout, self.h1q2Point, self.h1s2Point, self.h2q2Point,
                        self.h2s2Point, self.h3q2Point, self.h3s2Point)


        #Question 3 
        self.h1q3Point = QComboBox(self)
        self.h1s3Point = QComboBox(self)
        self.h2q3Point = QComboBox(self)
        self.h2s3Point = QComboBox(self)
        self.h3q3Point = QComboBox(self)
        self.h3s3Point = QComboBox(self)

        self.createTeam(3, self.homeLayout, self.h1q3Point, self.h1s3Point, self.h2q3Point,
                        self.h2s3Point, self.h3q3Point, self.h3s3Point)


        #Question 4 
        self.h1q4Point = QComboBox(self)
        self.h1s4Point = QComboBox(self)
        self.h2q4Point = QComboBox(self)
        self.h2s4Point = QComboBox(self)
        self.h3q4Point = QComboBox(self)
        self.h3s4Point = QComboBox(self)

        self.createTeam(4, self.homeLayout, self.h1q4Point, self.h1s4Point, self.h2q4Point,
                        self.h2s4Point, self.h3q4Point, self.h3s4Point)


        #Question 5 
        self.h1q5Point = QComboBox(self)
        self.h1s5Point = QComboBox(self)
        self.h2q5Point = QComboBox(self)
        self.h2s5Point = QComboBox(self)
        self.h3q5Point = QComboBox(self)
        self.h3s5Point = QComboBox(self)

        self.createTeam(5, self.homeLayout, self.h1q5Point, self.h1s5Point, self.h2q5Point,
                        self.h2s5Point, self.h3q5Point, self.h3s5Point)


        #Question 6 
        self.h1q6Point = QComboBox(self)
        self.h1s6Point = QComboBox(self)
        self.h2q6Point = QComboBox(self)
        self.h2s6Point = QComboBox(self)
        self.h3q6Point = QComboBox(self)
        self.h3s6Point = QComboBox(self)

        self.createTeam(6, self.homeLayout, self.h1q6Point, self.h1s6Point, self.h2q6Point,
                        self.h2s6Point, self.h3q6Point, self.h3s6Point)


        #Question 7 
        self.h1q7Point = QComboBox(self)
        self.h1s7Point = QComboBox(self)
        self.h2q7Point = QComboBox(self)
        self.h2s7Point = QComboBox(self)
        self.h3q7Point = QComboBox(self)
        self.h3s7Point = QComboBox(self)

        self.createTeam(7, self.homeLayout, self.h1q7Point, self.h1s7Point, self.h2q7Point,
                        self.h2s7Point, self.h3q7Point, self.h3s7Point)


        #Question 8 
        self.h1q8Point = QComboBox(self)
        self.h1s8Point = QComboBox(self)
        self.h2q8Point = QComboBox(self)
        self.h2s8Point = QComboBox(self)
        self.h3q8Point = QComboBox(self)
        self.h3s8Point = QComboBox(self)

        self.createTeam(8, self.homeLayout, self.h1q8Point, self.h1s8Point, self.h2q8Point,
                        self.h2s8Point, self.h3q8Point, self.h3s8Point)


        #Question 9 
        self.h1q9Point = QComboBox(self)
        self.h1s9Point = QComboBox(self)
        self.h2q9Point = QComboBox(self)
        self.h2s9Point = QComboBox(self)
        self.h3q9Point = QComboBox(self)
        self.h3s9Point = QComboBox(self)

        self.createTeam(9, self.homeLayout, self.h1q9Point, self.h1s9Point, self.h2q9Point,
                        self.h2s9Point, self.h3q9Point, self.h3s9Point)


        #Question 10 
        self.h1q10Point = QComboBox(self)
        self.h1s10Point = QComboBox(self)
        self.h2q10Point = QComboBox(self)
        self.h2s10Point = QComboBox(self)
        self.h3q10Point = QComboBox(self)
        self.h3s10Point = QComboBox(self)

        self.createTeam(10, self.homeLayout, self.h1q10Point, self.h1s10Point, self.h2q10Point,
                        self.h2s10Point, self.h3q10Point, self.h3s10Point)


        #Question 11 
        self.h1q11Point = QComboBox(self)
        self.h1s11Point = QComboBox(self)
        self.h2q11Point = QComboBox(self)
        self.h2s11Point = QComboBox(self)
        self.h3q11Point = QComboBox(self)
        self.h3s11Point = QComboBox(self)

        self.createTeam(11, self.homeLayout, self.h1q11Point, self.h1s11Point, self.h2q11Point,
                        self.h2s11Point, self.h3q11Point, self.h3s11Point)


        #Question 12 
        self.h1q12Point = QComboBox(self)
        self.h1s12Point = QComboBox(self)
        self.h2q12Point = QComboBox(self)
        self.h2s12Point = QComboBox(self)
        self.h3q12Point = QComboBox(self)
        self.h3s12Point = QComboBox(self)

        self.createTeam(12, self.homeLayout, self.h1q12Point, self.h1s12Point, self.h2q12Point,
                        self.h2s12Point, self.h3q12Point, self.h3s12Point)


        #Question 13 
        self.h1q13Point = QComboBox(self)
        self.h1s13Point = QComboBox(self)
        self.h2q13Point = QComboBox(self)
        self.h2s13Point = QComboBox(self)
        self.h3q13Point = QComboBox(self)
        self.h3s13Point = QComboBox(self)

        self.createTeam(13, self.homeLayout, self.h1q13Point, self.h1s13Point, self.h2q13Point,
                        self.h2s13Point, self.h3q13Point, self.h3s13Point)


        #Question 14 
        self.h1q14Point = QComboBox(self)
        self.h1s14Point = QComboBox(self)
        self.h2q14Point = QComboBox(self)
        self.h2s14Point = QComboBox(self)
        self.h3q14Point = QComboBox(self)
        self.h3s14Point = QComboBox(self)

        self.createTeam(14, self.homeLayout, self.h1q14Point, self.h1s14Point, self.h2q14Point,
                        self.h2s14Point, self.h3q14Point, self.h3s14Point)


        #Question 15 
        self.h1q15Point = QComboBox(self)
        self.h1s15Point = QComboBox(self)
        self.h2q15Point = QComboBox(self)
        self.h2s15Point = QComboBox(self)
        self.h3q15Point = QComboBox(self)
        self.h3s15Point = QComboBox(self)

        self.createTeam(15, self.homeLayout, self.h1q15Point, self.h1s15Point, self.h2q15Point,
                        self.h2s15Point, self.h3q15Point, self.h3s15Point)


        #Question 16 
        self.h1q16Point = QComboBox(self)
        self.h1s16Point = QComboBox(self)
        self.h2q16Point = QComboBox(self)
        self.h2s16Point = QComboBox(self)
        self.h3q16Point = QComboBox(self)
        self.h3s16Point = QComboBox(self)

        self.createTeam(16, self.homeLayout, self.h1q16Point, self.h1s16Point, self.h2q16Point,
                        self.h2s16Point, self.h3q16Point, self.h3s16Point)


        #Question 17 
        self.h1q17Point = QComboBox(self)
        self.h1s17Point = QComboBox(self)
        self.h2q17Point = QComboBox(self)
        self.h2s17Point = QComboBox(self)
        self.h3q17Point = QComboBox(self)
        self.h3s17Point = QComboBox(self)

        self.createTeam(17, self.homeLayout, self.h1q17Point, self.h1s17Point, self.h2q17Point,
                        self.h2s17Point, self.h3q17Point, self.h3s17Point)


        #Question 18 
        self.h1q18Point = QComboBox(self)
        self.h1s18Point = QComboBox(self)
        self.h2q18Point = QComboBox(self)
        self.h2s18Point = QComboBox(self)
        self.h3q18Point = QComboBox(self)
        self.h3s18Point = QComboBox(self)

        self.createTeam(18, self.homeLayout, self.h1q18Point, self.h1s18Point, self.h2q18Point,
                        self.h2s18Point, self.h3q18Point, self.h3s18Point)


        #Question 19 
        self.h1q19Point = QComboBox(self)
        self.h1s19Point = QComboBox(self)
        self.h2q19Point = QComboBox(self)
        self.h2s19Point = QComboBox(self)
        self.h3q19Point = QComboBox(self)
        self.h3s19Point = QComboBox(self)

        self.createTeam(19, self.homeLayout, self.h1q19Point, self.h1s19Point, self.h2q19Point,
                        self.h2s19Point, self.h3q19Point, self.h3s19Point)


        #Question 20 
        self.h1q20Point = QComboBox(self)
        self.h1s20Point = QComboBox(self)
        self.h2q20Point = QComboBox(self)
        self.h2s20Point = QComboBox(self)
        self.h3q20Point = QComboBox(self)
        self.h3s20Point = QComboBox(self)

        self.createTeam(20, self.homeLayout, self.h1q20Point, self.h1s20Point, self.h2q20Point,
                        self.h2s20Point, self.h3q20Point, self.h3s20Point)



        #Question ot1 
        self.h1qo1Point = QComboBox(self)
        self.h1so1Point = QComboBox(self)
        self.h2qo1Point = QComboBox(self)
        self.h2so1Point = QComboBox(self)
        self.h3qo1Point = QComboBox(self)
        self.h3so1Point = QComboBox(self)

        self.createTeam(21, self.homeLayout, self.h1qo1Point, self.h1so1Point, self.h2qo1Point,
                        self.h2so1Point, self.h3qo1Point, self.h3so1Point)


        #Question ot2 
        self.h1qo2Point = QComboBox(self)
        self.h1so2Point = QComboBox(self)
        self.h2qo2Point = QComboBox(self)
        self.h2so2Point = QComboBox(self)
        self.h3qo2Point = QComboBox(self)
        self.h3so2Point = QComboBox(self)

        self.createTeam(22, self.homeLayout, self.h1qo2Point, self.h1so2Point, self.h2qo2Point,
                        self.h2so2Point, self.h3qo2Point, self.h3so2Point)


        #Question ot3 
        self.h1qo3Point = QComboBox(self)
        self.h1so3Point = QComboBox(self)
        self.h2qo3Point = QComboBox(self)
        self.h2so3Point = QComboBox(self)
        self.h3qo3Point = QComboBox(self)
        self.h3so3Point = QComboBox(self)

        self.createTeam(23, self.homeLayout, self.h1qo3Point, self.h1so3Point, self.h2qo3Point,
                        self.h2so3Point, self.h3qo3Point, self.h3so3Point)


        self.homeTeam.setLayout(self.homeLayout)

    def createAwayTeam(self):
        self.awayTeam = QGroupBox()
        self.awayLayout = QGridLayout()
        '''
        NAMING CONVENTIONS

        a = Away
        # = seat number or question number (seat number first, then question number
        q = quizzer (main quizzer)
        s = substitute
    
        a#q#Point - Point dropdown for away quizzer at seat # for question #
        a#s#Point - Point dropdown for away sub     at seat # for question #
        '''

        #Question 1 
        self.a1q1Point = QComboBox(self)
        self.a1s1Point = QComboBox(self)
        self.a2q1Point = QComboBox(self)
        self.a2s1Point = QComboBox(self)
        self.a3q1Point = QComboBox(self)
        self.a3s1Point = QComboBox(self)

        self.createTeam(1, self.awayLayout, self.a1q1Point, self.a1s1Point, self.a2q1Point,
                        self.a2s1Point, self.a3q1Point, self.a3s1Point)

        #Question 2 
        self.a1q2Point = QComboBox(self)
        self.a1s2Point = QComboBox(self)
        self.a2q2Point = QComboBox(self)
        self.a2s2Point = QComboBox(self)
        self.a3q2Point = QComboBox(self)
        self.a3s2Point = QComboBox(self)

        self.createTeam(2, self.awayLayout, self.a1q2Point, self.a1s2Point, self.a2q2Point,
                        self.a2s2Point, self.a3q2Point, self.a3s2Point)


        #Question 3 
        self.a1q3Point = QComboBox(self)
        self.a1s3Point = QComboBox(self)
        self.a2q3Point = QComboBox(self)
        self.a2s3Point = QComboBox(self)
        self.a3q3Point = QComboBox(self)
        self.a3s3Point = QComboBox(self)

        self.createTeam(3, self.awayLayout, self.a1q3Point, self.a1s3Point, self.a2q3Point,
                        self.a2s3Point, self.a3q3Point, self.a3s3Point)


        #Question 4 
        self.a1q4Point = QComboBox(self)
        self.a1s4Point = QComboBox(self)
        self.a2q4Point = QComboBox(self)
        self.a2s4Point = QComboBox(self)
        self.a3q4Point = QComboBox(self)
        self.a3s4Point = QComboBox(self)

        self.createTeam(4, self.awayLayout, self.a1q4Point, self.a1s4Point, self.a2q4Point,
                        self.a2s4Point, self.a3q4Point, self.a3s4Point)


        #Question 5 
        self.a1q5Point = QComboBox(self)
        self.a1s5Point = QComboBox(self)
        self.a2q5Point = QComboBox(self)
        self.a2s5Point = QComboBox(self)
        self.a3q5Point = QComboBox(self)
        self.a3s5Point = QComboBox(self)

        self.createTeam(5, self.awayLayout, self.a1q5Point, self.a1s5Point, self.a2q5Point,
                        self.a2s5Point, self.a3q5Point, self.a3s5Point)


        #Question 6 
        self.a1q6Point = QComboBox(self)
        self.a1s6Point = QComboBox(self)
        self.a2q6Point = QComboBox(self)
        self.a2s6Point = QComboBox(self)
        self.a3q6Point = QComboBox(self)
        self.a3s6Point = QComboBox(self)

        self.createTeam(6, self.awayLayout, self.a1q6Point, self.a1s6Point, self.a2q6Point,
                        self.a2s6Point, self.a3q6Point, self.a3s6Point)


        #Question 7 
        self.a1q7Point = QComboBox(self)
        self.a1s7Point = QComboBox(self)
        self.a2q7Point = QComboBox(self)
        self.a2s7Point = QComboBox(self)
        self.a3q7Point = QComboBox(self)
        self.a3s7Point = QComboBox(self)

        self.createTeam(7, self.awayLayout, self.a1q7Point, self.a1s7Point, self.a2q7Point,
                        self.a2s7Point, self.a3q7Point, self.a3s7Point)


        #Question 8 
        self.a1q8Point = QComboBox(self)
        self.a1s8Point = QComboBox(self)
        self.a2q8Point = QComboBox(self)
        self.a2s8Point = QComboBox(self)
        self.a3q8Point = QComboBox(self)
        self.a3s8Point = QComboBox(self)

        self.createTeam(8, self.awayLayout, self.a1q8Point, self.a1s8Point, self.a2q8Point,
                        self.a2s8Point, self.a3q8Point, self.a3s8Point)


        #Question 9 
        self.a1q9Point = QComboBox(self)
        self.a1s9Point = QComboBox(self)
        self.a2q9Point = QComboBox(self)
        self.a2s9Point = QComboBox(self)
        self.a3q9Point = QComboBox(self)
        self.a3s9Point = QComboBox(self)

        self.createTeam(9, self.awayLayout, self.a1q9Point, self.a1s9Point, self.a2q9Point,
                        self.a2s9Point, self.a3q9Point, self.a3s9Point)


        #Question 10 
        self.a1q10Point = QComboBox(self)
        self.a1s10Point = QComboBox(self)
        self.a2q10Point = QComboBox(self)
        self.a2s10Point = QComboBox(self)
        self.a3q10Point = QComboBox(self)
        self.a3s10Point = QComboBox(self)

        self.createTeam(10, self.awayLayout, self.a1q10Point, self.a1s10Point, self.a2q10Point,
                        self.a2s10Point, self.a3q10Point, self.a3s10Point)


        #Question 11 
        self.a1q11Point = QComboBox(self)
        self.a1s11Point = QComboBox(self)
        self.a2q11Point = QComboBox(self)
        self.a2s11Point = QComboBox(self)
        self.a3q11Point = QComboBox(self)
        self.a3s11Point = QComboBox(self)

        self.createTeam(11, self.awayLayout, self.a1q11Point, self.a1s11Point, self.a2q11Point,
                        self.a2s11Point, self.a3q11Point, self.a3s11Point)


        #Question 12 
        self.a1q12Point = QComboBox(self)
        self.a1s12Point = QComboBox(self)
        self.a2q12Point = QComboBox(self)
        self.a2s12Point = QComboBox(self)
        self.a3q12Point = QComboBox(self)
        self.a3s12Point = QComboBox(self)

        self.createTeam(12, self.awayLayout, self.a1q12Point, self.a1s12Point, self.a2q12Point,
                        self.a2s12Point, self.a3q12Point, self.a3s12Point)


        #Question 13 
        self.a1q13Point = QComboBox(self)
        self.a1s13Point = QComboBox(self)
        self.a2q13Point = QComboBox(self)
        self.a2s13Point = QComboBox(self)
        self.a3q13Point = QComboBox(self)
        self.a3s13Point = QComboBox(self)

        self.createTeam(13, self.awayLayout, self.a1q13Point, self.a1s13Point, self.a2q13Point,
                        self.a2s13Point, self.a3q13Point, self.a3s13Point)


        #Question 14 
        self.a1q14Point = QComboBox(self)
        self.a1s14Point = QComboBox(self)
        self.a2q14Point = QComboBox(self)
        self.a2s14Point = QComboBox(self)
        self.a3q14Point = QComboBox(self)
        self.a3s14Point = QComboBox(self)

        self.createTeam(14, self.awayLayout, self.a1q14Point, self.a1s14Point, self.a2q14Point,
                        self.a2s14Point, self.a3q14Point, self.a3s14Point)


        #Question 15 
        self.a1q15Point = QComboBox(self)
        self.a1s15Point = QComboBox(self)
        self.a2q15Point = QComboBox(self)
        self.a2s15Point = QComboBox(self)
        self.a3q15Point = QComboBox(self)
        self.a3s15Point = QComboBox(self)

        self.createTeam(15, self.awayLayout, self.a1q15Point, self.a1s15Point, self.a2q15Point,
                        self.a2s15Point, self.a3q15Point, self.a3s15Point)


        #Question 16 
        self.a1q16Point = QComboBox(self)
        self.a1s16Point = QComboBox(self)
        self.a2q16Point = QComboBox(self)
        self.a2s16Point = QComboBox(self)
        self.a3q16Point = QComboBox(self)
        self.a3s16Point = QComboBox(self)

        self.createTeam(16, self.awayLayout, self.a1q16Point, self.a1s16Point, self.a2q16Point,
                        self.a2s16Point, self.a3q16Point, self.a3s16Point)


        #Question 17 
        self.a1q17Point = QComboBox(self)
        self.a1s17Point = QComboBox(self)
        self.a2q17Point = QComboBox(self)
        self.a2s17Point = QComboBox(self)
        self.a3q17Point = QComboBox(self)
        self.a3s17Point = QComboBox(self)

        self.createTeam(17, self.awayLayout, self.a1q17Point, self.a1s17Point, self.a2q17Point,
                        self.a2s17Point, self.a3q17Point, self.a3s17Point)


        #Question 18 
        self.a1q18Point = QComboBox(self)
        self.a1s18Point = QComboBox(self)
        self.a2q18Point = QComboBox(self)
        self.a2s18Point = QComboBox(self)
        self.a3q18Point = QComboBox(self)
        self.a3s18Point = QComboBox(self)

        self.createTeam(18, self.awayLayout, self.a1q18Point, self.a1s18Point, self.a2q18Point,
                        self.a2s18Point, self.a3q18Point, self.a3s18Point)


        #Question 19 
        self.a1q19Point = QComboBox(self)
        self.a1s19Point = QComboBox(self)
        self.a2q19Point = QComboBox(self)
        self.a2s19Point = QComboBox(self)
        self.a3q19Point = QComboBox(self)
        self.a3s19Point = QComboBox(self)

        self.createTeam(19, self.awayLayout, self.a1q19Point, self.a1s19Point, self.a2q19Point,
                        self.a2s19Point, self.a3q19Point, self.a3s19Point)


        #Question 20 
        self.a1q20Point = QComboBox(self)
        self.a1s20Point = QComboBox(self)
        self.a2q20Point = QComboBox(self)
        self.a2s20Point = QComboBox(self)
        self.a3q20Point = QComboBox(self)
        self.a3s20Point = QComboBox(self)

        self.createTeam(20, self.awayLayout, self.a1q20Point, self.a1s20Point, self.a2q20Point,
                        self.a2s20Point, self.a3q20Point, self.a3s20Point)



        #Question ot1 
        self.a1qo1Point = QComboBox(self)
        self.a1so1Point = QComboBox(self)
        self.a2qo1Point = QComboBox(self)
        self.a2so1Point = QComboBox(self)
        self.a3qo1Point = QComboBox(self)
        self.a3so1Point = QComboBox(self)

        self.createTeam(21, self.awayLayout, self.a1qo1Point, self.a1so1Point, self.a2qo1Point,
                        self.a2so1Point, self.a3qo1Point, self.a3so1Point)


        #Question ot2 
        self.a1qo2Point = QComboBox(self)
        self.a1so2Point = QComboBox(self)
        self.a2qo2Point = QComboBox(self)
        self.a2so2Point = QComboBox(self)
        self.a3qo2Point = QComboBox(self)
        self.a3so2Point = QComboBox(self)

        self.createTeam(22, self.awayLayout, self.a1qo2Point, self.a1so2Point, self.a2qo2Point,
                        self.a2so2Point, self.a3qo2Point, self.a3so2Point)


        #Question ot3 
        self.a1qo3Point = QComboBox(self)
        self.a1so3Point = QComboBox(self)
        self.a2qo3Point = QComboBox(self)
        self.a2so3Point = QComboBox(self)
        self.a3qo3Point = QComboBox(self)
        self.a3so3Point = QComboBox(self)

        self.createTeam(23, self.awayLayout, self.a1qo3Point, self.a1so3Point, self.a2qo3Point,
                        self.a2so3Point, self.a3qo3Point, self.a3so3Point)


        self.awayTeam.setLayout(self.awayLayout)


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
        else:
            qPoint.setAlignment(Qt.AlignCenter)
        
        qType.addItems(types)
        qPart.addItems(parts)
        
        qLabel.setFixedWidth(55)
        qLabel.setAlignment(Qt.AlignCenter)
        qPoint.setFixedWidth(55)
        qType.setFixedWidth(55)
        qPart.setFixedWidth(55)
        qNote.setFixedWidth(55)

        #add widgets to layout
        self.scoreLayout.addWidget(qLabel, 1, position)                          
        self.scoreLayout.addWidget(qPoint, 2, position)
        self.scoreLayout.addWidget(qType,  3, position)
        self.scoreLayout.addWidget(qPart,  4, position)
        self.scoreLayout.addWidget(qNote,  5, position)

    def createTeam(self, position, layout, t1q, t1s, t2q, t2s, t3q, t3s):
        if position > 20:
            points = [" ", "10", "-5"]
        else:
            points = [" ", "+", "-"]
        t1q.addItems(points)
        t1s.addItems(points)
        t2q.addItems(points)
        t2s.addItems(points)
        t3q.addItems(points)
        t3s.addItems(points)

        t1q.setFixedWidth(55)
        t1s.setFixedWidth(55)
        t2q.setFixedWidth(55)
        t2s.setFixedWidth(55)
        t3q.setFixedWidth(55)
        t3s.setFixedWidth(55)

        layout.addWidget(t1q, 1, position)
        layout.addWidget(t1s, 2, position)
        layout.addWidget(t2q, 3, position)
        layout.addWidget(t2s, 4, position)
        layout.addWidget(t3q, 5, position)
        layout.addWidget(t3s, 6, position)
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scoresheet()
    sys.exit(app.exec_())
