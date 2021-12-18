# Rebecca Nell
# CIS 135
# named_lists_nell.py
# Script #16


# Establish a Python list named py_list and print list to the screen
py_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(py_list)
print()


# Create and call a function that contains a for-loop that will access data in the list
# Print each piece of data found to the screen
def printList(py_list):
    for each in py_list:
        # print("Found", each, "in py_list")
        print(f"Found {each} in py_list")
    return


print("First call to printList")
printList(py_list)


# Declare a function with a modified for-loop to iterate through the list, double each item (x2)
# Return the list to the caller at the end of the function
def updateList(py_list):
    for count, value in enumerate(py_list):
        py_list[count] = value * 2
    return py_list


py_list = updateList(py_list)
print()


# Call the printList function again, printing out the values in the list
print("Final call to printList")
printList(py_list)