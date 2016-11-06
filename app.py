from flask import Flask, render_template, request, session, url_for, redirect
import os
import sqlite3
from hashlib import sha256
import utils.addStory as AS

app = Flask(__name__)

@app.route('/')
def homepage():
    if session.get('username'):
        return render_template('homepage.html', user=session['username'])
    return render_template('homepage.html')

@app.route('/addStory')
def add():
    return render_template("addStory.html")

@app.route("/loadStory", methods = ['GET', 'POST'])
def loadS():
    AS.addStory(request.form['name'], request.form['summary'], request.form['start'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('homepage'))
    #print request.form
    try:
        username = request.form['username']
        password = request.form['password']
    except:
        return render_template('homepage.html', error=True, msg="Error.")
    #print username
    #print password
    if request.form.get("register"):
        valid,msg = register(username, password)
        return render_template('homepage.html', error=not valid, msg=msg)
    if request.form.get("login"):
        valid,msg = auth_user(username, password)
        if valid:
            session['username'] = username
            return render_template("homepage.html", error=not valid, msg=msg, user=username)
        return render_template("homepage.html", error=not valid, msg=msg)
    return render_template("homepage.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('username'):
        session.pop('username')
    return redirect(url_for('homepage'))

def register(user, pw):
    f = "data/data.db"
    db = sqlite3.connect(f, check_same_thread=False)
    c = db.cursor()

    c.execute('SELECT * FROM users WHERE username = ?', user)
    if len(list((c))) != 0:
        print "User %s exists" % user
        db.close()
        return False,"Username taken"
    pw = sha256(pw).hexdigest()
    c.execute('INSERT INTO users VALUES (?,?,"")', (user, pw))
    db.commit()
    db.close()
    print "Registered successfully"
    return True,"Successfully registered"

def auth_user(user, pw):
    f = "data/data.db"
    db = sqlite3.connect(f, check_same_thread=False)
    c = db.cursor()

    pw = sha256(pw).hexdigest()
    c.execute('SELECT * FROM users WHERE username = ? and password = ?',
            (user, pw))
    if len(list((c))) == 1:
        db.close()
        print "Login successful"
        return True,"Successfully logged in"
    db.close()
    print "Login failed"
    return False,"Bad user/pass combo"

@app.route('/story')
def myStory():
    ##find num stories for this user on db
    ##render template of user 
    return render_template('story.html', username=request.form['user'])

if __name__ == '__main__':
    if os.path.getsize("data/data.db") == 0:
        f = "data/data.db"
        db = sqlite3.connect(f, check_same_thread=False)
        c = db.cursor()
        print "Initializing database"
        c.execute("CREATE TABLE users (username TEXT, password TEXT, contributedStories TEXT)")
        db.commit()
        db.close()
    app.debug=True
    app.secret_key = 'V\xfc\xa5\x04\x8ac\xa9#SU\x02*\x990\x9d\xb9\x08\xe6\xb5\x8d\xb9\xd2\xbe\x93\x94\xf1\xf2W7\xd6"\x0b\xe5\xc3{\xc7{U\xf8\xf4\xbc\xdd\xe6\x01\xea\t\\|<\xce'
    app.run()
