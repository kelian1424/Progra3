from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = ['La guitarra', 'Para no verte más', 'Balada para un gordo']
    return render_template('lista.html', titulo='canciones', musicas=lista)