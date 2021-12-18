# Rebecca Nell
# CIS 135
# nested_loops_nell.py
# Script #20

# function to create a loop that counts up inside of another loop which also counts up
def incrementLoop():
    outer_counter = 1
    while outer_counter <= 3:
        inner_counter = 1
        while inner_counter <= 3:
            print(f'\tOuter Counter {outer_counter}, Inner Counter {inner_counter}')
            inner_counter += 1
        outer_counter += 1
    return


print("\nCounting Up with Nested Loops")
incrementLoop()


# function to create a loop that counts down inside of another loop which also counts down
def decrementLoop():
    outer_counter = 3
    while outer_counter > 0:
        inner_counter = 3
        while inner_counter > 0:
            print(f'\tOuter Counter {outer_counter}, Inner Counter {inner_counter}')
            inner_counter -= 1
        outer_counter -= 1
    return


print("\nCounting Down with Nested Loops")
decrementLoop()


# import required library to use time.sleep()
import time


# function to run a loop inside of a loop that counts up in incrementally by 1 second
# displays in a stopwatch layout 00:00
def stopWatch():
    second, minute = 60, -1
    while second == 60:
        second = 0
        if minute == -1:
            minute = 0
        else:
            minute += 1
        while second <= 59:
            if second <= 9:
                print(f'Timer : {minute}:0{second}')
            else:
                print(f'Timer : {minute}:{second}')
            time.sleep(1)
            second += 1
    return


stopWatch()
