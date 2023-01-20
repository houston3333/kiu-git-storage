class Student:
    def __init__(self, fullname, groupnumber, average_score):
        self.fullname = fullname
        self.groupnumber = groupnumber
        self.average_score = average_score

        def __str__(self):
            return f'fullname: {self.name}, groupnumber: {self.groupnumber}, average_score: {self.average_score}, scholarship: {self.scholarship}'


class Bachelor(Student):
    def __init__(self, fullname, groupnumber, average_score):
        super().__init__(fullname, groupnumber, average_score)
        self.scholarship()

    def scholarship(self):
        average_score = self.average_score
        if average_score == 5:
            self.scholarship = 3000
        elif 4 < average_score < 5:
            self.scholarship = 2000
        elif 3 < average_score < 4:
            self.scholarship = 1500


class Graduate(Student):
    def __init__(self, fullname, groupnumber, average_score):
        super().__init__(fullname, groupnumber, average_score)
        self.scholarship()

    def scholarship(self):
        average_score = self.average_score
        if average_score == 5:
            self.scholarship = 5000
        elif 4 < average_score < 5:
            self.scholarship = 4500
        elif 3 < average_score < 4:
            self.scholarship = 3500




