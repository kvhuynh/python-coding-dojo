# import the function that will return an instance of a connection
from operator import methodcaller
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = "recipes"

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data["user_id"]
        self.recipe_name = data["recipe_name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.is_under_30 = data["is_under_30"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #join two tables first

# ---------- VALIDATE ---------- #

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True # we assume this is true
        if len(recipe["recipe_name"]) < 4 and not recipe["recipe_name"].isalpha():
            flash("Recipe name must be at least 3 characters and must be all alphabetical")
            is_valid = False
        if len(recipe["description"]) < 4 and not recipe["description"].isalpha():
            flash("Last name must be at least 3 characters and must be all alphabetical")
            is_valid = False
        if len(recipe["instructions"]) < 4:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        return is_valid


# ---------- GET ---------- #

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        print(users)
        return users

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email =%(email)s;"
        result = connectToMySQL('recipes').query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def join(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query, data)

# ---------- SAVE ---------- #
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (user_id, recipe_name, instructions, description, is_under_30) VALUES (%(user_id)s, %(recipe_name)s,%(instructions)s,%(description)s, %(is_under_30)s);"
        # comes back as the new row id
        result = connectToMySQL('recipes').query_db(query,data)
        return result