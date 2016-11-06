import sqlite3
from flask import Flask, render_template, session

def updateStory(storyID, update):
    
    f = "data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("UPDATE stories SET updater = '%s' WHERE id = %d"%(session['username'], storyID))
    c.execute("UPDATE stories SET latest = '%s' WHERE id = %d"%(update, storyID))
    currentStory = c.execute("SELECT story FROM stories WHERE id = %d"%(storyID))[0]
    c.execute("UPDATE stories SET story = '%s' WHERE id = %d"%(currentStory + update, storyID))
