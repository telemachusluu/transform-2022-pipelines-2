#!/usr/bin/env python

import os
import project.web_utils
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    feature_flag_cart_enable = os.environ.get("FEATURE_FLAG_CART_ENABLE")
    print(feature_flag_cart_enable)
    if feature_flag_cart_enable == "False":
        return render_template("index.html", feature_flag_cart_enable=False)
    elif feature_flag_cart_enable == "True":
        return render_template("index.html", feature_flag_cart_enable=True)


@app.route("/cart")
def cart():
    feature_flag_cart_enable = os.environ.get("FEATURE_FLAG_CART_ENABLE")
    if feature_flag_cart_enable == "False":
        return project.web_utils.cart(render_template, feature_flag_cart_enable=False)
    elif feature_flag_cart_enable == "True":
        return project.web_utils.cart(render_template, feature_flag_cart_enable=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
