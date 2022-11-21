import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('hydroponicssheets-8ae54978587b.json', scope)
client = gspread.authorize(creds)
hydroponicssheet = client.open("[hydroponics] Information for cool people").worksheet("main")

#hydroponicssheet.update_cell(row, column, "content")
hydroponicssheet.update_cell(5,5,"New Test!!!")
hydroponicssheet.update_cell(5,6,"New Test!!!")

value = hydroponicssheet.cell(1,1).value
print(value)