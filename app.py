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
    

    score = 7.5

    budget = request.form["budget"]
    if budget =="":
        budget == 21800000 # Median Budget for Movie

    runtime = request.form["runtime"]
    if run_time == "":
        run_time == 105 # Median Run Time
        runtime = float(runtime)
    
    genre = request.form["genre"]
    if genre_Action == 0:
        genre = ""
    elif genre_Action == 1:
        genre == "Action"
    if genre_Adventure == 0:
        genre = ""
    elif genre_Adventure == 1:
        genre = "Adventure"
    if genre_Animation == 0:
        genre = ""
    elif genre_Animation == 1:
        genre = "Aniumation"
    if genre_Biography == 0:
        genre = ""
    elif genre_Biography == 1:
        genre = "Biography"
    if genre_Comedy == 0:
        genre = ""
    elif genre_Comedy == 1:
        genre = "Comedy"
    if genre_Crime == 0:
        genre = ""
    elif genre_Crime == 1:
        genre = "Crime"
    if genre_Drama == 0:
        genre = ""
    elif genre_Drama == 1:
        genre = "Drama"
    if genre_Horror == 0:
        genre = ""
    elif genre_Horror == 1:
        genre = "Horror"
    if genre_Other == 0:
        genre = ""
    elif genre_Other == 1:
        genre = "Other"
    
    writer = request.form["writer"]
    if writer_JoelCoen == 0:
        writer = ""
    elif writer_JoelCoen == 1:
        writer = "Joel Coen"
    if writer_JohnHughes == 0:
        writer = ""
    elif writer_JohnHughes == 1:
        writer = "John Hughes"
    if writer_LucBesson== 0:
        writer = ""
    elif writer_LucBesson == 1:
        writer = "Luc Besson"
    if writer_StephenKing == 0:
        writer = ""
    elif writer_StephenKing == 1:
        writer = "Stephen King"
    if writer_WesCraven == 0:
        writer = ""
    elif writer_WesCraven == 1:
        writer = "Wes Craven"
    if writer_WoodyAllen == 0:
        writer = ""
    elif writer_WoodyAllen == 1:
        writer = "Woody Allen"
    if writer_other == 0:
        writer = ""
    elif writer_other == 1:
        writer = "Other"
    
    star = request.form["star"]
    if star_AdamSandler == 0:
        star = ""
    elif star_AdamSandler == 1:
        star = "Adam Sandler"
    if star_ArnoldSchwarzenegger == 0:
        star = ""
    elif star_ArnoldSchwarzenegger == 1:
        star = "Adam Sandler"
    if star_BruceWillis == 0:
        star = ""
    elif star_BruceWillis == 1:
        star = "Bruce Willis"
    if star_DenzelWashington == 0:
        star = ""
    elif star_DenzelWashington == 1:
        star = "Denzel Washington"
    if star_EddieMurphy == 0:
        star = ""
    elif star_EddieMurphy == 1:
        star = "Eddie Murphy"
    if star_HarrisonFord == 0:
        star = ""
    elif star_HarrisonFord == 1:
        star = "Harrison Ford"
    if star_JohnTravolta == 0:
        star = ""
    elif star_JohnTravolta == 1:
        star = "John Travolta"
    if star_JohnnyDepp == 0:
        star = ""
    elif star_JohnnyDepp == 1:
        star = "Johnny Depp"
    if star_KeanuReeves == 0:
        star = ""
    elif star_KeanuReeves == 1:
        star = "Keanu Reeves"
    if star_KevinCostner == 0:
        star = ""
    elif star_KevinCostner == 1:
        star = "Kevin Costner"
    if star_MattDamon == 0:
        star = ""
    elif star_MattDamon == 1:
        star = "Matt Damon"
    if star_MatthewMcConaughey == 0:
        star = ""
    elif star_MatthewMcConaughey == 1:
        star = "Matthew McConaughey"
    if star_MelGibson == 0:
        star = ""
    elif star_MelGibson == 1:
        star = "Mel Gibson"
    if star_NicolasCage == 0:
        star = ""
    elif star_NicolasCage == 1:
        star = "Nicolas Cage"
    if star_RoberDeNiro == 0:
        star = ""
    elif star_RobertDeniro == 1:
        star = "Robert De Niro"
    if star_SylvesterStallone == 0:
        star = ""
    elif star_SylvesterStallone == 1:
        star = "SylvesterStallone"
    if star_TomCruise == 0:
        star = ""
    elif star_TomCruise == 1:
        star = "Tom Cruise"
    if star_TomHanks == 0:
        star = ""
    elif star_TomHanks == 1:
        star = "Tom Hanks"
    if star_other == 0:
        star = ""
    elif star_other == 1:
        star = "Other"

    
    company = request.form["company"]
    if company_ColumbiaPictures == 0:
        company  = ""
    elif company_ColumbiaPictures == 1:
        company = "Columbia Pictures"
    if company_DimensionFilms == 0:
        company  = ""
    elif company_DimensionFilms == 1:
        company = "Dimension Films"
    if company_DreamworksPictures == 0:
        company  = ""
    elif company_DreamworksPictures == 1:
        company = "Deamworks Pictures"
    if company_Fox2000Pictures == 0:
        company  = ""
    elif company_Fox2000Pictures == 1:
        company = "Fox 2000 Pictures"
    if company_Lionsgate == 0:
        company  = ""
    elif company_Lionsgate == 1:
        company = "Lionsgate"
    if company_Metro-Goldwyn-Mayer(MGM) == 0:
        company  = ""
    elif company_Metro-Goldwyn-Mayer(MGM) == 1:
        company = "Metro-Goldwny-Mayer (MGM)"
    if company_Miramax == 0:
        company  = ""
    elif company_Miraxmax == 1:
        company = "Miramax"
    if company_NewLineCinema == 0:
        company  = ""
    elif company_NewLineCiema == 1:
        company = "New Line Cinema"
    if company_ParamountPictures== 0:
        company  = ""
    elif company_ParamountPictures == 1:
        company = "ParamountPictures"
    if company_ScreenGems == 0:
        company  = ""
    elif company_ScreenGems == 1:
        company = "Screen Gems"
    if company_SummitEntertainment == 0:
        company  = ""
    elif company_SummitEntertainment == 1:
        company = "Summit Entertainment"
    if company_TouchstonePictures == 0:
        company  = ""
    elif company_TouchstonePictures == 1:
        company = "Touchstone Pictures"
    if company_TriStarPictures == 0:
        company  = ""
    elif company_TriStarPictures == 1:
        company = "TriStar Pictures"
    if company_TwentiethCenturyFox == 0:
        company  = ""
    elif company_TwentiethCenturyFox == 1:
        company = "Twentieth Century Fox"
    if company_UniversalPictures == 0:
        company  = ""
    elif company_UniversalPictures == 1:
        company = "Universal Pictures"
    if company_WaltDisneyPictures == 0:
        company  = ""
    elif company_WaltDisneyPictures == 1:
        company = "Walt Disney Pictures"
    if company_WarnerBros == 0:
        company  = ""
    elif company_WarnerBros == 1:
        company = "Warner Bros."
    if company_other == 0:
        company  = ""
    elif company_other == 1:
        company = "Other"

    prediction = 0

    X = [[score, budget, runtime, genre, writer,  star,  company,]]

    return render_template("model.html", prediction = prediction)

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