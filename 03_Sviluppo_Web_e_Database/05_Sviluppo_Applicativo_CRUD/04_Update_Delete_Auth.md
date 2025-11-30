# Lezione 3: Modifica e Cancellazione (Update/Delete)

Per completare il blog, dobbiamo permettere agli autori di modificare o cancellare i propri post.
Aggiungeremo queste funzioni nel nostro file principale: `app/main.py`.

Qui introduciamo un concetto fondamentale: **Autorizzazione**.
*   **Autenticazione:** Il sistema sa chi sei (Login).
*   **Autorizzazione:** Hai il permesso di fare questa azione? (Es. modificare un post che non hai scritto tu).

### 1. Helper per i controlli (`get_post`)

In `app/main.py`, aggiungiamo una funzione per non ripetere codice (mettila fuori dalle route, magari prima di `update`).
Questa funzione fa tre cose:
1.  Recupera il post dal DB.
2.  Controlla se esiste.
3.  Controlla se l'utente corrente è il proprietario del post.

```python
from werkzeug.exceptions import abort

def get_post(id, check_author=True):
    # 1. Recupera il post dal DB (usiamo la funzione creata nella Lezione 1)
    post = post_repository.get_post_by_id(id)

    # 2. Se non esiste -> Errore 404 Not Found
    if post is None:
        abort(404, f"Il post id {id} non esiste.")

    # 3. Controllo AUTORIZZAZIONE
    # Se check_author è attivo, controlla che l'autore sia l'utente loggato
    if check_author and post['author_id'] != g.user['id']:
        abort(403) # Errore 403 Forbidden (Vietato!)

    return post
```

### 2. La Route di Update

Qui dobbiamo applicare due livelli di sicurezza manualmente:
1.  **Sei loggato?** (`if g.user is None`)
2.  **È il tuo post?** (gestito da `get_post`)

Aggiungi a `app/main.py`:

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
            # Chiamiamo la funzione di update del repository
            post_repository.update_post(id, title, body)
            return redirect(url_for('main.index'))

    return render_template('blog/update.html', post=post)
```

### 3. La Route di Delete

Anche qui, doppio controllo di sicurezza.
Nota che accettiamo solo il metodo `POST`. Perché? Per evitare che un link malevolo o un crawler cancelli i dati visitando l'URL.

Aggiungi a `app/main.py`:

```python
@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    # 1. Sei loggato?
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    # 2. È tuo? (verifica anche che esista)
    get_post(id) 
    
    # 3. Cancella usando il repository
    post_repository.delete_post(id)
    return redirect(url_for('main.index'))
```

### 4. Il Template `blog/update.html`

Crea il file `app/templates/blog/update.html`.

Simile a quello di creazione, ma con una differenza importante: usiamo `value` per pre-compilare i campi con i dati esistenti.

La logica `request.form.get('title') or post['title']` significa:
*   Se l'utente ha provato a salvare ma c'era un errore, rimostra quello che ha appena scritto.
*   Altrimenti (è la prima volta che apre la pagina), mostra il titolo originale dal DB.

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Modifica "{{ post['title'] }}"</h1>
  
  <!-- Form di Modifica -->
  <form method="post">
    <label for="title">Titolo</label>
    <input name="title" id="title" value="{{ request.form.get('title') or post['title'] }}" required>

    <label for="body">Testo</label>
    <textarea name="body" id="body" rows="5" required>{{ request.form.get('body') or post['body'] }}</textarea>

    <input type="submit" value="Salva Modifiche">
  </form>

  <hr>
  
  <!-- Form di Cancellazione (Separato) -->
  <!-- L'action punta alla route di delete con l'id del post -->
  <!-- Nota: l'endpoint è 'main.delete' -->
  <form action="{{ url_for('main.delete', id=post['id']) }}" method="post">
    <input type="submit" value="Elimina Post" 
           onclick="return confirm('Sei sicuro di voler eliminare questo post?')"
           style="background-color: red; color: white;">
  </form>
{% endblock %}
```

### Conclusione Modulo 05
Ora il tuo blog è completo e sicuro!
Hai implementato:
*   **CRUD Completo:** Create, Read, Update, Delete.
*   **Architettura:** Codice diviso in Repository (SQL), Blueprint (Python) e Template (HTML).
*   **Sicurezza:** Protezione contro accessi non autorizzati e modifica di dati altrui.