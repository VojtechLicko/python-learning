# The syntax is : newlist = [expression for item in iterable if condition == True]
nic = []
l_1 = [x ** 2 for x in range(1, 7)]
print(l_1[::-1])

l_1.reverse()
print(l_1)

for x in range(6, 0, -1, ):
    nic.append(x ** 2)
print(nic)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comprehension = [n for n in nums]
print(comprehension)
comprehension = [n * n for n in nums]
print(comprehension)
comprehension = [n for n in nums if n % 2 == 0]
comprehension = [(letter, num) for letter in 'abcd' for num in '0123']
print(comprehension)
