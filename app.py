import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'kerry_rivers'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', "Env Not loaded")

mongo = PyMongo(app)


# This is the function for the home page:
@app.route("/")
@app.route("/get_river_info")
def get_river_info():
    return render_template("home.html", rivers=mongo.db.river_names.find())


# This function adds the form data, on the add_river page, to the database:


@app.route("/insert_river", methods=['POST'])
def insert_river():
    rivers = mongo.db.river_names
    rivers.insert_one(request.form.to_dict())
    return redirect(url_for('get_river_info'))


# This is the function for the update river page:

@app.route("/update_river/<river_id>")
def update_river(river_id):
    the_river = mongo.db.river_names.find_one({"_id": ObjectId(river_id)})
    return render_template("update_river.html", river=the_river)


# This is the function for the leave a review page:

@app.route("/leave_review")
def leave_review():
    return render_template("leave_review.html", rivers=mongo.db.river_names.find())


# This is the function for the read_review page:

@app.route("/read_review")
def read_review():
    return render_template("read_review.html",
                           rivers=mongo.db.river_names.find())


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT')),
            debug=True)
