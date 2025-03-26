from flask import Flask , Blueprint , render_template

routes = Blueprint('routes' , __name__)


@routes.route("/")
def base():
    return render_template("index.html")


@routes.route("/login")
def login():
    return render_template("auth/login.html")


@routes.route("/register")
def register():
    return render_template("auth/register.html")

routes.route("/about")
def about():
    return render_template("about.html") 