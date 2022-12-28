import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_next_id_num(hydroponicssheet):
    #.cell(row, column)
    return hydroponicssheet.cell(1,1).value

def get_next_available_row(hydroponicssheet):
    #.cell(row, column)
    return hydroponicssheet.cell(2,1).value

def get_sheets_date_time(hydroponicssheet):
    #.cell(row, column)
    return hydroponicssheet.cell(2,2).value

def give_sheet_connection():
    print("giving sheet connection")
    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('hydroponicssheets-8ae54978587b.json', scope)
    client = gspread.authorize(creds)
    print("before sheet open")
    hydroponicssheet = client.open("[hydroponics] Information for cool people").worksheet("main")
    print("after sheet open")
    return hydroponicssheet

# updates info given in parameters to google sheet then returns that rows id
def push_data(ph, ppm):
    print("starting push_data")
    hydroponicssheet = give_sheet_connection()
    print("has sheet connection")
    id = get_next_id_num(hydroponicssheet)
    print("has id from sheet")
    row = get_next_available_row(hydroponicssheet)
    date_time = get_sheets_date_time(hydroponicssheet)
    hydroponicssheet.update_cell(row, 1, id)
    print("updated id")
    hydroponicssheet.update_cell(row, 2, date_time)
    hydroponicssheet.update_cell(row, 3, ph)
    hydroponicssheet.update_cell(row, 4, ppm)
    print("updated everything done.")
    return id
