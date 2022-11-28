import time
import sheet_editor

print("Starting...")
x = 1
while x < 10:
    # id that was on the google sheet
    id = sheet_editor.push_data(x, -1.0)
    print("Updated ID#:",id)
    time.sleep(2)
    x = x+1

print("Done!")