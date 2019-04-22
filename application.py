import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from tempfile import mkdtemp
import requests


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    """Show the main page with instructions"""

    if request.method == "POST":

        usuario = request.form.get("usr")
        id = request.form.get("id")

         # URL to get a embeddable version of the tweet
        url = 'https://publish.twitter.com/oembed?url=https://twitter.com/'+ usuario +'/status/' + id

        # Get the embedable HTML out of the json
        twt_embed = requests.get(url)
        twt_json = twt_embed.json()
        twt_html = twt_json['html']


        return render_template("index.html", tweet=twt_html)
    else:
        return render_template("index.html")

