import time
import pyperclip
import keyboard
import sqlite3
from datetime import datetime

common_db_path = "clipboard_changes.db"
recent_value = ""

def read_file_on_hotkey(e):
    if keyboard.is_pressed('space+z'):
        # Connect to the SQLite database
        conn = sqlite3.connect(common_db_path)
        cursor = conn.cursor()

        # Retrieve clipboard changes with timestamps from the database
        cursor.execute("SELECT timestamp, content FROM clipboard_changes")
        changes = cursor.fetchall()

        for change in changes:
            timestamp, content = change
            print("Timestamp:", timestamp)
            print("Content:", content)

        conn.close()

keyboard.on_press(read_file_on_hotkey)

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        print("Value changed: %s" % str(recent_value))

        # Save the changed value with timestamp to the SQLite database
        conn = sqlite3.connect(common_db_path)
        cursor = conn.cursor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO clipboard_changes (timestamp, content) VALUES (?, ?)", (timestamp, recent_value))
        conn.commit()
        conn.close()

    time.sleep(0.1)