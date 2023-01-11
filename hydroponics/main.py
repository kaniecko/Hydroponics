import time
import sheet_editor
import system_instance
import datetime
import ph_tester
from datetime import date
import sqlite3

def uploadToDataBase(id, phLevel, PPMLevel):
    dbConn = sqlite3.connect('dailyReading.db')
    now = datetime.datetime.now()
    system_instance.importNew(dbConn, id, now, phLevel, PPMLevel)

try:
    hydroponicssheet = sheet_editor.give_sheet_connection()
    while True:
        print("Starting Wait...")
        time.sleep(5)
        print("Wait is done...")
        ph = ph_tester.get_ph()
        print("the ph retrieved is:",f"{ph:.2f}")
        # id that was on the google sheet
        id = sheet_editor.push_data(ph, hydroponicssheet)
        print("sheet updated with id#:",id)
        uploadToDataBase(id, ph, 0)
        print("database updated with id#:",id)
except:
    print("There was an error.")
finally:
    print("Done!")

