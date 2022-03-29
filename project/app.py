#!/usr/bin/env python

import project.web_utils
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cart")
def cart():
    return project.web_utils.cart(render_template)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
