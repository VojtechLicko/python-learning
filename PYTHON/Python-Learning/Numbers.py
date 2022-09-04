from math import *

# from math import basically imports everything from math
# when u import something from some module u basically
# get access to the code and functions someone already wrote and u can use them
print(5 + 4)
print(2.890)
print(-3.23)
print(3 + 4.5)
print(3 * (4.5 + 5.3))
# u can do basically whatever you want with python math
print(10 % 3)
# this weird symbol is read mod and basically what it does
# it spits out the remainer of dividing as I did in my first class


# We can store numbers in variables
my_num = 5
print(my_num)

# To use number with string in one sequence  u have to put the number inside of parentheses and before the first
# parenthesis u have to use str and what str does it basically converts the number into the string so u could use it
# If u don't  use the str to convert it will cause error

print("It is rainy outside today " + str(my_num))

my_num_2 = - 6
print(abs(my_num_2))
# abs stands for absolute value
print(pow(4, 5))
# Power je vlastně mocnina sami si určíme co na kolikátou umocnit
print(max(5, 9))
# Max prints out the biggest number basically, and min does the right opposite
print(min(6, -4))

print(round(3.2))
# Round is just normal rounding of numbers
print(floor(5.7))
# What floor does it basically always rounds the number to the lower level no matter what
print(ceil(5.1))
# What ceil does its basically that it always rounds the number to the upper level no matter what
print(sqrt(36))
# sqrt je vlastně odmocnina
# There is huge amount of these on internet so if I need any i can search for them


print(11_11_11)  # underscores in numeric literals to improve readability

# using octals in python
print(0o123)  # with 0o prefix
# using hexadecimals in python
print(0x123)  # with 0x prefix
print(type(4.))  # is basically the same as 4.0

# Take, for example, the speed of light, expressed in meters per second. Written directly it would look like this:
# 300000000.
#
# To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already
# seen: 3 x 108.
#
# It reads: three times ten to the power of eight.
#
# In Python, the same effect is achieved in a slightly different way - take a look:
#
# 3E8
#
# The letter E (you can also use the lower-case letter e - it comes from the word exponent) is a concise record of
# the phrase times ten to the power of.

print(type(1e-22))

num = 5_355_600  # u can use underscores so the numbers will be more readable if u use spaces it will throw syntax err
print(num)
num = 5, 6
print(num)
num = 5.6  # point and comma dont mean the same when using numbers
print(num)

# using scientific notation in python
#  e and E when using numbers means exponent
# when using E the number that comes after it means how many times do u want to put the first number to the power of ten
print(3E1)
print(3E10)
# u can use this both in positive numbers and negative numbers
print(6.62607E-34)
print(2 ** 2 ** 3)
print(1/1)
