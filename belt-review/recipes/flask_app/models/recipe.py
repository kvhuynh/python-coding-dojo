# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DATABASE = "recipes"

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('recipes').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def get_one(cls,data):
        print(data)
        query  = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('recipes').query_db(query,data)
        print(result)
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email =%(email)s;"
        result = connectToMySQL('recipes').query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

# ---------- SAVE ---------- #
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s, NOW(), NOW());"
        # comes back as the new row id
        result = connectToMySQL('recipes').query_db(query,data)
        return result