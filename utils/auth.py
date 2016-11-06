# users.db
# username    password    contributedStories
# ----------  ----------  ------------------

import sqlite3
import hashlib

def auth(username, password, action):
    
    f = "users.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    
    if action == "register":
        userData = c.execute("SELECT username FROM users")
        for user in userData:
            if (username == user[0]):
                return "Username already taken."
        c.execute("INSERT INTO users VALUES ('%s', '%s', '%s')"%(username, hashlib.sha256(password).hexdigest(), ""))
    elif action == "login":
        userData = c.execute("SELECT username, password FROM users");
        for user in userData:
            if (username == user[0]):
                if (hashlib.sha256(password).hexdigest() == user[1]):
                    return "Logged in."
                else:
                    return "Incorrect password."
        return "User not found."
        
