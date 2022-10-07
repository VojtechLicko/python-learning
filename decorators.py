def hello(name="Jose"):
    return "Hello " + name


# Here we create a copy of the function
greet = hello
print(greet())


def hello(name="Jose"):
    print("The hello() function has been executed")

    def greet():
        return "\t This is inside the greet() function"

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")


hello()


def hello(name="Jose"):
    def greet():
        return "\t This is inside the greet() function"

    def welcome():
        return "\t This is inside the welcome() function"

    if name == "Jose":
        return greet
    else:
        return welcome


x = hello()
print(5 * "\n")
print(x())


def hello():
    return "Hi Jose!"


def other(func):
    print(3 * "\n")
    print("Other code would go here")
    print(func())


other(hello)


def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before the original fucntion")
        original_func()
        print("Some extra code, after the orginal function")

    return wrap_func


def func_needs_decorator():
    print("I want to be decorated!!")


print(2 * "\n")
decorated_func = new_decorator(func_needs_decorator)
decorated_func()
print(2 * "\n")


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")


func_needs_decorator()


def uppercase_decorator(function):
    func = function()
    make_uppercase = func.upper()
    return make_uppercase


@uppercase_decorator
def say_hi():
    return "hello there"


print(5 * "\n")
# so here basically decorator is called on say_hi and modifies it
# and then the say_hi is called
print(say_hi)

x = 2


def my_decorator(func):
    result = func()
    return result**2


@my_decorator
def my_function():
    return x**2


print(5 * "\n")
print(my_function)


def decorator_factory(argument):
    def your_decorator(function):
        return function.upper()

    return your_decorator


@decorator_factory
# @your_decorator
def your_func(x):
    return x


print(3 * "\n")
print(your_func("Hello"))
# A decorator is a design pattern in Python that allows a user to add new
# functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want
# to decorate.
