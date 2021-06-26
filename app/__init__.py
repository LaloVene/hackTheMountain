from flask import Flask, render_template, send_from_directory, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db
from . import db
import os

# Flask uses load dotenv by default
app = Flask(__name__)

app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.sqlite")

# directories

@app.route("/")
def main():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    return ""

@app.route("/preview")
def preview():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    return ""

@app.route("/topics")
def topics():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    return ""

@app.route("/resources")
def resources():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    return ""

@app.route("/sign-in", methods["POST"])
def sign_in():
    if request.method == "POST":
        username = request.form.get("Username")
        password = request.form.get("Password")
        db = get_db()
        error = None

        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"
        elif db.execute(
            "SELECT * FROM user WHERE Username = ?", (username)
        ).fetchone() != None:
            error = f"user {username} already exists"

        if error == None:
            db.execute(
                "INSERT INTO user (Username,Password) values (?,?)",
                username, generate_password_hash(password))
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    return ""

@app.route("/log-in", methods["POST"])
def log_in():
    if request.method == "POST":
        username = request.form.get("Username")
        password = request.form.get("Password")
        db = get_db()
        error = None

        user = db.execute(
            "SELECT * from user WHERE Username = ?", (username)
        ).fetchone()
        
        if not user:
            error = "Incorrect Username or nonexistent"
        elif not check_password_hash(user["Password"],password):
            error = "Incorrect password"

        if not error:
            return "Successful login", 200
        else:
            return error, 418
            
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    return ""

# ! health directory !
@app.route("/health")
def health():
    return ""