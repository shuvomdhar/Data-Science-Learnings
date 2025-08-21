from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "profile.html", 
        name="Arun", 
        is_topper=True,
        subjects=["Maths", "Science", "History"],
    )