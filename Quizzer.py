
class Quizzer(QWidget):
    def __init__(self):
        super().__init__()

        self.score        = 0
        self.canQO        = True
        self.right        = 0
        self.wrong        = 0
        self.isQO         = False
        self.fouls        = 0
        self.toQO         = 5
        self.percRight    = 0
        self.tenMissed    = 0
        self.twentyMissed = 0
        self.thirtyMissed = 0
