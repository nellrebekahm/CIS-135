# # # # 1
# # #
# #
# counts = [0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(length):
#     for i in range(width):
#         print('0', end='  ')
#     print()
# -------

# counts = ['0 0 0 0 0 0 0 0', '0 0 0 0 0 0 0 0', '0 0 0 0 0 0 0 0', '0 0 0 0 0 0 0 0', '0 0 0 0 0 0 0 0',
#           '0 0 0 0 0 0 0 0', '0 0 0 0 0 0 0 0', '0 0 0 0 0 0 0 0']
# length = len(counts)
# i = 3
#
# while i < length:
#     print(counts[i])
#     i += 1
# # --------------------------------
#
# counts = [0, 0, 0, 0, 0, 0, 0, 0]
# length = len(counts)
#
# i = 3
#
# while i < length:
#     print(counts)
#     i += 1

# # ---------------------------------
# 2
# names = ["Tony", "Steve", "Natasha", "Thor", "Clint", "Bruce", "Wanda", "Peter", "Stephen", "Bucky"]
#
# length = len(names)
# i = 0
#
# while i < length:
#     print(names[i])
#     i += 1
# ----------------------------------
# test_list = [6, 4, 8, 9, 10]
#
# print("The original list : " + str(test_list))
#
# try:
#     test_list.index(11)
#     res = "Element found"
# except ValueError:
#     res = "Element not in list !"
#
# print("The value after catching error : " + str(res))
#
# ---------
test_list = ['1', '2', '3', '4', '5']
num = str(input('Enter a number: '))

try:
    test_list.index(num)
    print("This number is already in the list.")
except ValueError:
    print("Error")
# ------------------------------
