from flask_app import app, bcrypt
from flask import render_template, request, redirect, session, flash

# This imports model file
from flask_app.models import model_recipe
# ---------- CREATE ---------- #

@app.route("/recipe/new")
def recipe_new():
    return render_template("recipe_new.html")


@app.route("/recipe/create", methods=["POST"])
def recipe_create():
    #validate
    print(request.form)
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect("/recipe/new")
    #create recipe
    data = {
        **request.form,
        "user_id": session["uuid"]
    }
    model_recipe.Recipe.create(data)
    return redirect("/")

@app.route("/recipes/<int:id>/edit")
def recipe_edit(id):
    context = {
        "recipe": model_recipe.Recipe.get_one({"id":id})
    }
    return render_template("recipe_edit.html", **context)

@app.route("/recipe/<int:id>/update", methods=["POST"])
def recipe_update(id):
    #validate
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/{id}/edit")

    data = {
        **request.form,
        "id": id
    }

    model_recipe.Recipe.update_one(data)
    return redirect(f"/recipes/{id}/edit")

@app.route("/recipes/<int:id>/delete")
def recipe_delete(id):
    model_recipe.Recipe.delete_one({"id": id})
    return redirect("/")

@app.route("/recipes/<int:id>/view")
def view_recipe(id):
    context = {
        "recipe": model_recipe.Recipe.get_one({"id":id})
    }
    return render_template("view_recipe.html", **context)
