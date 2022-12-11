
import time
import sheet_editor

#THIS IS A TEST

print("Starting...")
x = 0
while x <= 80:
    # id that was on the google sheet
    time.sleep(5)
    id = sheet_editor.push_data(x, -1.0)
    print("Updated ID#:",id)
    x = x+1

print("Done!")

