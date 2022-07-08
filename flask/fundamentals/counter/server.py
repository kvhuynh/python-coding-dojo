#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = os.urandom(12)

@app.route('/')         
def index():
    if 'count' in session:
        session["count"] += 1
        print('key exists!')
    else:
        print("key 'count' does NOT exist")
        session["count"] = 1
    if request.form["reset"] == "RESET":
        print("yo")
    print(session)
    return render_template("index.html")

@app.route('/add_two')
def add_two():
    if 'count' in session:
        session["count"] += 2
        print('key exists!')
    else:
        print("key 'count' does NOT exist")
        session["count"] = 1
    print(session)
    return render_template("index.html")

@app.route('/destroy_session')
def redirect():
    session.clear()		# clears all keys
    session.pop('key_name')		# clears a specific key
    redirect("index.html")

# @app.route('/checkout', methods=['POST'])         
# def checkout():
#     print(request.form)
#     print(f"Charging {request.form['first_name']} for {int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])} fruits.")
#     return render_template("checkout.html", form=request.form)

if __name__=="__main__":   
    app.run(debug=True)    