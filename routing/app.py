from flask import Flask

app = Flask(__name__)

@app.route("/user/<username>")
def hello_world(username):
    return f"<p>Hello, {username}!</p>"
