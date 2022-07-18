from flask_app import app, bcrypt
from flask import render_template, request, redirect, session, flash

# This imports model file
from flask_app.models.recipe import Recipe
# ---------- CREATE ---------- #

@app.route("/validate_new_recipe", methods=["POST"])
def validate_recipe():
    print(request.form)
    is_valid = Recipe.validate_recipe(request.form)
    if is_valid:
        print("valid!")
        data = {
            "recipe_name": request.form["recipe_name"],
            "description": request.form["description"],
            "instructions": request.form["instructions"],
            "date-cooked": request.form["date_cooked"],
            "is_under_30": request.form["is_under_30"]
        }
        # user_id = Recipe.save(data)
        # session["user_id"] = user_id
        return redirect("/user")
    return redirect("/create_recipe")


@app.route("/create_recipe")
def create_recipe():
    return render_template("new-recipe.html")

