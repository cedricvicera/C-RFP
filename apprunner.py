from flask import Flask, redirect, url_for, render_template, request
from filereader import file_reader
from riskcalculator import filter_df, calculator

# Press the green button in the gutter to run the script.
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
        print(sex, age, race)  #will be replaced with data processing methods, delete later
        df_filter = df.copy()
        df_filter = filter_df(df, sex, age, race)
        print("filtered df")
        print(df_filter)
        result = str(calculator(df_filter))
        print(result)
        return render_template("result.html", number=result)  #need to add a placeholder in result.html
    else:
        return render_template("form.html")

#result page
@app.route("/result")
def result():
    return render_template("result.html")

if __name__== "__main__":
    file_name = 'COVID-19_Case_Surveillance_Public_Use_Data.csv'
    df = file_reader(file_name)
    app.run(debug=True)
