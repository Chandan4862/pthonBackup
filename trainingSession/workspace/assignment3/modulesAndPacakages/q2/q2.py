
# 2. Create a package consisting different functions related to cryptography.  
# Ex: Encryption, Decryption, AES256, Salting, MD5 Generation
# Minimum 5 relatable functions required in a package

# print(f.decrypt(encrypt_value))
from crypto.cryptog import encrypt
from crypto.cryptog import decrypt
from crypto.cryptog import md5
from crypto.cryptog import salty
print("Enter string")
string=input()

encrypted_msg,key= encrypt(string)
print("Encrypted::",encrypted_msg)

decrypted_msg= decrypt(encrypted_msg,key)
print("Decrypted::",decrypted_msg)

print("Byte eqvivalent of MD5 hash::",md5(string))

print("Salted::",salty(string))


