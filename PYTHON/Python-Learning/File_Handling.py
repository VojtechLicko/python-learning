import os.path

# Reading from external files in python
# for opening a file we use special command open()
# In python u can use relative path to the file, absolute path to the file or
# u can use just the name of the file if its in the same directory
file_try = open("filehandler", "r")
# There are multiple modes for handling files w = write a = append r = read r+ = read, write whenever you stop using
# the file use the .close function to close it Also whenever you try to take data from some document its good to
# check before if its readable We do that with .readable() function We can change if the file is readable with its
# mode When you want to read a single line we use .readline() function When we use .readlines function it puts all of
# the lines into a list We can get certain lines by specifying their index It is quite often useful to use for loop
# in files To use append mode we use the a mode and .write(function) Be aware that you can easily mess the file up
# with these functions If you wanna put something on a new line just use the \n escape character When you use w mode
# writing it just overwrites the whole document You can also use w to create a new file u can imagine that there is a
# cursor in the text file and once you read it the cursor is on the end of the text file so u can not read the file
# again , to read the file again u would have to use the .seek method like this myfile.seek(0)
print(file_try.readlines())
file_try.close()

my_file = open('udemy.txt')
x = my_file.read()
print(x)

file_name = "the document"  # here i put my file

if os.path.isfile(file_name):

    with open("the document", "type in which i open the document") as file:
        print(file.read())  # will show u the content of the file
else:
    print(f"file {file_name} does not exist.")

