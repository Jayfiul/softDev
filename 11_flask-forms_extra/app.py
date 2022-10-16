#Yusha Aziz
#SoftDev
#K11 -- flask-forms
#2022-10-14
#time spent: 1 hour

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import csv


UsePass = []


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
# myDict = { "Yusha":["Tiny"] , "Brian" : ["Testes"] } #dictionary to hold username and password, where the username is the key

with open('logins.csv') as f: # opens the csv with the combinations
    myDict = f.readlines()

print(myDict)
logins = []  #creates a blank list that is intended to hold the logins from the csv


for i in myDict: #splice list and creates a list of [Usernames,Passwords]
    i = i[:-1]
    i.split(',')
    logins.append(i.split(',')) 

print(logins) #prints the list of logins in the terminal for convenience

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

@app.route("/signUp") #this is for a new function
def signUp(): #this code will change the HTML template from login.html to signUp.html
    return render_template( 'signUp.html' )

@app.route("/register") #this a new path
def register(): #this function will be called when the signUp button is pressed on the console side
    
    #update the list of users and passwords in case someone tries to make two users in a row with the same username without loggging in 
    with open('logins.csv') as f:  
        myDict = f.readlines()

    logins = [] 

    for i in myDict: #code to get an updated list of Usernames and Passwords (in case they made new logins)
        i = i[:-1]
        i.split(',')
        logins.append(i.split(','))
    
    
    print("!!!!!!!!!!!!!! rquestUserNew ~~~~~~~~~~~~")
    print(request.args['username1'])
    user1 = request.args['username1'] #stores the inputted new username request into an easy to read variable
    #code to check if the username already exists
    user = False #if user = False, the username does not exist
    for i in logins:
        if(i[0] == user1): #that means the username is already in the list of Usernames
            user = True
    if(user):
        error = "hi"
        print("\n")
        print("USERNAME EXISTS \n") #code to see it working in the terminal
        return render_template('signUp.html', error = "Username Exists Try Again!") #error code for HTML to run, and start a try again
    
    print("!!!!!!!!!!!!!! rquestPASSnew ~~~~~~~~~~~~")
    print(request.args['password1'])
    pass1 = request.args['password1'] #stores the new password 
    
    print("!!!!!!!!!!!!!! rquestPASSconfirm ~~~~~~~~~~~~")
    print(request.args['password2'])
    pass2 = request.args['password2']  #stores the confirmed password 
    
    if(pass1 != pass2): #checks if the paswswords are matching or not, if they do not match it will bring you back to the signUp page
        print("\n")
        print("PASSWORDS DO NOT MATCH \n")
        return render_template('signUp.html', error= "Passwords Do Not Match Try Again!") #calls the signUp page with the error
    else:
        print("\n")
        print("passwords match!") #message for the coder to see in the terminal to make sure the code is working
        
    with open('logins.csv', 'a', newline='') as c: #opens the CSV file in append mode
        writer = csv.writer(c) #creates a csv writer
        combo = [str(request.args['username1']),str(request.args['password1'])] #stores the new Username, and Passowrd into an Array
        writer.writerow(combo) #It will then append this combination into the csv file, on a new line
    print(combo) #prints the new combination for the reader
    return render_template('login.html') #now that you have added a new combination, you can go back and login
    

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
    with open('logins.csv') as f: 
        myDict = f.readlines()

    logins = [] 

    for i in myDict: #code to get an updated list of Usernames and Passwords (in case they made new logins)
        i = i[:-1]
        i.split(',')
        logins.append(i.split(','))
            
    #code below checks if the username exists
    user = False
    for i in logins:
        if(i[0] == request.args['username']):
            user = True
            UserIndex = i
    if(user == False): #if the username does not exist call the function with the error
        error = "hi"
        print("\n")
        print("WRONG USERNAME \n") #code to see it working in the terminal
        return render_template('login.html', error = "Username Does not Exist, GO BACK") #calls the function with the error
    else:
        print("\n") 
        print("Username is correct")
    if(UserIndex[1] == request.args['password']): #if the password matches the one of the corresponding username it will run
        return "Waaaa hooo HAAAH"  
    else: 
        error = "hi"
        print("\n")
        print("WRONG PASSWORD \n")
        
        return render_template('login.html', error = "Wrong Password HEHEHEHAWWWWW") #calls the HTML file with the error
    # A working username and password will have this url:
    # http://127.0.0.1:5000/auth?username=Yusha&password=Cat&sub1=Submit+Query
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
