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

@app.route("/", methods=["POST"])
def model():
    

    score = 7.5
    X_list = []
    X_list.append(score)

    budget = request.form["budget"]
    if budget =="":
        budget == 21800000 # Median Budget for Movie
    X_list.append(budget)
    
    runtime = request.form["runtime"]
    if run_time == "":
        run_time == 105 # Median Run Time
        runtime = float(runtime)
    X_list.append(runtime)

    genre = request.form["genre"]
    if genre == "Action":
        X_list.append(1)
    else:
        X_list.append(0)
    if genre == "Adventure":
        X_list.append(1)
    else:
        X_list.append(0)
    if genre == "Animation":
        X_list.apped(1)
    else:
        X_list.append(0)
    if genre == "Biography":
        X_list.append(1)
    else:
        X_list.apped(0)
    if genre == "Comedy":
        X_list.append(1)
    else:
       X_list.append(0)
    if genre == "Crime":
        X_list.append(1)
    else:
        X_list.append(0)
    if genre == "Drama":
        X_list.append(1)
    else:
        X_list.append(0)
    if genre == "Horror":
        X_list.append(1)
    else:
        X_list.append(0)
    if genre == "Other":
        X_list.append(1)
    else:
        X_list.append(0)
    
    writer = request.form["writer"]
    if writer == "Joel Coen":
        X_list.append(1)
    else:
        X_list.append(0)
    if writer == "John Hughes":
        X_list.append(1)
    else:
        X_list.append(0)
    if writer == "Luc Besson":
        X_list.append(1)
    else:
        X_list.append(0)
    if writer =="Stephen King":
        X_list.append(1)
    else:
        X-list.append(0)
    if writer == "Wes Craven":
        X_list.append(1)
    else:
        X_list.append(0)
    if writer == "Woody Allen":
        X_list.append(1)
    else:
        X_list.append(0)
    if writer == "Other":
        X_list.append(1)
    else:
        X_list.append(0)
    
    star = request.form["star"]
    if star == "Adam Sandler":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Arnold Schwarzenegger":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Bruce Willis":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Denzel Washington":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Eddie Murphy":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Harrison Ford":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "JohnTravolta":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Johnny Depp":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Keanu Reeves":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Kevin Costner":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Matt Damon":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Matthew McConaughey":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Mel Gibson":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Nicolas Cage":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Robert De Niro":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Sylvester Stallone":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Tom Cruise":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Tom Hanks":
        X_list.append(1)
    else:
        X_list.append(0)
    if star == "Other":
        X_list.append(1)
    else:
        X_list.append(0)

    
    company = request.form["company"]
    if company == "Columbia Pictures":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Dimension Films":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Dreamworks Pictures":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Fox 2000 Pictures":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Lionsgate":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Metro-Goldwyn-Mayer(MGM)":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Miramax":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "New Line Cinema":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Paramount Pictures":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Screen Gems":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Summit Entertainment":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Touchstone Pictures":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "TriStar Pictures":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Twentieth Century Fox":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Universal Pictures":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Walt Disney Pictures":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Warner Bros":
        X_list.append(1)
    else:
        X_list.append(0)
    if company == "Other":
        X_list.append(1)
    else:
        X_list.append(0)

    prediction = 0

    X = [X_list]

    print(X)

    filename = './model/movies_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    prediction = loaded_model.predict(X)[0][0]

    return render_template("index.html", prediction = prediction)


# Debugger

if __name__ == "__main__":
    app.run(debug=True)