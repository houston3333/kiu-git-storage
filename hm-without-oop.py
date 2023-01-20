student1 = {
    'degree': 'bachelor',
    'fullname': 'GGI', 
    'groupnumber': 1011, 
    'average_score': 4.5 , 
    'scholarship': None
}


def bachelor(average_score):
    if average_score == 5:
        return 3000
    elif 4 < average_score < 5:
        return 2000
    elif 3 < average_score < 4:
        return 1500


def graduate(average_score):
    if average_score == 5:
        return 5000
    elif 4 < average_score < 5:
        return 4500
    elif 3 < average_score < 4:
        return 3500


def student(student):
    if student['degree'] == 'bachelor':
        student['scholarship'] = bachelor(student['average_score'])
        return student
    if student['degree'] == 'graduate':
        student['scholarship'] = graduate(student['average_score'])
        return student


print(student(student1))
