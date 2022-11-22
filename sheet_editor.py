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
    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('hydroponicssheets-8ae54978587b.json', scope)
    client = gspread.authorize(creds)
    hydroponicssheet = client.open("[hydroponics] Information for cool people").worksheet("main")
    return hydroponicssheet

def push_data(ph, ppm):
    hydroponicssheet = give_sheet_connection()
    id = get_next_id_num(hydroponicssheet)
    row = get_next_available_row(hydroponicssheet)
    date_time = get_sheets_date_time(hydroponicssheet)
    #hydroponicssheet.update_cell(row, column, "content")
    hydroponicssheet.update_cell(row, 1, id)
    hydroponicssheet.update_cell(row, 2, date_time)
    hydroponicssheet.update_cell(row, 3, ph)
    hydroponicssheet.update_cell(row, 4, ppm)
    return id
