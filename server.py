from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, stav tsechansky!</p>"


# @app.route("/home")
# def home():
#     return "<p>BL:OGGGG</p>"

@app.route("/")
def blog():
    return render_template('home.html')