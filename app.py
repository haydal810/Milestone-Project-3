import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'kerry_rivers'
app.config["MONGO_URI"] = 'mongodb+srv://haydal810:Glencar234@myfirstcluster-me2gf.mongodb.net/kerry_rivers?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_river_names")
def get_river_names():
    return render_template("rivers.html", rivers=mongo.db.river_names.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
