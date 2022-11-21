from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import json
import requests


app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

f = open("key_nasa.txt", "r")
keyNasa = f.read() 

print(keyNasa)

@app.route("/") 
def hello_world():
    return render_template('main.html', key = keyNasa) 

app.run()  # Q5: Where have you seen similar constructs in other languages?
