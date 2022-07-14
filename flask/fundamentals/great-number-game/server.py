#!/usr/bin/env python3
import os
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = os.urandom(12)
@app.route('/')


def index():
    global random_num
    random_num = random.randint(1, 100)
    print(random_num)
    if "count" != session:
        session["count"] = 1
    return render_template("index.html")

# if session["count"] > 5:
#     @app.route("/you_lost")
#     def lose_screen():
#         return render_template("index.html", lost=True)


@app.route("/guess", methods=["POST"])
def guessed():
    if int(request.form["user-guess"]) > random_num:
        session["count"] += 1
        return redirect('/too_high')
    elif int(request.form["user-guess"]) < random_num:
        session["count"] += 1
        return redirect('/too_low')
    else:
        return redirect('/correct')

leader_board_names = {}
@app.route("/leader_board", methods=["POST"])
def leader_board():
    print(request.form)

    leader_board_names[request.form["user-name"]] = session["count"]
    return render_template("index.html", winners=leader_board_names, win=True)

@app.route("/too_high")
def too_high():
    return render_template("index.html", too_high="too high")

@app.route("/too_low")
def too_low():
    return render_template("index.html", too_low="too low")

@app.route("/correct")
def correct():
    return render_template("index.html", correct="correct")


if __name__=="__main__":   
    app.run(debug=True)    