first_num = float(input("Enter the first number : "))
operator = input("Enter the operator :")
second_num = float(input("Enter the second number: "))

if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "/":
    try:
        print(first_num / second_num)
    except ZeroDivisionError:
        print(" U cant divide by zero")
elif operator == "*":
    print(first_num * second_num)
else:
    print("U did not input the right  operator or numbers")

# Raise an exception


x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
