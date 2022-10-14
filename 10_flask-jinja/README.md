Yusha Aziz
SoftDev
K10 -- flask-jinja
2022-10-13
time spent: 20 mins

Disco:
You cannot just put template filename into url.

render_template renders the template with arguments specified, and has variables within the html

Variables in html in {{ }}

Python code is in {% %}

#Q0: The code cannoy run without the render_template
#Q1: Yes, you just add the extension /my_fois_template
#Q2: The first argument is the name of the template you want to access. 
     For the remaining arguments the order does not matter, the purpose is to designate values for the variables in the HTML