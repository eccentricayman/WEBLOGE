from flask import Flask, render_template, request, session, url_for, redirect
import os
import utils.addStory as AS
import utils.auth as auth

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
    return auth.login(session,request)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('username'):
        session.pop('username')
    return redirect(url_for('homepage'))

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
