from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import model_user
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

# ---------- VALIDATE ---------- #

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data["recipe_name"]) < 4 and not data["recipe_name"].isalpha():
            flash("Recipe name must be at least 3 characters and must be all alphabetical", "err_recipe_name")
            is_valid = False
        if len(data["description"]) < 4 and not data["description"].isalpha():
            flash("Description must be at least 3 characters and must be all alphabetical", "err_recipe_description" )
            is_valid = False
        if len(data["instructions"]) < 4:
            flash("Instructions must be at least 3 characters.", "err_recipe_instructions")
            is_valid = False
        return is_valid


# ---------- Create ---------- #

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipe (user_id, recipe_name, instructions, description, is_under_30) VALUES (%(user_id)s, %(recipe_name)s,%(instructions)s,%(description)s, %(is_under_30)s);"
        # comes back as the new row id
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

# ---------- Read ---------- #
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email =%(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls,data):
        print(data)
        query  = "SELECT * FROM recipe WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        return cls(result[0])

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipe JOIN users ON users.id = recipe.user_id"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for recipe in results:
                recipe_instance = cls(recipe)
                user_data = {
                    "id": recipe["users.id"],
                    "created_at": recipe["users.created_at"],
                    "updated_at": recipe["users.updated_at"],
                    "first_name": recipe["first_name"],
                    "last_name": recipe["last_name"],
                    "email": recipe["email"],
                    "password": recipe["password"]
                }
                user = model_user.User(user_data)
                recipe_instance.name = user

                all_recipes.append(recipe_instance)
            return all_recipes
        return results

# ---------- Update ---------- #
    @classmethod
    def update_one(cls, data) -> None:
        query = "UPDATE recipe SET recipe_name = %(recipe_name)s, description = %(description)s, instructions = %(instructions)s, is_under_30 = %(is_under_30)s WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)

# ---------- Delete ---------- #
    @classmethod
    def delete_one(cls, data: dict) -> None:
        query = "DELETE FROM recipe WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data) 