# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import csv


UsePass = []


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
myDict = { "Yusha":["Tiny"] , "Brian" : ["Testes"] } #dictionary to hold username and password, where the username is the key

'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )

@app.route("/signUp")
def signUp():
    return render_template( 'signUp.html' )

@app.route("/register")
def register():
    print("!!!!!!!!!!!!!! rquestUserNew ~~~~~~~~~~~~")
    print(request.args['username1'])
    with open('logins.csv', 'a', newline='') as c: #opens the CSV file in append mode
        writer = csv.writer(c) #creates a csv writer
        combo = [str(request.args['username1']),str(request.args['password1'])]
        writer.writerow(combo)
    print(combo)
    return render_template('login.html')
    

@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***") 
    print(request.args['username']) #this line will print out the username the person typed
    print("***DIAG: request.args['password']  ***")
    print(request.args['password'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    keys = list(myDict.keys())
    user = False
    for i in keys:
        if(i == request.args['username']):
            user = True
    if(user == False):
        error = "hi"
        print("\n")
        print("WRONG USERNAME \n") #code to see it working in the terminal
        return render_template('login.html', error = "Username Does not Exist, GO BACK")
    else:
        print("\n") 
        print("Username is correct")
    if(myDict[request.args['username']][0] == request.args['password']): #this is a passwords maker.
        return "Waaaa hooo HAAAH"  
    else: 
        error = "hi"
        print("\n")
        print("WRONG PASSWORD \n")
        
        return render_template('login.html', error = "Wrong Password HEHEHEHAWWWWW")
    # A working username and password will have this url:
    # http://127.0.0.1:5000/auth?username=Yusha&password=Tiny&sub1=Submit+Query
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
