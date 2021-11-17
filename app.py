# Imports
import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base

from flask import (
    Flask,
    render_template,
    jsonify,
    redirect)

# Create Engine

engine = create_engine("sqlite:///movies.sqlite")

# Creating new mdoel from Database

Base = automap_base()

# Reflect Tables

Base.prepare(engine, reflect=True)

# Save Reference to table

print(Base.classes.keys())

Movies = Base.classes.movies

###########################
#   Flask Setup
###########################

app = Flask(__name__)


# Flask Website and Pages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model", methods=["POST"])
def model():
    
    ##director = float(request.form["director"])

    score = 7.5
    
    star = float(request.form)["star"]
    
    company = float(request.form["company"])

    genre = float(request.form["genre"])

    budget = request.form["budget"]
    if budget =="":
        budget == 21800000 # Median Budget for Movie

    runtime = request.form["runtime"]
    if run_time == "":
        run_time == 105 # Median Run Time 
    
    run_time = float(runtime)

    prediction = 0

X = [[genre, score, writier, star, budget, company, runtime]]

@app.route("/chart1")
def chart1():
    return render_template("chart1.html")

@app.route("/chart2")
def chart2():
    return render_template("chart2.html")

@app.route("/chart3")
def chart3():
    return render_template("chart3.html")

@app.route("/chart4")
def chart2():
    return render_template("chart4.html")

@app.route("/about")
def record():
    return render_template("about.html")




# Debugger

if __name__ == "__main__":
    app.run(debug=True)