def gsheet_find(user_name=''):
    data_sheet = get_data_sheet(set_cred())

    cell = data_sheet.find(user_name)
    return_value = '' if cell == None else data_sheet.cell(cell.row, cell.col + 3).value

    return return_value

def gsheet_update(user_name='',password=''):
    data_sheet = get_data_sheet(set_cred())

    cell = data_sheet.find(user_name)
    next_row = next_available_row(data_sheet)

    #insert on the next available row
    if cell == None :
        data_sheet.update_cell(next_row, 1, user_name)
        data_sheet.update_cell(next_row, 4, password)
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
    creds = ServiceAccountCredentials.from_json_keyfile_name('start_up.json',scope)
    return creds

def get_data_sheet(creds):
    #import library
    import gspread

    #create gspread authorize using that credential
    client = gspread.authorize(creds)
    #Now will can access our google sheets we call client.open on 
    data_sheet = client.open('ginnys-data').sheet1
    return data_sheet

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return len(str_list)+1
