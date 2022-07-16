from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# ---------- CREATE ---------- #

@app.route("/")
def index():
    return render_template("index.html")

# ---------- READ ---------- #

@app.route("/validate_new_user", methods=["POST"])
def validate():
    print(request.form)
    is_valid = User.validate_user(request.form)
    if is_valid:
        print("valid!")
        password = request.form["password"]
        pw_hash = bcrypt.generate_password_hash(password)
        print(pw_hash)
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": pw_hash
        }
        user_id = User.save(data)
        session["user_id"] = user_id
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    data = {"email": request.form["email"]}
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid Email/Password", "login")
        return redirect("/")
    session["user"] = user.id
    return redirect("/user")

@app.route("/user")
def signed_in():
    data = {
        "id": session["user"]
    }
    user = User.get_one(data)
    print(user)
    return render_template("user.html", user=user.first_name)


# ---------- DELETE ---------- #
@app.route("/clear_session")
def destroy_session():
    session.clear()
    return redirect("/")



