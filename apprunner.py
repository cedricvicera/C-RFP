from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

#home page
@app.route("/")
def home():
    return render_template("index.html")

#form page: to get user input
@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        sex = request.form.get("sex")
        age = request.form.get("age")
        race = request.form.get("race")
        print(sex, age, race)  #will be replaced to data processing methods
        return redirect("/") #will be replaced to result page
    else:
        return render_template("form.html")

#result page
@app.route("/results")
def results():
    return render_template("results.html")

if __name__== "__main__":
    app.run(debug=True)
