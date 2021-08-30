from encryptor import *
import json

def gsheet_find(user_name,data_title):
    data_sheet = get_data_sheet(set_cred())
    
    col_idx = find_column(data_sheet, data_title)
    if col_idx == None:
        return "data_title: {} not found.".format(data_title)

    cell = data_sheet.find(user_name)
    return_value = None if cell == None else data_sheet.cell(cell.row, cell.col + col_idx).value

    return return_value

def gsheet_update(user_name,password):
    data_sheet = get_data_sheet(set_cred())

    cell = data_sheet.find(user_name)
    next_row = next_available_row(data_sheet)
    uname_col = find_column(data_sheet, 'user_name') + 1
    pwd_col =  find_column(data_sheet, 'password') + 1

    #insert on the next available row
    if cell == None :
        data_sheet.update_cell(next_row, uname_col, user_name)
        data_sheet.update_cell(next_row, pwd_col, password)
        return_value = 'new user: ' + user_name + ' ok.'
    else :
        data_sheet.update_cell(cell.row, 4, password)
        return_value = 'update user: ' + user_name + ' ok.'

    return return_value

def set_cred():
    #Service client credential from oauth2client
    from oauth2client.service_account import ServiceAccountCredentials
    # Print nicely
    # import pprint
    # pp = pprint.PrettyPrinter()

    #Create scope
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    #create some credential using that scope and content of start_up.json
    encrypted_api = open(resource_path('google_api.key'),"r").read()
    api_json = json.loads(decrypted(encrypted_api))

    creds = ServiceAccountCredentials.from_json_keyfile_dict(api_json, scope)
    return creds

def get_data_sheet(creds):
    #import library
    import gspread

    #create gspread authorize using that credential
    client = gspread.authorize(creds)
    #Now will can access our google sheets we call client.open on 
    data_sheet = client.open('ginnys-data').sheet1
    return data_sheet

def find_column(data_sheet, data_title) :
    column_list = data_sheet.row_values(1)
    for idx, val in enumerate(column_list):
        if val == data_title:
            return idx 

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return len(str_list)+1
