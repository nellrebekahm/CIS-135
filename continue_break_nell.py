# Rebecca Nell
# CIS 135
# continue_break_nell.py
# Script #21


# function that implements a break statement with a for-range loop
# prints numbers 1 to 10, breaks at 5
def breakOut():
    print("\t\tInside breakOut function")
    for x in range(1, 11):
        if x == 5:
            break
        else:
            print(f'\t\t{x}')
    return


# function that implements a continue statement in a for-range loop
# prints numbers 1 to 10, skips printing 5
def continueOn():
    print("\t\tInside continueOn function")
    for x in range(1, 11):
        if x == 5:
            continue
        else:
            print(f'\t\t{x}')
    return


# function that simply implements the pass keyword as a
# placeholder for code in the function
def easyPass():
    print("\t\tInside easyPass function")
    pass
    return


# function which displays a menu for the user to call the other
# functions described above as many times as they like with option to exit
def mainMenu():
    selection = 0
    while selection != 4:
        print("\nWelcome to break, continue, pass function caller.")
        print("\tOption 1: Run Break Function")
        print("\tOption 2: Run Continue Function")
        print("\tOption 3: Run Pass Function")
        print("\tOption 4: Exit")
        selection = int(input("\nPLease make a selection from the menu: "))
        if selection == 1:
            breakOut()
        elif selection == 2:
            continueOn()
        elif selection == 3:
            easyPass()
    return


mainMenu()