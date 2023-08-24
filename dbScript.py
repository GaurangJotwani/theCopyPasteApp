import sqlite3

db_path = "clipboard_changes.db"

# Connect to the database (this will create a new file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the clipboard_changes table if it doesn't exist
create_table_sql = '''
CREATE TABLE IF NOT EXISTS clipboard_changes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME,
    content TEXT
);
'''
cursor.execute(create_table_sql)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
