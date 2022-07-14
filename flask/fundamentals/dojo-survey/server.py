#!/usr/bin/env python3
import os
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = os.urandom(12)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def guessed():
    print(request.form)
    for key in request.form:
        session[key] = request.form[key]
    print(session)

    return render_template("result.html", data=request.form)


if __name__=="__main__":   
    app.run(debug=True)    