'''
Team BBY: Yusha Aziz, Brian Chen, Andrew
Soft Dev
K08 -- serve
2022-10-04
time spent: 90 mins
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

'''
Terminal Output:
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
'''


'''
DISCO:
-This one does not have "print(_name_)
-It only returns No hablo queso! on the https

'''