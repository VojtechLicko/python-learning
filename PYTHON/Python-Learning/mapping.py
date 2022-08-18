# Python map() function
# map(fun, iter)
# Parameters :
#
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
# Basically we have something we can iterate over and function and we iterate over it with a function


# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
