import os
## import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'kerry_rivers'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', "Env Not loaded")
mongo = PyMongo(app)


# Function to load HOME page:

@app.route("/")
@app.route("/get_river_names")
def get_river_names():
    return render_template("home.html", rivers=mongo.db.river_names.find())

# Function to load ABOUT page:


@app.route("/about")
def about():
    return render_template("about.html")

# ADD_RIVER page:


@app.route("/add_new_river")
def add_new_river():
    return render_template("add_river.html")

# This function POSTs the input data from the user, to the database:


@app.route("/insert_river", methods=['POST'])
def insert_river():
    river = mongo.db.river_names
    river.insert_one(request.form.to_dict())
    return redirect(url_for('get_river_names'))


# Function to load UPDATE_RIVER page:

@app.route("/edit_river/<river_id>")
def edit_river(river_id):
    the_river = mongo.db.river_names.find_one({"_id": ObjectId(river_id)})
    return render_template("update_river.html", river=the_river)

# UPDATE_RIVER function - This updates a river's info on the db:

@app.route("/update_river/<river_id>", methods=["POST"])
def update_river(river_id):
    river = mongo.db.river_names
    river.update({'_id': ObjectId(river_id)}, {
        'river_name' : request.form.get('river_name'),
        'status' : request.form.get('status'),
        'fish' : request.form.get('fish'),
        'free_or_permit' : request.form.get('free_or_permit'),
        'angling_methods' : request.form.get('angling_methods')
    })
    return redirect(url_for('get_river_names'))

# delete river record function:

@app.route("/delete_river/<river_id>")
def delete_river(river_id):
    mongo.db.river_names.remove({'_id': ObjectId(river_id)})
    return redirect(url_for('get_river_names'))

# Function to load Review a River page:

@app.route("/leave_review")
def leave_review():
    return render_template("leave_review.html", rivers=mongo.db.river_names.find())




# Function to insert User review to DB:

@app.route("/insert_review", methods=['POST'])
def insert_review():
    review = mongo.db.river_reviews
    review.insert_one(request.form.to_dict())
    return redirect(url_for('read_review'))



# Function to load READ REVIEWS page:

@app.route("/read_review")
def read_review():
    return render_template("read_review.html", reviews=mongo.db.river_reviews.find())


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)