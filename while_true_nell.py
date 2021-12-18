# Rebecca Nell
# CIS 135
# while_true_nell.py
# Assignment #9




# Loop 1: traditional while loop
print()
print("Loop 1:")

while_yes = 'y'

while while_yes == 'y' or while_yes == 'Y':
    while_yes = input("Please enter 'y' to continue. Enter any other response to exit: ")


# Loop 2: while-not-some-boolean-value loop
print()
print("Loop 2:")

while_true = True
while while_true:
    t_f = str(input("Please enter 'y' to continue. Enter any other response to exit: "))
    if t_f == 'y' or t_f == 'Y':
        pass
    elif t_f != 'y' or t_f != 'Y':
        while_true = False


# Loop 3: while True loop that continuously runs as long as a user does not input the response 'y'
print()
print("Loop 3:")

while_true = False
while not while_true:
    t_f = str(input("Please enter any response to continue. Enter 'y' to exit: "))
    if t_f == 'y' or t_f == 'Y':
        while_true = True
    else:
        while_true = False



# Loop 4: while False loop that runs as long as a user inputs the response 'y'
print()
print("Loop 4:")

while_false = False
while not while_false:
    t_f = str(input("Please enter 'y' continue. Enter any other response to exit: "))
    if t_f == 'y' or t_f == 'Y':
        while_false = False
    else:
        while_false = True

