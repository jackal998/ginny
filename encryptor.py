import os
import sys
from cryptography.fernet import Fernet

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

key = open(resource_path('_libmaster.pyd'),"rb").read()
f = Fernet(key)

def encrypted(string):
    return f.encrypt(string.encode())

def decrypted(enstring):
    return f.decrypt(enstring.encode()).decode()

def encomp(string, enstring):
    return True if string == decrypted(enstring) else False