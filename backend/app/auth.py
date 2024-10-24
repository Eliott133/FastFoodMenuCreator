from flask import Blueprint, flash, render_template, redirect, url_for, request

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "Futur login page"