from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/feedback", methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username") # request.form["key"] -> if the key does not exist then it will throw an error and the app can crash and the get returns "none" it the username does not exists
        message = request.form.get("message")

        return render_template("thankyou.html", user=name, message=message)
    
    return render_template("feedback.html")