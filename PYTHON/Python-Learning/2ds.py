number_grid = [
    [1, 2, 3, ],
    [4, 5, 6, ],
    [7, 8, 9, ],

]
print(number_grid[2][1])

# this is called 2d list(basically two lists together)
# Now we are going to show a nested for loop
# (basically a for loop in a for loop to get access to the data in the 2d lists)


for row in number_grid:
    for numbers in row:
        print({numbers}, " this is that".format(numbers))

me = True
if me:
        print("není pravda")
else:
    print("Je pravda")