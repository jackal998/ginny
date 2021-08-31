from google_db import gsheet_update
from encryptor import *

user_name = 'Adam'
password = 'ppp'

token = encrypted(password)

gsheet_update(user_name, 'password', token.decode())