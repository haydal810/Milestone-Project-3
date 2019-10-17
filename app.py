import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'kerry_rivers'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', "Env Not loaded")
mongo = PyMongo(app)



## HOME page:

@app.route("/")
@app.route("/get_river_names")
def get_river_names():
    return render_template("home.html", rivers=mongo.db.river_names.find())

## HOME page function - to show individual document in collection in db...

@app.route("/show_river_doc")
def show_river_doc():
    return render_template("home.html", river_doc=mongo.db.river_names.find_one())
## Stuck here on above function




## add_river page:

@app.route("/add_new_river")
def add_new_river():
    return render_template("add_river.html", rivers=mongo.db.river_names.find())

## This function adds the form data, on the add_river page, to the database:

@app.route("/insert_river", methods=['POST'])
def insert_river():
    river = mongo.db.river_names
    river.insert_one(request.form.to_dict())
    return redirect(url_for('get_river_names'))



## edit river page:

@app.route("/edit_river")
def edit_river():
    return render_template("update_river.html", rivers=mongo.db.river_names.find())



## leave a review page:

@app.route("/leave_review_river")
def leave_review_river():
    return render_template("leave_review.html", rivers=mongo.db.river_names.find())


## read reviews page:

@app.route("/read_review")
def read_review():
    return render_template("read_review.html", rivers=mongo.db.river_names.find_one())













if __name__ == '__main__':
    app.run(host=os.getenv('IP'), 
    port=int(os.getenv('PORT')), 
    debug=True)
