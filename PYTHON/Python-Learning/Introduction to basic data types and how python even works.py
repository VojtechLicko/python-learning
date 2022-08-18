print("1")
print("2")
print("1")
print("6")
# memorize shortcuts
print("Hello world \n" * 10)
# in python u can multiply
# Python executes code in order
# Variables = Its a container where we can store certain data values
# In python u can multiply strings
age = 70
character_name = "Johny"
print("There once was a man named " + character_name + ",")
print("he was " + str(age) + " years old")
age_of_character_2 = 89
# U can create multiline strings only with triple quotes
multiple_line_str = """Now its 
possible cause 
I have
Triple
Quotes
"""
# In python :
# x, y = 1, 2
# Is same as
# x = 1
# y = 2
# also we can set multiple variables to same value
# x = y = 1
print("He really liked the name " + character_name + ",")
print("But he didn't like being " + str(age_of_character_2) + ".")

# Boolean is True of False data and u can as well store it in variables
# Numbers
# Strings are just a plain text


print("Giraffe\n academy")

# \n creates a new line

print("This is a quotation mark""\"")

# To print out quotation mark u have to use backslash before it so python knows what you are using it for

phrase = "Giraffe Academy"

print(phrase.lower())
print(phrase.upper())
# .lower  lowers the all the letters to lowercase and .upper does the right opposite

print(phrase.isupper())
print(phrase.islower())
# .isupper is basically function that asks if the certain phrase u put in is all in upper case, if its not
# it will return False if it is it will return True and its the right opposite with the .islower

print(len(phrase))
# len basically measures how many characters are there in a string,
# the empty places when you used spacebar count as characters too


# Indexing in python starts from zero and program is executed in its order from line 1 to whatever line it ends

# If I wanna grab specific character lets say the first character, The first character is on 0th index and
# the second character  in the phrase has indexing 1st
print(phrase[0])

print(phrase.index("G"))
# .index will return a index of the the "G" I wrote in the brackets
# If i put something in there that is not in the phrase , It will show me a error that substring was not found
print(phrase.replace("Giraffe", "Tiger"))
# With .replace u basically replace whatever you need in the phrase with something else
# There are lots of these functions in python and I can search for them whenever I need them if i want to
print(multiple_line_str)
# With this  syntax of declaring variables u can link variable to specific type
school: str = "this is school"
# if u try to declare something u declared as string as integer  it will throw warning at u
school = 55


# In static programming languages we have to declare what type of data the variables are when we first declare them
# And if we try to change variable that was previously declared as a string the static programming languages will
# complain and every variable is set to type in compile time


# But with the dynamic languages every variable is  determined at the runtime of the program so we can basically
# redeclare string as integer


# If i hover my mouse over a variable in python it will show its type , I can also do the same thing with type() method
# Also in python u can use negative index so it starts from the end of the string



