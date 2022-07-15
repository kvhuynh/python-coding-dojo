from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    return render_template("dojo.html", locations=Dojo.get_all())

@app.route('/dojo/show/<int:id>')
def dojo_data(id):
    data ={ 
        "id":id
    }
    return render_template("dojos-ninjas.html",dojo_name=Dojo.get_one(data), dojo=Ninja.get_ninjas(data))

@app.route("/ninjas")
def add_ninja():
    return render_template("new-ninja.html", current_dojos=Dojo.get_all())

@app.route("/ninja_added", methods=["post"])
def added():
    print(request.form)
    Ninja.save(request.form)
    return redirect("/")

@app.route("/dojo_added", methods=["post"])
def add_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect("/")
