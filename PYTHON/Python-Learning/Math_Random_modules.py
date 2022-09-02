import math
import random

# math modules is for math operations and math generally
# random is a number generator
# U can actually use help() function for every module to see its uses
value = 4.35
print(math.floor(value))
# at .5 values with round in python, u choose to round up or down on
# odds and evens so u would get as much numbers rounded down
# as you would get rounded up
print(round(value))
print(math.pi)
print(math.inf)
print(math.nan)
print(math.e)
# for operations with numbers numpy is another really good module
print(math.log(100, 10))
print(10**2)
print(math.degrees(math.pi/2))
print(math.radians(180))
print(random.randint(0, 100))
random.seed(101)  # seed is basically like seed in minecraft
# it basically predefines what will the random.randint methods return
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
my_list = list(range(0, 20))
print("\n")
# Random.choice returns one random item from a sequence
# Random.choices does same thing but returns multiple outputs
print(random.choice(my_list))
print(random.choices(my_list, k=10))
# Shuffles the list randomly
random.shuffle(my_list)
print(my_list)
# returns random float random in given range
print(random.uniform(0, 100))
print(random.gauss(0, 1))
