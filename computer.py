# Rebecca_Nell
# CIS 135
# computer.py
# Week 13 Assignment

# import of child Electronics child class
from electronics import Electronics


# Computer class defined and extends from Electronics class
class Computer(Electronics):
    def __init__(self, brandName, operatingSystem):
        super().__init__(brandName)
        self.operating_system = operatingSystem

    def get_operating_system(self):
        return self.operating_system
