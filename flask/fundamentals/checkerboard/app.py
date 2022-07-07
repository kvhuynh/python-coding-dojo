from flask import Flask, render_template
app = Flask(__name__)                     
    
@app.route('/')                           
def render_checkerboard():
    return render_template("index.html")
    
@app.route("/<int:num>")
def variable_checkerboard(num):
    return render_template("index.html", num=num)

@app.route("/<int:num>/<int:width>")
def height_width_checkerboard(num, width):
    return render_template("index.html", num=num, width=width)

@app.route("/<int:num>/<int:width>/<string:color1>/<string:color2>")
def custom_color_dimensions(num, width, color1, color2):
    return render_template("index.html", num=num, width=width, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True) 