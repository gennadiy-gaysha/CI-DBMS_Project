import os
from flask import Flask

# flask_sqlalchemy is an extension for the Flask framework that enables the
# use of SQLAlchemy to work with databases in Flask applications.
from flask_sqlalchemy import SQLAlchemy
# Since we are not pushing the env.py file to GitHub, this file will not
# be visible once deployed to Heroku, and will throw an error. This is why
# we need to only import 'env' if the OS can find an existing file path for
# the env.py file itself.
if os.path.exists("env.py"):
    import env  # noqa

# Create an instance of the imported Flask() class, which takes the default
# Flask __name__ module. The __name__ variable is a special Python variable
# that refers to the name of the current module or script. In this case,
# __name__ represents the name of the module or script in which this line of
# code is executed.
app = Flask(__name__)

# Specify two app configuration variables, and these will both come from our
# environment variables.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{os.environ.get('123')}@localhost:5433/taskmanager"

# Create an instance of the imported SQLAlchemy() class, and set to the instance
# of our Flask 'app', another words, associates it with the Flask application
# specified by the app variable.
db = SQLAlchemy(app)

from taskmanager import routes  # noqa
