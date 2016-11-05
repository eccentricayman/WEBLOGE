from flask import Flask, render_template, request, session, url_for, redirect
import os
import sqlite3
from hashlib import sha256

app = Flask(__name__)

f = "data/users.db"
db = sqlite3.connect(f, check_same_thread=False)
c = db.cursor()

@app.route('/')
def homepage():
    if session.get('username'):
        return render_template('homepage.html', user=session['username'])
    return render_template('homepage.html')

@app.route('/addStory')
def add():
    return render_template("addStory.html")

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

def register(user, pw):
    c.execute('SELECT * FROM users WHERE username = ?', user)
    if len(list((c))) != 0:
        print "User %s exists" % user
        return False,"Username taken"
    pw = sha256(pw).hexdigest()
    c.execute('INSERT INTO users VALUES (?,?,"")', (user, pw))
    print "Registered successfully"
    return True,"Successfully registered"

def auth_user(user, pw):
    pw = sha256(pw).hexdigest()
    c.execute('SELECT * FROM users WHERE username = ? and password = ?',
            (user, pw))
    if len(list((c))) == 1:
        print "Login successful"
        return True,"Successfully logged in"
    print "Login failed"
    return False,"Bad user/pass combo"

@app.route('/story')
def myStory():
    ##find num stories for this user on db
    ##render template of user 
    return render_template('story.html', username=request.form['user'])

if __name__ == '__main__':
    if os.path.getsize("data/users.db") == 0:
        print "Initializing database"
        c.execute("CREATE TABLE users (username TEXT, password TEXT)")
    app.debug=True
    app.secret_key = 'V\xfc\xa5\x04\x8ac\xa9#SU\x02*\x990\x9d\xb9\x08\xe6\xb5\x8d\xb9\xd2\xbe\x93\x94\xf1\xf2W7\xd6"\x0b\xe5\xc3{\xc7{U\xf8\xf4\xbc\xdd\xe6\x01\xea\t\\|<\xce'
    app.run()
