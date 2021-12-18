# Rebecca Nell
# CIS 135
# if_else_nell.py
# Assignment #8




print()

# prompts user to type either y or n
yesNo1 = input("Hello user, please enter either 'y' or 'n': ")

# evaluates user data and responds accordingly
if yesNo1 == 'y' or yesNo1 == 'Y':
    print("The response was 'y'")
elif yesNo1 == 'n' or yesNo1 == 'N':
    print("The response was not 'y'")
else:
    print("The response was neither 'y' or 'n'")