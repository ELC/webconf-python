from flask import Flask
from waitress import serve

from .data import data
from .routes import api_routes

app = Flask(__name__)

app.register_blueprint(api_routes, url_prefix="/")

data.init_database()

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000, threads=10)
