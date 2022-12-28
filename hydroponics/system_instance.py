import dbAccess
import sqlite3

class system_instance: 
    def __init__(self, id, dateNtime, ph, ppm, color):
        self._id = id
        self._dateNtime = dateNtime
        self._ph = ph
        self._ppm = ppm
        self._color = color

    @property
    def id(self):
        return self._id

    @property
    def dateNtime(self):
        return self._dateNtime

    @property
    def ph(self):
        return self._ph

    @property
    def ppm(self):
        return self._ppm

    @property
    def color(self):
	    return self._color

def importNew(dbConn, id, dateNtime, ph, ppm):
    sqlQ = """Insert into Readings(EntryNumber, Date, pH, PPM)
                values((?), (?), (?), (?));"""

    #Tests for if plate is in the database if not returns 0
    safetyMeasure = """select EntryNumber
        from Readings
        where EntryNumber = (?);"""

    s = dbAccess.selectOneRow(dbConn, safetyMeasure, [id])
    if s:
        return 0
    try:
        dbAccess.performAction(dbConn, sqlQ, [id, dateNtime, ph, ppm])
    except Exception as err:
        print(err)
        return 0

    return 1
