import tkinter as tk
from tkinter import ttk
import sqlite3



class ClipboardUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Clipboard Changes")
        self.common_db_path = "clipboard_changes.db"


        self.tree = ttk.Treeview(self.master, columns=("Timestamp", "Content"), show="headings")
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.heading("Content", text="Content")
        self.tree.pack()

        self.show_contents()

    def show_contents(self):
        conn = sqlite3.connect(self.common_db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT timestamp, content FROM clipboard_changes")
        changes = cursor.fetchall()
        conn.close()
        sorted_changes = sorted(changes, key=lambda x: x[0], reverse=True)


        for change in sorted_changes:
            self.tree.insert("", "end", values=change)
