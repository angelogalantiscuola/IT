from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.repositories import post_repository

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # 1. Prendiamo i post veri dal database
    posts = post_repository.get_all_posts()
    
    # 2. Passiamo la variabile 'posts' al template
    return render_template('index.html', posts=posts)

@bp.route('/about')
def about():
    return render_template('about.html')

# --- NUOVA ROUTE: CREAZIONE POST ---
@bp.route('/create', methods=('GET', 'POST'))
def create():
    # Protezione: Se non sei loggato, vai al login
    if g.user is None:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Il titolo è obbligatorio.'

        if error is not None:
            flash(error)
        else:
            # Creiamo il post usando l'ID dell'utente loggato (g.user['id'])
            post_repository.create_post(title, body, g.user['id'])
            return redirect(url_for('main.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    # 1. Recupera il post dal DB
    post = post_repository.get_post_by_id(id)

    # 2. Se non esiste -> Errore 404 Not Found
    if post is None:
        abort(404, f"Il post id {id} non esiste.")

    # 3. Controllo AUTORIZZAZIONE
    # Se check_author è attivo, controlla che l'autore sia l'utente loggato
    if check_author and post['author_id'] != g.user['id']:
        abort(403) # Errore 403 Forbidden (Vietato!)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    # --- LIVELLO 1: PROTEZIONE (Sei loggato?) ---
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    # --- LIVELLO 2: AUTORIZZAZIONE (È tuo?) ---
    # Questa funzione blocca tutto con un errore 403 se il post non è tuo
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Il titolo è obbligatorio.'

        if error is not None:
            flash(error)
        else:
            post_repository.update_post(id, title, body)
            return redirect(url_for('main.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    # 1. Sei loggato?
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    # 2. È tuo?
    get_post(id) 
    
    # 3. Cancella
    post_repository.delete_post(id)
    return redirect(url_for('main.index'))