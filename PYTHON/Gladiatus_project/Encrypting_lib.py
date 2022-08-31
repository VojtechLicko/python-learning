from cryptography.fernet import Fernet

file_name_1 = 'key_1.txt'
file_name_2 = 'key_2.txt'
file_name_3 = 'key_3.txt'


# Here we are creating 3 txt files to store key
#  for the encryption in bcs we are doing triple encryption

def write_key_1():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(file_name_1, "wb") as key_file:
        key_file.write(key)


def write_key_2():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(file_name_2, "wb") as key_file:
        key_file.write(key)


def write_key_3():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(file_name_3, "wb") as key_file:
        key_file.write(key)


def load_key_1():
    """
    Loads the key from the current directory named `key.key`
    """
    return open(file_name_1, "rb").read()


def load_key_2():
    """
    Loads the key from the current directory named `key.key`
    """
    return open(file_name_2, "rb").read()


def load_key_3():
    """
    Loads the key from the current directory named `key.key`
    """
    return open(file_name_3, "rb").read()


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        # encrypt data
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


# uncomment this if it's the first time you run the code, to generate the key
'''write_key_3()

key = load_key_3()
file = "Hesla.txt"
# encrypt it
encrypt(file, key)'''

'''with open('key_3.txt', 'r+') as key_33:
    for lines in key_33:
        lines = str(lines)

decrypt('Hesla.txt', key=lines)
# Takhle to celé fungovalo'''
