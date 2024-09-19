# app.py

from flask import Flask, render_template, jsonify, request, session
from conection import conBull
import secrets

app = Flask(__name__)

# cambiar en prod a env
app.secret_key = secrets.token_hex(16)

# Ruta inicial que renderiza la plantilla index.html
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la petición de incremento del contador
@app.route('/increment', methods=['POST'])
def increment_counter():
    # Supongamos que tenemos un contador simple en la sesión
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return jsonify({'count': session['counter']})

@app.route('/list', methods=['GET'])
def get_list():
    items = conBull()
    return render_template('list_partial.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)

