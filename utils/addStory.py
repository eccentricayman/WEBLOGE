# stories table
# name        id          summary     updater     latest     story
# ----------  ----------  ----------  ----------  ---------  --------

import sqlite3
from flask import Flask, render_template, session

def addStory(name, summary, start):

    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    storyList = c.execute("SELECT name, id FROM stories")
    storyID = 0
    
    for story in storyList:
        if (name == story[0]):
            return render_template("addStory.html", message = "Story already exists; choose a different name.")
        storyID = int(story[1])
    c.execute("INSERT INTO stories VALUES ('%s', %d, '%s', %s, %s, %s)"%(name, storyID, summary, session['username'], start, start))

    db.commit()
    db.close()
    return render_template("loadStory.html", id = storyID)


