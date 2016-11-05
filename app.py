from flask import Flask, render_template, request, session, url_for, redirect
from auth.py import auth;

app = Flask(__name__)

@app.route('/')
def display():
    if len(session.keys())==0:
        return render_template("login.html")
    else:
        return redirect(url_for('genFeed.html'))
                        
@app.route('/addStory')
def add():
    return render_template("addStory.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/authenticate", methods=['GET', 'POST'])
def authenticate():
    authStr = auth(request.form['username'], request.form['password'], request.form['action'])
    if authStr == "Logged in.":
        session['username'] = request.form['username']
    return render_template("login.html", message = authStr)
    
@app.route('/story')
def myStory():
    ##find num stories for this user on db
    ##render template of user 
    return render_template('story.html', username=request.form['user'])

if __name__ == '__main__':
    app.debug=True
    app.run()
