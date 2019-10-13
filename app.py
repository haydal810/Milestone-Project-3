import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'kerry_rivers'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', "Env Not loaded")

mongo = PyMongo(app)

## This is the function for the home page:
@app.route("/")
@app.route("/get_river_names")
def get_river_names():
    return render_template("rivers.html", rivers=mongo.db.river_names.find())

## This is the function for the edit river page:
@app.route("/")
@app.route("/edit_river")
def edit_river():
    return render_template("edit_river.html", rivers=mongo.db.river_names.find())



## This is the function for the review page:
@app.route("/")
@app.route("/review_river")
def review_river():
    return render_template("review.html", rivers=mongo.db.river_names.find())



## This is the function for the review page:
@app.route("/")
@app.route("/add_new_river")
def add_new_river():
    return render_template("add_river.html")




if __name__ == '__main__':
    app.run(host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)






