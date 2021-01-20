from flask import Flask, render_template, redirect, session
import controllers, settings, extensions
from extensions import db
import requests
from flask_socketio import SocketIO
from services import image_stream

app = Flask("__name__")
socketio = SocketIO(app)

def register_blueprints(app):
    app.register_blueprint(controllers.auth.blueprint)
    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(controllers.get_song.blueprint)

    return None

def register_extensions(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

if __name__ == "__main__":

    app.register_blueprint(controllers.auth.blueprint)
    app.secret_key = settings.SECRET_KEY
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    register_extensions(app)
    register_blueprints(app)

    socket = image_stream.create_socket(socketio)
    socket.run(app, debug=True)
