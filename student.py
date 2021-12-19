# Rebecca Nell
# CIS 135
# nell_final.py


# Student class which stores the student information enter by the user
class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        return

    def print_student(self):
        print(f'{self.first_name.title()} {self.last_name.title()} {self.student_id.upper():>20}')
        return

# Class class which stores student class information entered by the user
class Class:
    def __init__(self, class_name, class_grade):
        self.class_name = class_name
        self.class_grade = class_grade

    def add_class(self):
        print(f'{self.class_name.upper()} {self.class_grade.upper()}')
        return

# function to calculate student GPA
def compute_gpa():
    get_GPA = 0
    # if get_class_grade == 'A':
    #     get_GPA += 4
    # elif get_class_grade == 'B':
    #     get_GPA += 3
    # elif get_class_grade == 'C':
    #     get_GPA += 2
    # elif get_class_grade == 'D':
    #     get_GPA += 1
    # elif get_class_grade == 'F':
    #     get_GPA += 0
    # else:
    #     'This letter grade does not exist, please try again.'


