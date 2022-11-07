#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:14:43 2022

@author: max
"""

# make a basic class or Human
class Human:
    # every object of the class needs to be initialised
    # with the __init__ function
    
    # __init__ is known as the "constructor" function in 
    # object oriented programming
    
    # __init__ by default receives "self" as the first
    # argument
    def __init__(self, age, gender='F', name=None):
        self.age = age
        self.gender = gender
        self.name = name
        self.check_if_adult()
    # end __init__

    def check_if_adult(self):
        self.is_adult = False
        if self.age >= 18:
            self.is_adult = True
    # end check_if_adult

    def print_info(self):
        print('age:         ', self.age)
        print('gender:      ', self.gender)
        print('name:        ', self.name)
        print('is_adult:    ', self.is_adult)
# end Human

# when an object is initialised, the fuction __init__ is called
h = Human(24)
g = Human(12, gender='M', name='Mark')
# j = Human() # will produce error:
# TypeError: __init__() missing 1 required positional argument: 'age'

# print(h.age)
# print(g.name)
# print(g.age)

h.print_info()
g.print_info()


# make a new class for Athlete that *inherits* from the class Human
# which makes sense, since athletes are humans
class Athlete(Human):
    def __init__(self, age, height=None, weight=None, gender='F', name=None):
        super().__init__(age, gender=gender, name=name)
        self.height = height
        self.weight = weight
        self.compute_bmi()
    # end __init__

    def compute_bmi(self):
        if self.height is None or self.weight is None:
            self.bmi = None
            self.bmi_category = None
        else:
            self.bmi = self.weight/(self.height**2)
            self.bmi_category = 'healthy'
            if self.bmi >= 25:
                self.bmi_category = 'overweight'
            elif self.bmi < 18.5:
                self.bmi_category = 'underweight'
    # end compute_bmi

    def print_info(self):
        super().print_info()
        print('height:      ', self.height)
        print('weight:      ', self.weight)
        print('bmi:         ', self.bmi)
        print('bmi cat.:    ', self.bmi_category)
# end class Athlete

a = Athlete( 21, 1.7, 95 )
print("========================")
a.print_info()