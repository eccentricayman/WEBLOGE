from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)

@app.route('/')
def display():
    if len(session.keys())==0:
        return render_template("home.html")
    else:
        return redirect(url_for('story')

@app.route('/addStory')
def add():
    return render_template("add.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/story')
def myStory():
    ##find num stories for this user on db
    ##render template of user 
    return render_template('story.html', username=request.form['user'])

if __name__ == '__main__':
    app.debug=True
    app.run()
