# Rebecca Nell
# CIS 135
# counter_nell.py
# Assignment #10


# prints counter value with each loop cycle
print()
control_variable_1 = 'y'
counter_1 = 0
while control_variable_1 == 'y' or control_variable_1 == 'Y':
    counter_1 = counter_1 + 1
    control_variable_1 = input("Counter1 = %d \nEnter 'y' to continue: " % counter_1)



# prints counter value with each loop cycle
# late update on counter value, final value of counter is equal to last cycle value
print()
control_variable_2 = 'y'
counter_2 = 0

while control_variable_2 == 'y' or control_variable_2 == 'Y':
    counter_2 = counter_2 + 1
    control_variable_2 = input("Counter2 = %d \nEnter 'y' to continue: " % counter_2)

print("Counter2 Total =", counter_2)


# while loop to print the values counting up from 1 to 10
print()
count_up = 1

while count_up < 11:
    print("Counter3 =", count_up)
    count_up = count_up + 1


# while loop to print the values counting down from 10 to 1
print()
count_down = 10

while count_down > 0:
    print("Counter4 =", count_down)
    count_down = count_down - 1
