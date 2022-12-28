
import time
import sheet_editor
import dbObjects
import datetime
from datetime import date
import sqlite3

#THIS IS A TEST

def uploadToDataBase(id, phLevel, PPMLevel):
    dbConn = sqlite3.connect('dailyReading.db')
    now = datetime.datetime.now()
    dbObjects.importNew(dbConn, id, now, phLevel, PPMLevel)

print("Starting...")
x = 0
while x <= 80:
    # id that was on the google sheet
    time.sleep(5)
    uploadToDataBase(x, 0, 0)
    id = sheet_editor.push_data(x, -1.0)
    print("Updated ID#:",id)
    x = x+1

print("Done!")

