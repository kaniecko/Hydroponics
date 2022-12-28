
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
    print("uploaded to database")

print("Starting...")
x = 0
while x <= 20:
    # id that was on the google sheet
    time.sleep(5)
    ph = ph_tester.get_ph()
    id = sheet_editor.push_data(ph, -1.0)
    uploadToDataBase(id, ph, 0)
    print("Updated ID#:",id)
    x = x+1

print("Done!")

