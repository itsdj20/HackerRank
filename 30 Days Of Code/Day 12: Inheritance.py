class Student(Person, object):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        iAvg = sum(self.scores)/len(self.scores)
        return 'O' if iAvg > 89 else 'E' if iAvg > 79 else 'A' if iAvg > 69 else 'P' if iAvg > 54 else 'D' if iAvg > 39 else 'T'
