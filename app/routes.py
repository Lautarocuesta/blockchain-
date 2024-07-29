from flask import render_template, url_for, flash, redirect
from . import app, db
from .models import User, Transaction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Lógica de registro de usuario
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica de inicio de sesión de usuario
    pass
