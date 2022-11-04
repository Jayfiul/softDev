'''
The Bottlers: Jeff Chen, Fang Min Chen, Yusha Aziz
SoftDev
K19 - Sessions Greetings
4-November-2022
Time spent: 1 hrs
'''
from flask import session, Flask, render_template, request

app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
username = "Bob"
password = "thebuilder"
@app.route('/')
def index():
    if 'username' in session:
        return render_template('response.html', username=session['username'])
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] == username:
        print(request.form['password'])
        if request.form['password'] == password:
            session['username'] = request.form['username']
            print(session['username'])
            print("found")
            return render_template('response.html', username=session['username'])
        #if password is wrong
        return render_template('login.html', error = "wrong password!")
    #if username is wrong
    return render_template('login.html', error = "wrong username!")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username')
    return render_template('login.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

