# Rebecca Nell
# CIS 135
# student_class_nell.py
# Script #29

# imported data from person_object_nell
from person_object_nell import Person
import datetime


# student class with data extracted from person_object_nell
class Student(Person):
    year = datetime.datetime.now()

    def __init__(self, first_name, last_name, favorite_food):
        super().__init__(first_name, last_name, favorite_food)
        self.year_started = self.year.strftime("%Y")
        self.class_list = {}

    def run_report(self):
        print(f'\n\tStudent Name: \t{self.first_name.title()} {self.last_name.title()}')
        print(f'\tYear Started: \t{self.year_started}')
        print(f'\tClass List:')
        course_keys = self.class_list.keys()
        for course in course_keys:
            print(f'\t\t {course}: {self.class_list[course]}')
        print(f'\tEnd of report for student: {self.last_name.title()}')
        return


# fn = 'clinton'
# ln = 'garwood'
# ff = ''
# test_student = Student(fn, ln, ff)
# test_student.run_report()