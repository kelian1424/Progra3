from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Definimos la lista de canciones
    lista = ['La guitarra', 'Para no verte más', 'Balada para un gordo']
    # Pasamos el título y la lista al HTML
    return render_template('lista.html', titulo='canciones', musicas=lista)

if __name__ == '__main__':
    app.run(debug=True)