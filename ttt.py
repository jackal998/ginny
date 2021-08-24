from google_db import gsheet_find
from google_db import gsheet_update
import bcrypt

passwd = b''

# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(passwd, salt)
# # sheet.update_cell(5, 2, "Nitin Das")
# print(passwd)
# print(salt)
# print(hashed)
# print(hashed.hex())

# gsheet_update("Nitin Das", hashed.hex())

# >>> bytes.fromhex('deadbeef')
# b'\xde\xad\xbe\xef'

r = gsheet_find('ej')
print(r)

if bcrypt.checkpw(passwd, bytes.fromhex(r)):
    print("match")
else:
    print("does not match")
