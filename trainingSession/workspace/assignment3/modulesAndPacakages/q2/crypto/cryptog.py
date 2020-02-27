from cryptography.fernet import Fernet
import hashlib
def encrypt(str1):
    str2= str1.encode()
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypt_value = f.encrypt(str2)
    return encrypt_value,key

def decrypt(str,key):
    f=Fernet(key)
    return f.decrypt(str)

def md5(string):
    md5= hashlib.md5(string.encode())
    return md5.digest()

def salty(string):
    salt='1AC'
    encoded=salt.encode()+string.encode()
    return hashlib.md5(encoded).digest()

