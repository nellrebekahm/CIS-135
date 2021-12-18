# Rebecca Nell
# CIS 135
# sum_total_nell.py
# Assignment #14


# Simple Implementation
def askAgain():
    get_input = 1
    sub_total = 0
    while get_input != 0:
        get_input = int(input("\tPlease enter a number, or enter 0 (zero) to exit: "))
        sub_total += get_input
        print("\tGrand total so far = : ", sub_total)
    return sub_total


print("\nWelcome to the Sum-Total Python App")
grand_total = askAgain()
print("The grand total is ", grand_total)


# Advanced Implementation
def askAgain():
    get_input = 1
    sub_total = 0
    loop_counter = 0
    while get_input != 0:
        get_input = int(input("\tPlease enter a number, or enter 0 (zero) to exit: "))
        sub_total += get_input
        loop_counter += 1
        print("\tLoop count: ", loop_counter, "Running grand total so far: ", sub_total)
    return loop_counter, sub_total


print("\nWelcome to the Advanced Sum-Total Python App")
count_loop, grand_total = askAgain()
print("The loop ran", count_loop, "times, with a grand total of", grand_total)
