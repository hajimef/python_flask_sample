from flask import Flask

app = Flask(__name__)

@app.route("/history/")
def history():
    return "<p>History page</p>"

@app.route("/about")
def about():
    return "<p>About page</p>"
