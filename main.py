
import os
from cryptography.fernet import Fernet
key = Fernet.generate_key()

#Make A Key
if not os.path.exists('mykey.key'):
    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

the_file = input(str('Please pick a file: '))
#Encrypting
def Encrypt():


    f = Fernet(key)

    with open(the_file, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open(the_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


#Decrypting
def Decrypt():


    f = Fernet(key)

    with open(the_file, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)


    with open(the_file, 'w') as decrypted_file:
        new = decrypted.decode()
        #print(new)
        decrypted_file.write(new)



#Ask
result = input(str("Do you want to (e)ncript or (d)ecript: "))
if result in ['e', 'E']:
    Encrypt()
if result in ['d', 'D']:
    Decrypt()