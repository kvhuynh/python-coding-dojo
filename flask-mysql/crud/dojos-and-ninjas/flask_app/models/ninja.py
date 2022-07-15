from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('names').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (CAST(%(dojo_id)s AS UNSIGNED), %(first_name)s,%(last_name)s,%(age)s, NOW(), NOW());"

        # comes back as the new row id
        result = connectToMySQL('names').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL('names').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id =%(id)s;"
        return connectToMySQL('names').query_db(query,data)
