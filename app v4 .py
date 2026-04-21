from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

import json



app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_muy_segura'  # Cambia esto en producción

# Simulación de una base de datos de usuarios
users = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'driver1': {'password': 'driver1pass', 'role': 'driver'},
    'driver2': {'password': 'driver2pass', 'role': 'driver'},
    'driver3': {'password': 'driver3pass', 'role': 'driver'},
    'editor': {'password': 'editorpass', 'role': 'editor'}
}


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Por favor, inicia sesión para acceder a esta página.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['role'] = users[username]['role']
            flash(f'Bienvenido, {username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')



@app.route('/ver_mapa')
def ver_mapa():
    if 'username' not in session or session['username'] == None:
        return redirect(url_for('login'))

    pass