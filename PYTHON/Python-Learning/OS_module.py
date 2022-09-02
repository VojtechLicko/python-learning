import os

# import shutil

# import send2trash

# f = open("practice.txt", mode="w+")
# f.write("This is a text string")
# f.close()

# This will get me my current working directory
print(os.getcwd())

# Listdir will get me everything in a specified directory
current_directory = os.getcwd()
print(os.listdir(current_directory))

# This is used to move files on your pc
# shutil.move('practice.txt', "C:\\Users\\vojta")
print(3 * "\n")
print(os.listdir("C:\\Users\\vojta"))

# Deleting Files
# os.unlink(path) which deletes a file at the path your provide
# os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
# shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.
# None of these methods can be reversed
# Send2trash is better alternative module

# shutil.move('C:\\Users\\vojta\\practice.txt', os.getcwd())
# send2trash.send2trash(
#    "C:\\Users\\vojta\\OneDrive\\Plocha\\Personal_programming\\PYTHON\\Python-Learning\\venv\\practice.txt")


# What os.walk does is that it will go through specified directory
# For each directory in the directory tree rooted at top (including top itself, but excluding '.' and '..'), yields a 3-tuple
for folder, sub_folders, files in os.walk("C:\\Users\\vojta\\OneDrive\\Plocha\\Practice_programs"):
    print("Currently looking at folder: " + folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold)

    print('\n')

    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
