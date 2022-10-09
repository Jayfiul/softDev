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
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

'''
DISCO:
-This one has two print statements
Prints:
about to print __name__...
__main__
'''
