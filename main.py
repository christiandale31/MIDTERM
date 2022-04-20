from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Index
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Login
@app.route("/login/", methods=["GET"])
def login():
    return render_template("login.html")

# Register
@app.route("/register/", methods=["GET"])
def register():
    return render_template("register.html")

if __name__=="__main__":
    app.run()