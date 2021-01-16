from flask import Flask, render_template, redirect, session
import controllers, settings, extensions
from extensions import db
import requests
from flask_socketio import SocketIO
from services import image_stream

def create_app():
    app = Flask("__name__")

    app.register_blueprint(controllers.auth.blueprint)
    app.secret_key = settings.SECRET_KEY
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    socketio = SocketIO(app)

    register_extensions(app)
    register_blueprints(app)

    socketio = image_stream.create_socket(socketio)
    socketio.run(app, debug=True)

    return app

def register_blueprints(app):
    app.register_blueprint(controllers.auth.blueprint)
    app.register_blueprint(controllers.home.blueprint)

    return None

def register_extensions(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()
