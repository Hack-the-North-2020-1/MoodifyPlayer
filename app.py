from flask import Flask, render_template, redirect, session
import controllers, settings
import requests

app = Flask("__name__")
app.register_blueprint(controllers.auth.blueprint)
app.secret_key = settings.SECRET_KEY

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)