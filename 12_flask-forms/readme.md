## The Difference Bettwen GET and POST
- GET is when the python code recieves/gets information from HTML
  - When you use GET the request code is differnt: `request.args['variable_name_in_HTML']`
- POST is when the HTML code sends/posts information to the python code to use 
  - When you use the POST method to recieve information the request code is different: `request.form.get('variable_name_in_HTML')` 
- The specific line in the code that determines whether the GET method or POST method is being used is in **line 37** of *login.html*. If the `method = ""` is equal to GET it will use the GET way of displaying information from the USER, and if it is POST, it will use the POST way of displaying the information that the user puts in the local host. 