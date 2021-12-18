# Rebecca Nell
# CIS 135
# parallel_data_nell.py
# Script #18


# color matrix with colors and values
colors = ["Red", "Yellow", "Lime", "Blue", "Aqua", "Fuchsia", "Silver", "Gray", "Maroon", "Olive", "Green", "Purple",
          "Teal", "Navy"]
red_code = [255, 255, 1, 1, 1, 255, 192, 128, 128, 128, 1, 128, 1, 1]
green_code = [1, 255, 255, 1, 255, 1, 192, 128, 1, 128, 128, 1, 128, 1]
blue_code = [1, 1, 1, 255, 255, 255, 192, 128, 1, 1, 1, 128, 128, 128]


# function with loop that will output color names as well as corresponding r-g-b data
def allColors(c, r, g, b):
    count = 0
    for each in c:
        print("The rgb color values for %s are red = '%d', green = '%d', blue = '%d'" % (
        c[count], r[count], g[count], b[count]))
        count += 1
    return


allColors(colors, red_code, green_code, blue_code)


# function prompts user to search color information
def askColor(cr, rc, gc, bc):
    getColor = input("\nWhat color would you like  to look up? ")
    if getColor in cr:
        spot_is = cr.index(getColor)
        print("The rgb color values for %s are red= '%d', green= '%d', blue= '%d" % (
        cr[spot_is], rc[spot_is], gc[spot_is], bc[spot_is]))
    return


askColor(colors, red_code, green_code, blue_code)


# function to allow color values entered by user to be recognized with or without capitalization
# function also gives command to exit loop using the keyword: 'exit'
def askColors(cr, rc, gc, bc):
    go = ''
    while go != 'exit':
        getColor = input("What color would you like to look up? ")
        if getColor.capitalize() in cr:
            spot_is = cr.index(getColor.capitalize())
            print("The rgb color values for %s are red= '%d', green= '%d', blue= '%d'" % (
            cr[spot_is], rc[spot_is], gc[spot_is], bc[spot_is]))
        else:
            print("Sorry, %s was not found in the collection." % (getColor.capitalize()))
        go = input("Press 'y' to search for another color or type 'exit' to exit.")
    return


askColors(colors, red_code, green_code, blue_code)
