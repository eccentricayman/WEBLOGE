import sqlite3

def auth(username, password, action):
    f = "users.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    if action == "register":
        

