import sqlite3
from flask import Flask, render_template, session

def loadStory(storyID):

    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    storyList = c.execute("SELECT name, id, summary, story FROM stories")

    for story in storyList:
        if (storyID == story[1]):
            return render_template("story.html", name = story[0], summary = story[2], storyText = story[4])
    db.commit()
    db.close()
    return render_template("story.html", notFound = True)
