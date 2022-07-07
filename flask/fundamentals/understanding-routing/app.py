from flask import Flask
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__) 
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<var>")
def say(var):
    return "Hi " + var + "!"

@app.route("/repeat/<int:num>/<string:var>")
def repeat(num, var):
    return var * num

@app.errorhandler(404)
def not_found(e):
    return "custom 404 not found"