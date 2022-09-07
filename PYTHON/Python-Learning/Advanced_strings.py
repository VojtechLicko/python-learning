s = "helloworld"


# String methods
print(s.capitalize())  # capitalizes first letter
print(s.lower())  # lowers the string
print(s.upper())  # turns everything to uppercase
print(s.count("o"))  # counts number of occurences of certain char
print(s.find("o"))  # finds first occurence of a char
# The center() method allows you to place your string 'centered' between
#  a provided string with a certain length.
print(s.center(20, "z"))
print('hello\thi'.expandtabs(10))  # makes the tabs bigger

# alphanumeric > numbers or chars
print(s.isalnum())  # checks if all the chars are alphanumeric
print(s.isalpha())  # checks if every characters are alphabetic
print(s.islower())  # checks if the string is lowercase
print(s.isspace())  # checks if the string is whitespace string
print(s.istitle())  # checks if something is title
print(s.isupper())  # checks if all chars are upper
print(s.endswith("o"))  # checks if somethign ends with certain char
print(s.split("e"))  # separates at every occurence
print(s.partition("o"))
