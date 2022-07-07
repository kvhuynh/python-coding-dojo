from flask import Flask, render_template
app = Flask(__name__) 
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/play")
def blue_boxes():
    return render_template("index.html", num=3, color="blue")

@app.route("/play/<int:x>")
def custom_boxes(x):
    return render_template("index.html", num=x, color="blue")

@app.route("/play/<int:x>/<string:color>")
def custom_color(x, color):
    return render_template("index.html", num=x, color=color)

app.run(debug=True)