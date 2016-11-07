import sqlite3
from flask import Flask, render_template, session

def myStories():
    myStoryList=[]
    
    f="data.db"
    db=sqlite.connect(f)
    c=db.cursor()

    storyList=c.execute('SELECT name, summary, id FROM stories WHERE updater = %s'%(session['username']))
    
    for story in storyList:
        myStoryList.append([story[0], story[1], story[2]])
        
    return myStoryList
