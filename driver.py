# Rebecca_Nell
# CIS 135
# driver.py
# Week 13 Assignment


# Electronics, Computer, and Phone child class imports
from electronics import Electronics
from computer import Computer
from phone import Phone


# this step prompts the user to input electronic device's brand name
# creates electronics object
electronicsBrand = input("\nEnter an electronics brand name: ")
electronicsObject = Electronics(electronicsBrand)


# this step prompts the user to enter computer's brand name and operating system
# creates computer object
computerBrand = input("\nEnter a computer brand name: ")
computerOperatingSystem = input("Enter a computer operating system: ")
computerObject = Computer(computerBrand, computerOperatingSystem)


# this step prompts the user to enter the phone's brand name, operating system, and number
# creates phone object
phoneBrand = input("\nEnter a phone brand name: ")
phoneOperatingSystem = input("Enter a phone operating system: ")
phoneNumber = input("Enter a phone number: ")
phoneObject = Phone(phoneBrand, phoneOperatingSystem, phoneNumber)


# this step prints the electronic device's brand name
print("\n\nThe Electronics Object:")
print("Brand name: " + electronicsObject.get_brand_name())

# this step prints the computer's brand name and operating system
print("\nThe Computer Object:")
print("Brand Name: " + computerObject.get_brand_name())
print("Operating System: " + computerObject.get_operating_system())

# this step prints the phone's brand name, operating system, and number
print("\nThe Phone Object:")
print("Brand Name: " + phoneObject.get_brand_name())
print("Operating System: " + phoneObject.get_operating_system())
print("Phone Number: " + phoneObject.get_phone_number())

