
s = set()

# add elements to set
s.add(1)
s.add(2)
print(s)
# clears the set
s.clear()
print(s)

s = {1, 2, 3}
sc = s.copy()  # copies one set
s.add(4)
print(s)
print(sc)
s.difference(sc)  # returns the difference between two sets
(s.difference_update(sc))  # basically \ in sets
print(s)
sc.discard(3)  # removes char thats in the set
print(sc)
s1 = {1, 2, 3}
s2 = {1, 2, 4}

print(s1.intersection(s2))  # basically průnik
s1.intersection_update(s2)
print(s1)

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

# returns boolean based on if two sets have intersection
print(s1.isdisjoint(s2))


print(s1.isdisjoint(s3))

# issubset
# This method reports whether another set contains this set.
print(s.issubset(s2))


# issuperset
# This method will report whether this set contains another set.

s2.issuperset(s1)

# symmetric_difference and symmetric_update
# Return the symmetric difference of two sets as a new set.
# (i.e. all elements that are in exactly one of the sets.)

print(s1)
print(s2)
print(s1.symmetric_difference(s2))


# union
# Returns the union of two sets (i.e. all elements that are in either set.)
print(s1.union(s2))

# update
# Update a set with the union of itself and others.
print(s1)
s1.update(s2)
print(s1)
