# Rebecca Nell
# CIS 135
# calculate_nell.py
# Assignment #13


# addition function
def addTwo():
    numOne = int(input("\tPlease enter the first number to add: "))
    numTwo = int(input("\tPlease enter the second number to add: "))
    sum = numOne + numTwo
    print("\tAdding: %d + %d = %d" % (numOne, numTwo, sum))
    input("\tPress enter to continue... \n")
    return


# subtraction function
def subtractTwo():
    numOne = int(input("\tPlease enter the first number to subtract: "))
    numTwo = int(input("\tPlease enter the second number to subtract: "))
    difference = numOne - numTwo
    print("\tSubtracting: %d - %d = %d" % (numOne, numTwo, difference))
    input("\tPress enter to continue... \n")
    return


# multiplication function
def productTwo():
    numOne = int(input("\tPlease enter the first number to multiply: "))
    numTwo = int(input("\tPlease enter the second number to multiply: "))
    product = numOne * numTwo
    print("\tMultiplying: %d x %d = %d" % (numOne, numTwo, product))
    input("\tPress enter to continue... \n")
    return


# division function
def divideTwo():
    numOne = int(input("\tPlease enter a number for the numerator: "))
    numTwo = int(input("\tPlease enter a number for the denominator: "))
    quotient = numOne / numTwo
    print("\tDividing %d %% %d = %d" % (numOne, numTwo, quotient))
    input("\tPress enter to continue... \n")
    return


# while loop for selecting which function the calculator should run
selection = 10
while selection != 0:
    print("\nGreetings! Welcome to the Python Calculator")
    print("Please make a selection from the menu below:")
    print("\tEnter 1) Addition\n \tEnter 2) Subtraction\n \tEnter 3) Division\n \tEnter 4) Multiplication")
    print("\t\tEnter 0 (zero) to exit")
    selection = int(input("Please make your selection: "))
    if selection == 1:
        addTwo()
    elif selection == 2:
        subtractTwo()
    elif selection == 3:
        divideTwo()
    elif selection == 4:
        productTwo()
    elif selection == 0:
        print("\nGoodbye")
    else:
        print("Your input is not valid. Please try again.")
