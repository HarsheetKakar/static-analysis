from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    # Put the blueprints here

    return app, db
