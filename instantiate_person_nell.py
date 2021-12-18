# Rebecca Nell
# CIS 135
# instantiate_person_nell.py
# Assignment #28


# class imported from file person_object_nell.py
import person_object_nell


# directory
person_directory = []


# function to add a person to the directory
def addPerson():
    print("\nAdd a New Person")
    first = input("Please enter the person's first name: ")
    last = input("Please enter the person's last name: ")
    food = input("Please enter the person's favorite food: ")
    new_person = person_object_nell.Person(first,last,food)
    person_directory.append(new_person)
    print(f'New entry added to the directory.')
    new_person.personal_traits()
    return


# function to remove a person from the directory
def removePerson():
    print("\n\tRemove an entry from the directory ")
    last = input("\tPLese enter the person's last name: ")
    for each in person_directory:
        if last.lower() == each.last_name.lower():
            person_directory.remove(each)
    printDirectory()
    return


# function to print the directory
def printDirectory():
    print("\nThe entries currently in the directory are:")
    for each in person_directory:
        each.personal_traits()
    return


# function to display the options menu
def displayMenu():
    stop_loop = 0
    while stop_loop != 4:
        print("\n1) Add a Person to the directory")
        print("2) Remove a Person from the directory")
        print("3) Print out the entire directory")
        print("4) Exit")
        stop_loop = int(input("Please select an option: "))
        if stop_loop == 1:
            addPerson()
        elif stop_loop == 2:
            removePerson()
        elif stop_loop == 3:
            printDirectory()
    return


displayMenu()