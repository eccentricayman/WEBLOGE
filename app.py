from flask import Flask, render_template, request, session, url_for, redirect
import os
import sqlite3
import utils.auth as auth
import utils.story as story

app = Flask(__name__)

@app.route('/')
def homepage():
    if session.get('username'):
        stories = story.fetch_stories(session['username'])
        return render_template('homepage.html', user=session['username'], stories=stories)
    stories = story.fetch_stories(None)
    return render_template('homepage.html', stories=stories)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if session.get('username'):
        return story.add_story(session,request)
    return render_template("homepage.html")

@app.route('/update', methods=['GET', 'POST'])
def update():
    if session.get('username'):
        return story.update_story(session, request)
    return redirect(url_for('homepage'))

@app.route('/addstory')
def addstory():
    return render_template("addstory.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return auth.login(session,request)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('username'):
        session.pop('username')
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    if os.path.getsize("data/data.db") == 0:
        f = "data/data.db"
        db = sqlite3.connect(f, check_same_thread=False)
        c = db.cursor()
        print "Initializing database"
        c.execute("CREATE TABLE users (username TEXT, password TEXT, contributedStories TEXT)")
        c.execute("CREATE TABLE stories (title TEXT, id INTEGER, updaters TEXT, updates TEXT)")
        db.commit()
        db.close()
    app.debug=True
    app.secret_key = 'V\xfc\xa5\x04\x8ac\xa9#SU\x02*\x990\x9d\xb9\x08\xe6\xb5\x8d\xb9\xd2\xbe\x93\x94\xf1\xf2W7\xd6"\x0b\xe5\xc3{\xc7{U\xf8\xf4\xbc\xdd\xe6\x01\xea\t\\|<\xce'
    app.run()
