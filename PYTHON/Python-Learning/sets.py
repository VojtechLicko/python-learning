my_set = {1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5}
my_set.add(6)
print(my_set)
# sets do not allow duplicates, unique values only
# the order of sets is not guaranteed
# | symbol is used to create a union of sets
# unordered and unindexed
# unchangebale
# sets are undordered
set_2 = {5, 8, 9}
union = my_set | set_2
print(union)  # sjednocení
# we can do intersections with & (průnik)
# we can do difference of set with -(rozdíl)
# We can use method .add with sets
'''FrozenSets'''
# the Difference between frozen sets and sets is that frozen sets are mutable

# we can use sets to get rid off unique values in lists etc.

my_list = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
print(set(my_list))











