'''
Team BBY: Yusha Aziz, Brian Chen, Andrew
Soft Dev
K08 -- serve
2022-10-04
time spent: 90 mins
'''

#Big DISCO:
#Debugger Mode means any time you save the file it will auto refresh the flask on http

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

'''
Terminal Output:
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-910-936

'''

'''
DISCO:
-   This code is the same as the one in v3 except for the if statements
-   The purpose of the if statement is to turn on debugger only if the file is in main

'''