### Notes:
- When you do http: ... /static/foo, so try to open a text file it tells you  to download that file 
- It also gives a strange response (304), which isn't 200 or 400, for worked  and didn't work

- html is served and displayed like html not plain text, that's why you are not prompted to download the file when its opened

- also a browser probably can't render plain text that's why it tells us to download and open with something that already downloaded on our computer


### Disco:
- when you add folders they end up as another route in your local website, so you can access files in a folder called static at 5000/static/file.html
- also it does not seem like a browser can serve plain text formats, only html


### Q/C/C:
- why doesn't the browser display text files, since even text in html is written in plain text format?
- are some folder names already taken? like some variable names in python are already taken?
