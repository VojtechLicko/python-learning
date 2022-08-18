is_male = False
is_tall = False

if is_male and is_tall is True:
    print("You are a tall male")
elif is_male is True and is_tall is False:
    print("You are a short male")
elif is_male is False and is_tall is False:
    print("You are a short female")
elif is_male is False and is_tall is True:
    print("You are a tall female")

x = 5
y = 5
# with if statements u can use:
# and
# or
# not
# xor basically means that only if one value of the values is true it will return true, but if both values are true
# xor will return false
hungry = True

if hungry:
    print("Feed me")
else:
    print("im not hungry")

loc = "Ban"

if loc == 'Auto Shop':
    print("Cars are cool")
elif loc == "Bank":
    print(" I have money")
else:
    print("what is this")

name = "Sammy"

if name == "Frankie":
    print("Hello Frankie")
elif name == "Sammy":
    print("Hello Sammy")
else:
    print("Hi someone")

# Short Hand If
# We use shorthand if u have only one statement to execute, you can put it on the same line as the if statement.
# if a > b: print("a is greater than b")
# Shorthand If Else
# a = 2
# b = 330
# print("A") if a > b else print("B")
