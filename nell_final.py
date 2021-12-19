# Rebecca Nell
# CIS 135
# nell_final.py

# imported data from student.py
import student


# function to display and navigate main menu
def print_main_menu():
    print('\n\t\t Main Menu \n1) Print a List of All Students \n2) Add a New Student \n3) Manage a Student Record '
          '\n4) Exit the '
          'Program')


# main menu option 1: prints the student directory
def print_all_students(all_students):
    print('\n\t\t Student Directory')
    for each in all_students:
        each.print_student()
    return


# main menu option 2: prompts the user to enter student information and creates a new entry in the directory if
# student doesn't already exist
def create_new_student(students):
    print('\nAdd a New Student')
    get_first_name = input('Please enter the student\'s first name: ')
    get_last_name = input('Please enter the student\'s last name: ')
    get_student_id = input('Please enter the student\'s number: ')
    if select_student_by_id(students, get_student_id) is None:
        new_student = student.Student(get_first_name, get_last_name, get_student_id)
        students.append(new_student)
    else:
        print("Student Exists Already")

    return students


# main menu option 3: displays a menu which allows the user to further edit previous student entries
def print_student_menu():
    print('\n\t\t Student Menu \n1) Add a Class to a Student Record \n2) Print an Individual Student Record \n3) '
          'Exit '
          'Student Menu')


# student menu option 1: asks the user to enter the student ID which they would like to edit, then pulls up the
# student associated with that ID and allows the user to add classes taken and grades received
def add_class_for_student(classes):
    student_ID_search = input('Please enter the ID of the student you wish to search: ')
    if select_student_by_id(classes, student_ID_search) is not None:
        get_class_name = input('\nEnter class name: ')
        get_class_grade = input('Enter letter grade received: ')
        new_class = student.Class(get_class_name, get_class_grade)
        classes.append(new_class)
        return
    else:
        print('Student not found. Please try again.')
    return classes


# student menu option 2: prompts the user to enter the student ID which they would like to view, then displays all of
# the information that the user has entered for the student
def print_student_record(classes_completed):
    print('\n\t\t Student Classes')
    for each in classes_completed:
        each.add_class()
    return


# this function allows the user to search for a specific student and their information by entering their ID number
def select_student_by_id(students, studentID):
    for student in students:
        if studentID == student.student_id:
            return student

    return None


# main program function
def main():
    all_students = []
    classes_completed = []
    main_menu_selection = 0
    student_menu_selection = 0

    while main_menu_selection != '4':
        print_main_menu()
        selection = input('\nPlease select a menu option: ')
        if selection == '1':
            print_all_students(all_students)
        elif selection == '2':
            all_students = create_new_student(all_students)
        elif selection == '3':
            while student_menu_selection != '3':
                print_student_menu()
                selection = input('\nPlease select a menu option: ')
                if selection == '1':
                    add_class_for_student(all_students)
                elif selection == '2':
                    print_student_record(classes_completed)
                elif selection == '3':
                    print_main_menu()
                    break
        elif selection == '4':
            exit()
        else:
            print('\nThat is not a valid selection, please try again.')


main()