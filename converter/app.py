from flask import Flask

app = Flask(__name__)

@app.route("/<int:id>")
def show_page(id):
    return f'<p>ID = {id}</p>'
