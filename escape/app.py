from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<path:str>")
def hello_world(str):
    return f"<p>Hello, {escape(str)}!</p>"
