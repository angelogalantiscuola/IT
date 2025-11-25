# Lezione 3: Update, Delete e Sicurezza

Mancano le operazioni di modifica e cancellazione.
Qui introduciamo un concetto fondamentale: **Autorizzazione**.

*   **Autenticazione:** Il sistema sa chi sei (Login).
*   **Autorizzazione:** Hai il permesso di fare questa azione? (Es. modificare un post che non hai scritto tu).

### 1. Helper per i controlli (`get_post`)

In `app/blog.py`, aggiungiamo una funzione per non ripetere codice. Questa funzione fa due cose:
1.  Controlla se il post esiste.
2.  Controlla se l'utente corrente è il proprietario del post.

```python
def get_post(id, check_author=True):
    # 1. Recupera il post dal DB
    post = post_repository.find_by_id(id)

    # 2. Se non esiste -> Errore 404 Not Found
    if post is None:
        abort(404, f"Il post id {id} non esiste.")

    # 3. Controllo AUTORIZZAZIONE
    # Se check_author è attivo, controlla che l'autore sia l'utente loggato
    if check_author and post['author_id'] != g.user['id']:
        abort(403) # Errore 403 Forbidden (Vietato!)

    return post
```

### 2. Route di Update

Qui dobbiamo applicare due livelli di sicurezza manualmente:
1.  **Sei loggato?** (`if g.user is None`)
2.  **È il tuo post?** (gestito da `get_post`)

```python
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
            post_repository.update(id, title, body)
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```

### 3. Route di Delete

Anche qui, doppio controllo di sicurezza.
Nota che accettiamo solo il metodo `POST`. Perché? Per evitare che un link malevolo o un crawler cancelli i dati visitando l'URL.

```python
@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    # 1. Sei loggato?
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    # 2. È tuo?
    get_post(id) 
    
    # 3. Cancella
    post_repository.delete(id)
    return redirect(url_for('blog.index'))
```

### 4. Il Template `blog/update.html`

Simile a quello di creazione, ma con una differenza importante: usiamo `value` per pre-compilare i campi con i dati esistenti.

La logica `request.form['title'] or post['title']` significa:
*   Se l'utente ha provato a salvare ma c'era un errore (es. titolo vuoto), rimostra quello che ha appena scritto (`request.form`).
*   Altrimenti (è la prima volta che apre la pagina), mostra il titolo originale salvato nel DB (`post`).

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Modifica "{{ post['title'] }}"</h1>
  
  <!-- Form di Modifica -->
  <form method="post">
    <label for="title">Titolo</label>
    <input name="title" id="title" value="{{ request.form.get('title') or post['title'] }}" required>

    <label for="body">Testo</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>

    <input type="submit" value="Salva Modifiche">
  </form>

  <hr>
  
  <!-- Form di Cancellazione (Separato) -->
  <!-- L'action punta alla route di delete con l'id del post -->
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input type="submit" value="Elimina Post" onclick="return confirm('Sei sicuro di voler eliminare questo post?')">
  </form>
{% endblock %}
```

### Conclusione Modulo 05
Ora il tuo blog è completo e sicuro!
Hai implementato:
*   **CRUD Completo:** Create, Read, Update, Delete.
*   **Architettura:** Codice diviso in Repository (SQL), Blueprint (Python) e Template (HTML).
*   **Sicurezza:** Protezione contro accessi non autorizzati e modifica di dati altrui.