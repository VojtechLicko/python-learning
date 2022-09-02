from collections import Counter, defaultdict, namedtuple

# Basically alternative and an adition to built-in python containers


# Counter is a dict subclass which helps count hashable objects.
# Inside of it elements are stored as dictionary keys
# and the counts of the objects are stored as the value.
lst = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]

print(Counter(lst))
x = (Counter("Hello World I am pritty good"))


# defaultdict is a dictionary-like object which provides
#  all methods provided by a dictionary but takes a first argument
# (default_factory) as a default data type for the dictionary.
#  Using defaultdict is faster than doing the
# same using dict.set_default method.
# A defaultdict will never raise a KeyError.
# Any key that does not exist gets the value returned by the default factory.

d = defaultdict(lambda: 0)
print(d["one"])


# namedtuple
# its something between a tuple and a object
Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sam = Dog(age=2, breed='Lab', name='Sammy')

frank = Dog(age=2, breed='Shepard', name="Frankie")

print(sam)
print(frank.breed)
print(frank[2])
