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

@app.route("/edit_river")
def edit_river():
    return render_template("edit_river.html", rivers=mongo.db.river_names.find())



## This is the function for the leave a review page:

@app.route("/review_river")
def review_river():
    return render_template("review.html", rivers=mongo.db.river_names.find())


## This is the function for the river_review page:

@app.route("/river_review")
def river_review():
    return render_template("river_review.html", rivers=mongo.db.river_names.find())




## This is the function for the add_river page:

@app.route("/add_new_river")
def add_new_river():
    return render_template("add_river.html", rivers=mongo.db.river_names.find())


## This function adds the form data to the database:

@app.route("/insert_river", methods=['POST'])
def insert_river():
    rivers = mongo.db.river_names
    rivers.insert_one(request.form.to_dict())
    return redirect(url_for('get_river_names'))








if __name__ == '__main__':
    app.run(host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)






