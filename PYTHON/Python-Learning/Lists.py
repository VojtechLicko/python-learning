my_friends = ["Kevin", "Karen", "Karen", "Jim", "Toby", "Oscar"]
print(my_friends[::-1])
print(my_friends)
# Print function will print out the whole list
# U can store large amounts of data in lists


print(my_friends[0])
# To print out specific element out of the list use indexing that starts from zero


print(my_friends[1:3])
# To print out certain section of the list u can use the colon and it includes the first number u put in but excludes
# the one that your section ends with


# U can modify lists


my_friends[1:3] = "Michael", "Johny"

print(my_friends)

# FUNCTIONS IN LISTS
# Lists are great to store lots of data in
lucky_numbers = [4, 8, 15, 16, 23, 42]
# .extend basically extends the list with the values u put in
my_friends.extend(lucky_numbers)
print(my_friends)
# .append basically adds the certain word to the end of the list
my_friends.append("Creed")
print(my_friends)
# .insert basically inserts the word u put in, in the location u put in
my_friends.insert(1, "Kelly")
print(my_friends)
my_friends.remove("Johny")
print(my_friends)
# .remove basically removes the certain word from the list
my_friends.pop()
print(my_friends)
# .pop pops the last element of the lis
print(my_friends.index("Kelly"))
# when u call your list . index it will tell you if certain word is in the list or it isnt
print(my_friends.count("Jim"))
# .count will tell me how many times is certain thing in the list

# What .sort does it sorts the list in alphabetical or number order

my_friends.reverse()
# .reverse basically reverses the whole list
print(my_friends)
# To copy some list in another we use .copy function
my_friends.clear()
# .clear basically clears the whole list
print(my_friends)

x = 5
u = 67

x -= 1
print(x)
x += 1
print(x)

new_list = ['one', 'two', 'three', 'five']
new_list.pop()
print(new_list)

# * is used to unpack
print(new_list)
print(*new_list)

# allow duplicates
my_list = ("apple", "banana")
print(type(my_list))
print(list(my_list))
my_list = ['string', 100, 12.3]
print(len(my_list))
print(my_list[0])
print(my_list[1:])
another_list = ['four', 'five']
# we can use concatenation with lists
new_list = my_list + another_list
new_list[0] = "one all caps"
print(new_list)
print(new_list.pop())  # u can print the popped item
print(new_list)
