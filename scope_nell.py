# Rebecca Nell
# CIS 135
# scope_nell.py
# Assignment #12
# this script includes an intentional error message required for the third point on the rubric


# first function to set Flynn's age when inside the grid
def enterGrid(flynnAge):
    flynnAge = flynnAge + 20
    print("\tFlynn's age in the grid is", flynnAge)
    return


# printout demonstrating variable flynnAge outside of the function and inside of the function
flynnAge = 27
print("\nFlynn's age before calling enterGrid = %g" % flynnAge)
enterGrid(flynnAge)
print("Flynn's age after calling enterGrid = %g" % flynnAge)


# function getName with variable lastISO
def getName(lastISO):
    userName = lastISO
    print("\tOriginal userName inside getName =", userName)
    userName = "Quorra"
    print('\tUpdated userName insider getName =', userName)
    return userName


lastISO = "unknown"
print("\nThe original value of lastISO is %s" % lastISO)
lastISO = getName(lastISO)
print("The value of lastISO is now %s" % lastISO)


# final rubric point: add the following lines of code to your script
# study to resulting error message
print()
lastISO = "unknown"
print("\nThe original value of lastISO is %s" % lastISO)
lastISO = getName(lastISO)
print("The value of lastISO is now %s" % lastISO)
print("The value of username is %s" % userName)
