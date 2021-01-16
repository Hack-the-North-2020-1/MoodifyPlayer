from flask import flash, redirect, render_template, url_for, Blueprint
import json, requests

blueprint = Blueprint('auth', __name__)