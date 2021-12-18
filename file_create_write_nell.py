# Rebecca Nell
# CIS 135
# file_create_write_nell.py
# Script #22


# function to create a file
def createFile(file_name):
    create_new = open(file_name, "x")
    create_new.close()
    return


# function to write data for the file
def writeData(file_name):
    write_data = open(file_name, "wt")
    write_data.write("Steps to file management:\r")
    write_data.write("\t1: Open a file.\r")
    write_data.write("\t2: Read or write data.\r")
    write_data.write("\t3: Close the file.\r")
    write_data.close()
    return


# function to print the data to the file
def printData(file_name):
    print_file = open(file_name, 'r')
    for line in print_file:
        print(line)
    print_file.close()
    return


# function to execute previous functions and name the file created
def main():
    file_name = "create_this_file.txt"
    createFile(file_name)
    writeData(file_name)
    printData(file_name)
    return


main()