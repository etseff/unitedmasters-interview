import validators
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from models.storage import Storage

app = Flask(__name__)

# Initialize instance of Storage used through the life of the process.
store = Storage()

@app.route("/")
def index():
    return render_template("url/home.html")

@app.route("/generate", methods=("GET", "POST"))
def generate():
    if request.method == "POST":
        long_url = request.form["long_url"]
        # Validate URL
        if not validators.url(long_url):
            return render_template("url/generate.html", error="Invalid URL. Please enter a valid URL.")
        
        # Generate short URL
        result = store.generate(long_url)
        return render_template("url/generate.html", result=result)
    else:
        return render_template("url/generate.html")

@app.route("/retrieve", methods=("GET", "POST"))
def retrieve():
    if request.method == "POST":
        short_url = request.form["short_url"]
        # Validate URL
        if not validators.url(short_url):
            return render_template("url/retrieve.html", error="Invalid URL. Please enter a valid URL.")
        
        # Find long URL
        result = store.find_long(short_url)
        
        # Long URL does not exist
        if result == None:
            return render_template("url/retrieve.html", noresult=short_url)    
        return render_template("url/retrieve.html", result=result)
    else:
        return render_template("url/retrieve.html")

@app.errorhandler(404)
def page_not_found(e):
    return "<p>Oops!</p>"