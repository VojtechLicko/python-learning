var = lambda x, y: x + y
print(var(60, 88))


def addition(x, y):
    res = (x + y)
    return res


print(addition(7, 8))
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
