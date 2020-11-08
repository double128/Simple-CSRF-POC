# Simple CSRF Proof of Concept

### Introduction
This is a simple proof of concept for a CSRF attack made with Flask.

### Instructions
1. Create a Python3 virtual environment with `python3 -m venv venv`. Make sure you have `python3-venv` installed. 
2. Initialize the database with the following commands: 

```
$ flask db init
$ flask db migrate -m "first commit"
$ flask db upgrade
```

3. Start the webserver with `./run.sh`. It should be accessible via your server's LAN IP on port 5000 now (ie. http://10.0.0.127:5000).
4. Register two users, with one being named whatever you want, and the other being named "hacker.man" with a password of "cisco123". 
5. In `config.py`, set `SECURE` to `False`. This will prevent Flask-WTF from generating CSRF tokens for forms.
6. Edit `fake_login_page.html` and change the IP address inside the `<form>` tag to your own server's IP address.
7. Open the HTML file in a browser.
8. ???
9. Profit!

### What does this prove
Putting it as simply as possible, this proves why CSRF tokens exist in the first place. If you try to follow the same steps but with `SECURE` set to `True`, instead of the form being submitted automatically when opening the HTML file (simulating a victim clicking on a malicious link), it will throw an error and tell the user that there is a "missing CSRF token". 

Also notice that if you log in as the other user you created, as soon as you open the HTML file, you'll now be logged in as "hacker.man" instead.

### Credits
Thanks to Miguel Grinberg's [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for helping remind me how to set up Flask for what is possibly the 100th time.

Additional thanks go out to [this article here](https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/cross-site-request-forgery-in-login-form/), which I designed my POC around.
