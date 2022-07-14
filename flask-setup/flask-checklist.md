# Pre-rec
```
pip install pipenv
```

# Checklist
- Createa folder / dir for assignment
- Navigate into that folder
- Create virtual env
```
pipenv install flask, pymysql
```

- WARNING check for "pipfile" and "pipfile.lock"
    - fix if you dont see

- Launch the virtual env
```
pipenv shell
```

- file structure list
    - assignment folder
      - flask_app
        - config 
          - mysqlconnection.py
        - controllers for every table
          - controller_driver.py
        - models for every table
          - model_drivers.py
            - index.html
        - static
            -css
                - styles.css
            - js
                - script.js
      - pip file
      - pip lock

# server.py boilerplate
``` python
from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():

    return render_template("index.html")
            
if __name__ == "__main__":
    app.run(debug=True) 
```

# mysql connection code

``` python
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', # rootroot on mac
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db) 
```

# model_table_name.py file
``` python
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class ObjectName:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
            
```

