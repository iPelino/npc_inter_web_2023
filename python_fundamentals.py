# printing some text to the console
# print("hello there!")
'''
this is a multi
line comment
'''

"""
this is also a multi
line comment
"""

# variables
# a variable is a container for a value
from abc import ABC, abstractmethod


message = "Helol World!"
# print(message[0:5:3])

# User input
# number = int(input("Enter any number "))

# print(number + number)

# conversion
# int()
# str()
# float()

# string operations

# print("o" in message)

# a = int(input("enter num a"))
# b = int(input("enter num b"))
# c = a/b
# if c%2 == 0:
#     if 1==1:
#         if True:
#             if False:
#                  pass


# LIST

names = []
other_names = ["Peter", "Pamela", [1,2,3,[4.1, 4.2, 4.3]]]
numbers = [2,5 ,7, 10, 13]
names.append("Paul")
names.append("Paula")
names.insert(0, "Pascal")
# names.clear()
complete_list = names + other_names
powered_list =[]
for number in numbers:
    powered_list.append(number**2)
# print(powered_list)


# print(names[-1][:4])

# DICTIONARIES
# ===============

student_marks = {
    "paul": {"web": 60, "math": [40, 50], "hacking": 65},
    "Jane": 25,
    "Pamela": 40
}

# print(student_marks)
# print(student_marks["paul"]["hacking"])
# print(student_marks.values())
# student_marks.values()

# LOOPS

text = "Hello World"

# for letter in range(0,20, 2):
#     print(letter)

# FUNCTIONS
# definition
def add(a, b=0):
    return a + b


# call
# add(a=5)
# add(10, 100)
# add()
# add()
# print(add(5, 10))

def somefunc(*args, **kwargs):
    print(args)
    print(kwargs)

# somefunc(1,2,3, name="paul", age=20)


# CLASSES
# =========
# class definition
class Person:
    # class attributes: class variables
    department = "CS"
    # class attributes: instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.color = "black"

    # instance methods
    def greet(self, name):
        print(f"Hello {name}")

    # class methods
    @classmethod
    def testing():
        pass

    # static methods
    @staticmethod
    def testing2():
        pass


# class instantiation
paul = Person("Paul", 20)

print(paul.name)
paul.greet("Peter")
paul.color = "white"
print(Person.department)


# OOP Pillars

# Inheritance
class Student(Person):
    def __init__(self, name, age, regno):
        super().__init__(name, age)
        self.regno = regno

    def greet(self, name, email):
        return f"Hello {name}, your email is {email}"
    
# Abstraction
class Vehicle(ABC):
    @abstractmethod
    def accelerate(self):
        pass


class Car(Vehicle):
    def accelerate(self):
        pass

class Truck(Vehicle):
    def accelerate(self):
        pass

car1 = Car()