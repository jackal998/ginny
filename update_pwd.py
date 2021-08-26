from google_db import gsheet_update
from encryptor import *

user_name = 'Ginny'
password = ''

token = encrypted(password)

gsheet_update(user_name, token.decode())