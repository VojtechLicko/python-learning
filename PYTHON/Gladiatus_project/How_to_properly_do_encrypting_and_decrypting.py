from Encrypting_lib import *

# This here is basically writing 3 keys and encrypting with them
write_key_1()
write_key_2()
write_key_3()
key_1 = load_key_1()
key_2 = load_key_2()
key_3 = load_key_3()
file = "Hesla.txt"
# encrypt it
encrypt(file, key_3)
encrypt(file, key_2)
encrypt(file, key_1)


# This here is decrypting and this is how the whole process should look like together

'''with open('key_1.txt', 'r+') as key_11:
    for lines in key_11:
        lines = str(lines)

decrypt('Hesla.txt', key=lines)

with open('key_2.txt', 'r+') as key_22:
    for lines in key_22:
        lines = str(lines)

decrypt('Hesla.txt', key=lines)


with open('key_3.txt', 'r+') as key_33:
    for lines in key_33:
        lines = str(lines)

decrypt('Hesla.txt', key=lines)'''
