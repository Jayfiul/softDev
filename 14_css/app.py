# Bottlers (Jeff Chen, Yusha Aziz, Fang Chen)
# SoftDev
# K14 css
# October 19 2022
# time spent: 0.5 hrs

from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'index.html' )



    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()