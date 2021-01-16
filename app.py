from flask import Flask, render_template, redirect, session
import controllers
import requests
from flask_socketio import SocketIO
from services.socketio_api import create_socket

app = Flask("__name__")
app.register_blueprint(controllers.auth.blueprint)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    socketio = create_socket(socketio)
    socketio.run(app, debug=True)