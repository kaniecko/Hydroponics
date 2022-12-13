import sqlite3

#Select one row of information
def selectOneRow(dbConn, sql, parameters=None):
    if parameters is None:
        parameters = []

    dbCursor = dbConn.cursor()
    try:
        dbCursor.execute(sql, parameters)
        row = dbCursor.fetchone()
        if row is None:
            return ()
        else:
            return row
    except Exception as err:
        print("selectOneRow failed:", err)
        return None
    finally:
        dbCursor.close()

 #Select multiple rows of information
def select_n_rows(dbConn, sql, parameters=None):
    if parameters is None:
        parameters = []

    dbCursor = dbConn.cursor()

    try:
        dbCursor.execute(sql, parameters)
        rows = dbCursor.fetchall()
        if rows is None:
            return []
        else:
            return rows
    except Exception as err:
        print("select_n_rows failed:", err)
        return None
    finally:
        dbCursor.close()



def performAction(dbConn, sql, parameters=[]): #Updates DB
    dbCursor = dbConn.cursor()
    try:
        dbCursor.execute(sql, parameters)
        dbConn.commit()
        return dbCursor.rowcount
    except Exception as err:
        print("perform_action failed:", err)
        return -1
    finally:
        dbCursor.close()