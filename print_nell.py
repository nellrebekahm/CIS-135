# Rebecca Nell
# print_nell.py
# CIS-135
# Assignment #6

hw = str("hello world")  # hw is a string reading Hello World
countdown = 0.12345  # countdown is a numeric variable equaling 0.12345
print(hw)  # hello world will print on line one
print(countdown)  # countdown value will print on line two

print("")  # empty line between text

print("The value of hw is {}.".format(hw))  # "The value of hw is hello world." will print to the screen

print("")  # empty line between text

print("The value of countdown is", f"{countdown:.5f}")
print("The value of countdown is", f"{countdown:.4f}")
print("The value of countdown is", f"{countdown:.3f}")
print("The value of countdown is", f"{countdown:.2f}")
print("The value of countdown is", f"{countdown:.1f}")
print("The value of countdown is", f"{countdown:.0f}")
# the values for countdown will print in descending order on separate lines

print("")  # empty line between text

print(hw + ", the value of countdown is", f"{countdown:.2f}")
# the text "hello world, the value of countdown is 0.12" will print to screen
