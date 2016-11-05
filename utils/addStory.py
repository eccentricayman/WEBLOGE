# stories
# name        id          updater     updates
# ----------  ----------  ----------  ----------

import sqlite3

def addStory(name):

    f = "data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    storyList = c.execute("SELECT name, id FROM stories")
    for story in storyList:
        if (name == story[0]):
            return "Story already exists, choose a different name."
