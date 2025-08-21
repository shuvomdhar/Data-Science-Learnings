from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # For single user
    """if username == "shuvom123" and password == "pass":
        return render_template("welcome.html", name = username)"""
    
    # For multiple users
    valid_users = {
        'admin':'123',
        'shuvom123':'pass',
        'rajat':'raj'
    }
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html", name = username)
    else:
        return "Invalid Credentials"