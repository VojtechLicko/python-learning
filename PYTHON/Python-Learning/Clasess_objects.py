# Class is basically your own data type
# Everything that is indented under class student goes into there
# __init__ in python is basically initialize
# In init u define what a Student is in our program
# Class is basically overview for all the object students
from typing import Any


class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name  # Here we basically say that the name of the student will be equal to the name we passed in
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        # with these you can basically call the students name and it will return a valu


student1 = Student("Vojta", "IT", 1, "Yes")
Student_overview = (str(student1.gpa) + " " + student1.major + " " + student1.name + " " + student1.is_on_probation)
print(Student_overview)
print(student1.name)
student2 = Student("Vo", "T", 9, "Yes")
print(student2.gpa)


class Phone:  # The thing that defines the object
    def __init__(self, processor, price, gpu):  # here we basically tell what properties do we wanna have on our object
        self.processor = processor  # it basically constructs the whole object
        self.price = price
        self.gpu = gpu

    def __str__(self) -> str:  # returns a string of a object
        return f"{self.gpu} is calling {self.price}"


iphone = Phone(processor="a13", gpu="a13", price=300)
Samsung = Phone(processor="a15", gpu="a13", price=3000)  # Properties of the actual object

print(iphone)
print(Samsung)

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left
# next(my_iter)

# __iter__ and __next__ are used to iterate through classes

