# app/main.py
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Simuliamo dei dati presi da un database (per ora finti)
    notizie_fittizie = [
        "Abbiamo imparato i Blueprint",
        "Configurato Jinja2",
        "Il progetto sta prendendo forma"
    ]
    # Passiamo la variabile 'notizie' al template
    return render_template('index.html', notizie=notizie_fittizie)

@bp.route('/about')
def about():
    return render_template('about.html')