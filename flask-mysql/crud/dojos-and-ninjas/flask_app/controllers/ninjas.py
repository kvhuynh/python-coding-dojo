from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninjas")
def add_ninja():
    return render_template("new-ninja.html", current_dojos=Ninja.get_all())

