import os
from flask import (
    Flask, flash, render_template,
    request, redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    news = list(mongo.db.news.find().sort("date", 1).limit( 1 ))
    games = list(mongo.db.games.find().limit( 3 ))
    return render_template("index.html", news=news, games=games)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # error flash if they exist
        if existing_user:
            flash("Username already exists, please try again.")
            return redirect(url_for("register"))

        # store them in session and update db if they don't already exist
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # gather user info from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # gather list of reviews by user
    reviews = list(mongo.db.reviews.find(
        { "created_by": session["user"]}))
    if session["user"]:
        return render_template("profile.html", username=username, reviews=reviews)

    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))

            else:
                # invalid password
                flash("incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username missmatch
            flash("incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/delete_review/<review_id>")
def delete_task(task_id):
    mongo.db.review.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("profile.html", username=username, reviews=reviews))


@app.route("/games")
def games():
    games = list(mongo.db.games.find())
    return render_template("games.html", games=games)


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        game = {
            "name": request.form.get("name"),
            "genre": request.form.get("genre"),
            "description": request.form.get("description"),
            "img_url": request.form.get("img_url"),
            "affiliate_link": request.form.get("img_url")
        }
        mongo.db.games.insert_one(game)
        flash("Game Successfully Added")
        return redirect(url_for("games"))

    genres = mongo.db.genres.find().sort("name", 1)
    return render_template("add_game.html", genres=genres)


@app.route("/genres")
def genres():
    genres = list(mongo.db.genres.find())
    return render_template("genres.html", genres=genres)


@app.route("/news")
def news():
    news = list(mongo.db.news.find())
    return render_template("news.html", news=news)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)