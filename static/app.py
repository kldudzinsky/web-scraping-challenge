from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import mars_scrape
import sys
app = Flask(__name__)
app.config["MONGO_URI"]='mongodb://localhost:27017/mars_db'
mongo=PyMongo(app)

@app.route("/")
def index():
    mars_data=mongo.db.mars.find_one()
    return render_template("index.html",mars_data=mars_data)
@app.route("/")
def scrape()
    mars_scrape= scrape_mars.scrape()
    mongo.db.mars.update({},mars_scrape, upset=True)

    return redirect("/", code=302)
if __name__="_main_":
    app.run(debug=True)
    