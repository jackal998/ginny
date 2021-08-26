from google_db import gsheet_update
from encryptor import *

user_name = 'Ginny'
password = '0607'

token = encrypted(password)

gsheet_update(user_name, token.decode())