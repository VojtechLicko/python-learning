# we can get the data type of a variable by using a function type() like this:

x = 5  # this is a int data type cause it is not a decimal number but its still a number
print(type(x))
y = 5.0  # this a float data type cause it is a decimal number
print(type(y))
z = "5"  # this is a string data type basically just plain text  we can use both single quotes and double quotes to
# define it
print(type(z))
d = '5'  # this is basically the same as the above
print(type(d))

# Variable names are case sensitive so if we change a letter in variable to a capital letter its a suddenly new variable

# Variable names cannot start with a number and can only contain numbers and Alphabet with exception for underscore _


# To make variable names more readable we can use capitalization or underscores

# We can assign more variables to different values with one line of code like this:

u, i, o = "Orange", "Banana", 5

print(u)
print(i)
print(o)

# We can also assign multiple variables to same value in the same line

h = j = k = "Orange"
print(h)
print(j)
print(k)

# When using , instead of + to add strings together
# What we basically do with , is that we convert all arguments to strings and print them with separated spaces
# But with + we are creating one big string


# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview


# x = str("Hello World")	str (concatetion)
# x = int(20)	int
# x = float(20.5)	float
# x = complex(1j)	complex
# x = list(("apple", "banana", "cherry"))	list
# x = tuple(("apple", "banana", "cherry"))	tuple
# x = range(6)	range
# x = dict(name="John", age=36)	dict
# x = set(("apple", "banana", "cherry"))	set
# x = frozenset(("apple", "banana", "cherry"))	frozenset
# x = bool(5)	bool
# x = bytes(5)	bytes
# x = bytearray(5)	bytearray
# x = memoryview(bytes(5))	memoryview


# We can assign a data type to variable using functions like : int() etc.
x = float(5)

# We can check strings
txt = "The best things in life are free!"
print("free is in text " if "free" in txt else "")
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

print("expensive is not in the text " if "expensive" not in txt else"")
