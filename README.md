# BrandonCodeSample

This is a simple python log in app that displays a home page and authenticates a user.  The app is not currently functional - there are a few issues I need to resolve involving the Bcrypt library and text encoding to ensure that the user password is stored securely.  The app works without a secure password, though.

The app has three main routes:

```code
/ (root)
```
This route is the home route and has a simple login page.  This allows a user to post their username/password to the web application to be authenticated.

```code
/login
```
This route is where the username/password are posted to from the web application.  Once they are posted, the app attempts to validate the username and password hash against what is contained in the database.

```code
/logout
```
This route is a simple GET request to the path to reset the user's session.

You will need Python and Pip installed to run this application.

This application was tested/created using Python 3.6, so please follow the installation instructions for your operating system for Python 3.6 from the url below:
```
https://www.python.org/downloads/
```

The following dependencies are required to run this application:
```
flask
sqlalchemy
flask_bcrypt (encrypted version)
import os

To install them, simply use:
pip install flask
pip install sqlalchemy
pip install flask_bcrypt

if pip is not installed, please see https://pip.pypa.io/en/stable/installing/ for installing pip to manage your Python libraries.
```

To use this application, follow the instructions below:

Clone down this repository
```
git clone git@github.com:boveus/BrandonCodeSample.git
cd BrandonCodeSample
git checkout -b non-encrypted
git pull origin non-encrypted (these steps are neccesary to run this app from the non-encrypted login branch.  The encrypted login is currently not working.)
```
Navigate to the repository file directory (it should be a directory that was created when you ran the git clone commany) and run the following commands
```
python maketables.py (This will create a sqllite DB)
python makeusers.py (This will create a user in the DB)
python app.py (This will launch the server)
```
Once python app.py is running, you should see a something similar to the message below:
```
* Running on http://0.0.0.0:4000/ (Press CTRL+C to quit)
```
In a web browser, navigate to localhost:4000 and you should see a login screen.

You can log in with 'test_user' as the username and 'password' as the password and logout by clicking on the 'logout' button.
