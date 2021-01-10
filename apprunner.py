from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/form", methods=["POST", "GET"])
def getinput():
    sex = request.form.get("sex")
    age = request.form.get("age")
    race = request.form.get("race")
    print(sex, age, race)
    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__== "__main__":
    app.run(debug=True)
