# You can put certain parameters  that user needs to put in, in those a parentheses next to the function name


def say_hi(name, age):
    print("Hi " + name + "I noticed you are " + str(age))


# In order to run the function you have to call it
say_hi("Mike", 35)
say_hi("Steve", 40)


# U have to indent the code that is in the function

# If you are naming something in python and there is 2 or more words we usually use underscoree there

# RETURN FUNCTION
def cube_v2(num):
    return print(num * num * num)


def cube(num):
    x = num * num * num
    print(x)


cube(3)

cube_v2(9)


def exponent(exponent_1, exponent_2):
    return exponent_1 ** exponent_2


print(exponent(3, 3))


# Create functions to do one simple thing not multiple hard things

# keyword arguments make your code more readable
# u can say what type should be each variable used in the function
# 'and say what type should have the result of the function
def increment(number: int, by: int = 1) -> int:
    return number + by


# we can set default values of arguments in functions

print(increment(5, by=3))

# If we dont know how many keyword argmuments are thre gonna be we use **kwargs and if we dont know how many arguments
# are gonna be there we use *args
