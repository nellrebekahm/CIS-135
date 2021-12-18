# Rebecca Nell
# CIS 135
# nell_final.py


class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.classes_completed = {}

        return

    def print_student(self):
        print(f'{self.first_name.title()} {self.last_name.title()} {self.student_id.upper():>20}')
        return

    def add_class(self):
        class_name = input('Enter class name: ')
        grade = input('Enter letter grade received: ')

        return

    # def compute_gpa(self):
    #     grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}




# class Grade:
#     def __init__(self, class_name, grade):
#         self.class_name = class_name
#         self.grade = grade
#         return
#
#     def classes_completed(self):
#         print(f'{self.class_name.title()} {self.grade}')
#         return
#



#
# fn = 'rebecca'
# ln = 'nell'
# s_id = '123456'
# new_student = Student(fn, ln, s_id)
# print(type(new_student))
# new_student.print_student()

