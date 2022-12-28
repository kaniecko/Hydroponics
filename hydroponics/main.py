
import time
import sheet_editor
import dbObjects
import datetime
import ph_tester
from datetime import date
import sqlite3

#THIS IS A TEST

def uploadToDataBase(id, phLevel, PPMLevel):
    dbConn = sqlite3.connect('dailyReading.db')
    now = datetime.datetime.now()
    dbObjects.importNew(dbConn, id, now, phLevel, PPMLevel)

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

