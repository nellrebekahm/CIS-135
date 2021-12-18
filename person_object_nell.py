# Rebecca Nell
# CIS 135
# person_object_nell.py
# Assignment #27

class Person:
    def __init__(self, first_name, last_name, favorite_food):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_food = favorite_food
        return

    def personal_traits(self):
        print(f'The favorite food of {self.first_name.title()} {self.last_name.title()} is {self.favorite_food}.')
        return


# fn = 'clinton'
# ln = 'garwood'
# ff = 'granola'
# my_object = Person(fn,ln,ff)
# print(type(my_object))
# my_object.personal_traits()
