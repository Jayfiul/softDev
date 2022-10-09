'''
Team BBY: Yusha Aziz, Brian Chen, Andrew
Soft Dev
K08 -- serve
2022-10-04
time spent: 90 mins
'''

from flask import Flask
app = Flask(__name__) # ...

@app.route("/") # ...
def hello_world():
    print(__name__) # ...
    return "No hablo queso!"  # ...

app.run()  # ...
                
