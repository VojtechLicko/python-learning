# Regex stands for regular expressions
# Regular Expressions (sometimes called regex for short) allows
# a user to search for strings using almost any sort of rule
# they can come up. For example, finding all capital letters
# in a string, or finding a phone number in a document.

# \d	A digit	file_\d\d	file_25
# \w	Alphanumeric	\w-\w\w\w	A-b_1
# \s	White space	a\sb\sc	a b c
# \D	A non digit	\D\D\D	ABC
# \W	Non-alphanumeric	\W\W\W\W\W	*-+=)
# \S	Non-whitespace	\S\S\S\S	Yoyo

# Character	Description	Example Pattern Code	Exammple Match
# +	Occurs one or more times	Version \w-\w+	Version A-b1_1
# {3}	Occurs exactly 3 times	\D{3}	abc
# {2,4}	Occurs 2 to 4 times	\d{2,4}	123
# {3,}	Occurs 3 or more	\w{3,}	anycharacters
# \*	Occurs zero or more times	A\*B\*C*	AAACC
# ?	Once or none	plurals?	plural

# re is a basically module for manipulating text
# Or if you need to find a specified pattern in text
import re

# print(help(re))
text = "The person's phone number is 408-555-1234. Call soon!"
print('phone' in text)
pattern = 'phone'
print(re.search(pattern, text))
# . is wildcard character in this module
# r stands for raw so python knows that
# the backslashes aren't escape characters
phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{3,})")
# the parentheses create group u can later go through with
# .group() .compile() puts these patterns together

results = re.search(phone_pattern, text)


print(results)
print(re.findall(phone_pattern, text))

for match in re.finditer("phone", text):
    print(match.span())  # returns start and end of the pattern
    print(match.group())

# print(help(match.span))

print(results.group(1))

# u can exclude certain characters and stuff, if u need to
# just look up documentation
phrase = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]', phrase))
test_phrase = 'This is a string! But it has punctuation. How can!!!!!!!\
     we remove it?'
clean = (re.findall('[^!.? ]+', test_phrase))
print(' '.join(clean))

text = "Only find the hypen-words in this sentence. But you do not know how\
 long-ish they are"
print(re.findall(r"[\w]+-[\w]+", text))
