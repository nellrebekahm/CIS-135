# Rebecca Nell
# CIS 135
# error_handling_nell.py
# Script 26


# Create a function named causeSyntaxError with a mangled print statement.
def causeSyntaxError():
    # print "This Syntax Error is included as an example."
    return


# Create a function named runLogicError that attempts to divide a number by zero.
def runLogicError():
    x = 1/0
    return


# Create a function named runFileError that attempts to open a file that does not exist.
def runFileError():
    with open('file_does_not_exist', 'r') as f:
        read_data = f.read()
    return


# Create a function named generateErrors that first calls runLogicError()
# and then calls runFileError().
def generateErrors():
    runLogicError()
    runFileError()
    return


# Create a function named handleErrors that uses
# try-catch blocks to properly handle the errors thrown by runLogicError().
def handleErrors():
    try:
        try:
            runLogicError()
        except ZeroDivisionError as err:
            print('Now handling:', err)
        try:
            runFileError()
        except(OSError, FileNotFoundError) as err:
            print('Now Handling:', err)
    finally:
        print('Finally all the errors are handled!')


# generateErrors()
handleErrors()