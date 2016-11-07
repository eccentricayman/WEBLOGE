import sqlite3
from flask import Flask, render_template

def myStories(session['username']):
    myStoryList=[]
    f="data.db"
    db=sqlite.connect(f)
    c=db.cursor()
    storyList=c.execute('SELECT * FROM stories WHERE updater==session["username"]')
    for story in storyList:
        if(session['username'] == story[4]):
            myStoryList.append(story[0])
    return myStoryList
