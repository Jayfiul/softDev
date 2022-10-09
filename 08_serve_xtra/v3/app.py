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
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

'''
Ternminal Output:
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 383-910-936
'''

'''
DISCO:
-   This one has new line of code on line 14
-   app.debug turns on debugging mode, and it allows the coder to
    see where the problems are
-   The debugger pin is a layer of security in case you leave yoru Debug mode on
    it makes it difficult for people to access the debugger
-   The print statements are not instantly printed, you have to reload first
'''