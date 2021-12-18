# Rebecca Nell
# CIS 135
# file_update_nell.py
# Script #23


# function to count the number of existing lines in the file
def countLines(file_name):
    get_count = 0
    count_file = open(file_name, 'r')
    for line in count_file:
        get_count += 1
    count_file.close()
    return get_count


# function to append the new data to the existing file
def appendFile(file_name, original_count):
    write_data = open(file_name, 'a')
    write_data.write(f'{file_name} had {original_count} lines of data, and now has {original_count + 1}\r')
    write_data.close()
    return


# function to confirm the data appended to the file
def confirmAppend(file_name):
    print_file = open(file_name, 'r')
    for line in print_file:
        print(line)
    print_file.close()
    return


# function to cap additional data at 10 total lines
def appendToTen():
    update_counter = 0
    file_name = 'create_this_file.txt'
    while update_counter < 9:
        update_counter = countLines(file_name)
        appendFile(file_name, update_counter)
    confirmAppend(file_name)
    return


appendToTen()
