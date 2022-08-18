print(0.1 + 0.2 - 0.3)
print("I'm the {}".format('man'))
print("who is the {0} or {1}".format('man', 'woman'))
print('Am i {j} or am I {b} well I think I am {s}'.format(j='jello', b="brain", s="sad"))
print(100 / 777)
result = 100 / 777
#                 value:width.precision
print("The result was {r:1.100f}".format(r=result))
# with formatting we can set how we wannna see the result
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# basically for sticking a variable into a string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
name = "Jose"
age = 3
print(f"Hello {name}")
print(f"{name} is {age} years old.")
# in formatted strings u can use numbers without getter an error
print(name + " is " + str(age) + "years old")
# Random Practicing
# Random Practicing
# Random Practicing
# Random Practicing
# Random Practicing
# Random Practicing
# Random Practicing

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd number: {num}")

list_sum = 0

for num in my_list:
    list_sum = list_sum + num

print(list_sum)

my_string = "Hello World"
for letter in my_string:
    print(letter)

x = 0

while x < 5:
    print(f"the current value of x is {x}")
    x += 1

else:
    print("X IS NOT LESS THAN FIVE")

print(list(range(0, 11, 2)))
# enumerate
index_count = 0

for let in 'abcde':
    print(f'At index{index_count} the letter is {let}')
    index_count += 1

word = "abcde"

for item in enumerate(word):
    print(item)
# automatic indexing for us in tuples
