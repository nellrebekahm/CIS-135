# Rebecca_Nell
# CIS 135
# phone.py
# Week 13 Assignment

# import of Computer child class
from computer import Computer


# Phone class defined and extends from Computer class
class Phone(Computer):
    def __init__(self, brandName, operatingSystem, phoneNumber):
        super().__init__(brandName, operatingSystem)
        self.phone_number = phoneNumber

    def get_phone_number(self):
        return self.phone_number
