DISCO: 
Cookies are created and stored using session['<something>'], and will be saved until they are cleared by the browser. 
To remove a cookie, use session.pop('<something'>]
Cookies can be accessed by the site as long as the secret key is the same
Q/C/C:
How is the secret key used by the site? 
Are secret keys ever changed?
What happens when secret keys are changed?
Is it difficult to decrypt secret keys?

It seems like cookies are very similar to a tuple?