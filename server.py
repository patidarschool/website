from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/index.html")
def world():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/courses.html")
def cources():
    return render_template("courses.html")


@app.route("/pricing.html")
def fees():
    return render_template("pricing.html")


@app.route("/portfolio.html")
def portfo():
    return render_template("portfolio.html")
