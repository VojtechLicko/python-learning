list1 = [1, 2, 3]

print(list1.append(4))  # adds to the end of the list individually
print(list1.count(10))  # counts how many times is the element in the list
print(list1.extend([5, 6]))  # extends the list with multiple vals
print(list1.index(2))  # index() will return the index of whatever element is
# placed as an argument. Note: If the the element is not in the list
# an error is raised

# insert
# insert() takes in two arguments: insert(index,object)
# This method places the object at the index supplied. For example
list1.insert(2, 'inserted')
print(list1)

# pop
#  which allows us to "pop" off the last element of a list.
#  However, by passing an index position you can remove and
#  return a specific element.
ele = list1.pop(1)  # pop the second element
print(list1)
print(ele)

# remove
# The remove() method removes the first occurrence of a value. For example:
list1.remove('inserted')

print(list1)
list2 = [1, 2, 3, 4, 3]

list2.remove(3)
print(list2)

list2.reverse()
print(list2)

# sort
# The sort() method will sort your list in place:
# takes arg for descending/ascending order
list2.sort()
print(list2)

# A common programming mistake is to assume you can assign a modified list
# to a new variable. While this typically works with immutable objects like
# strings and tuples:
