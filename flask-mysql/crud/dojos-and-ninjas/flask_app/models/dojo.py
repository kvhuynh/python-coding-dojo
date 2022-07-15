from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('names').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s, NOW(), NOW());"

        # comes back as the new row id
        result = connectToMySQL('names').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL('names').query_db(query,data)
        return cls(result[0])

    # @classmethod
    # def get_ninjas(cls, data):
    #     query = "SELECT * FROM ninjas WHERE dojo_id =%(id)s;"
    #     return connectToMySQL('names').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('names').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('names').query_db(query,data)