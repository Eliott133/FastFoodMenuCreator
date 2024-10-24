from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "It's work"