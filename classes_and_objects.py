# Class is basically your own data type
# Everything that is indented under class student goes into there
# __init__ in python is basically initialize
# In init u define what a Student is in our program
# Class is basically overview for all the object students

# p.py
class Python:
    def __init__(self, learning, language):
        self.learning = learning       # public
        self.__language = language     # private


def who(self):
    print('learning  : ', self.learning)
    print('language : ', self.__language)


x = Python(learning='coding', language='Python')
print(x.learning)
# print(x.__language)
'''



class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        # Here we basically say that the name of the student will be equal to the name we passed in
        self.__name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        # with these you can basically call the students name and it will return a valu

        @property
        def name(self):
            return self.__name


student1 = Student("Vojta", "IT", 1, "Yes")
print(student1.name)
student1.name = "x"
print(student1.name)


Student_overview = (str(student1.gpa) + " " + student1.major +
                    " " + student1.name + " " + student1.is_on_probation)
print(Student_overview)
print(student1.name)
student2 = Student("Vo", "T", 9, "Yes")
print(student2.gpa)
student1.nam


class Phone:  # The thing that defines the object
    # here we basically tell what properties do we wanna have on our object
    def __init__(self, processor, price, gpu):
        self.processor = processor  # it basically constructs the whole object
        self.price = price
        self.gpu = gpu

    def __str__(self) -> str:  # returns a string of a object
        return f"{self.gpu} is calling {self.price}"


iphone = Phone(processor="a13", gpu="a13", price=300)
# Properties of the actual object
Samsung = Phone(processor="a15", gpu="a13", price=3000)

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
'''
