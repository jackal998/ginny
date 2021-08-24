from google_db import gsheet_update
import bcrypt

user_name = 'ej'
passwd = b''

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)
gsheet_update(user_name, hashed.hex())