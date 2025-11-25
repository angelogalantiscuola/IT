# Lezione 2: Il Livello di Presentazione con Jinja2

Nella lezione precedente, le nostre funzioni restituivano semplici stringhe di testo contenenti tag HTML.

```python
@app.route('/')
def home():
    return "<h1>Ciao Mondo!</h1>"
```

Questo approccio diventa rapidamente insostenibile. Immagina di dover scrivere un'intera pagina HTML complessa dentro una stringa Python: sarebbe illeggibile, difficile da modificare e pieno di errori.

La soluzione è separare la **logica** (il codice Python) dalla **presentazione** (il codice HTML). Questo è il compito di un **motore di template**.

### 1. Cos'è Jinja2 e `render_template`

Flask è già equipaggiato con uno dei migliori motori di template per Python: **Jinja2**.

Jinja2 ci permette di scrivere file HTML standard e di inserire al loro interno dei segnaposto speciali. Flask userà Jinja2 per "renderizzare" questi template: leggerà il file HTML, sostituirà i segnaposto con dati reali e restituirà il risultato finale al browser.

La funzione chiave per fare questo è `render_template()`. Per convenzione, Flask cerca i file dei template in una cartella chiamata `templates`.

### 2. La Sintassi di Base di Jinja2

Jinja2 usa dei delimitatori speciali per distinguere i suoi comandi dall'HTML normale:

*   `{{ ... }}`: **Per le espressioni (stampare qualcosa).** Qualsiasi cosa metti qui dentro verrà calcolata e il suo risultato stampato nella pagina. È usato per visualizzare le variabili.
    ```html
    <h1>Ciao, {{ nome_utente }}!</h1>
    ```

*   `{% ... %}`: **Per le istruzioni (fare qualcosa).** È usato per la logica, come i cicli `for` o le condizioni `if`.
    ```html
    <ul>
      {% for prodotto in lista_prodotti %}
        <li>{{ prodotto.nome }}</li>
      {% endfor %}
    </ul>
    ```

### 3. Il Principio DRY e l'Ereditarietà dei Template

**DRY** sta per **"Don't Repeat Yourself"** (Non Ripeterti). È uno dei principi più importanti della programmazione.

Tutte le pagine di un sito web condividono elementi comuni: la navbar, il footer, l'inclusione dei file CSS e JavaScript. Sarebbe un incubo copiare e incollare questo codice in ogni singolo file HTML. Se dovessi cambiare un link nella navbar, dovresti modificarlo in decine di file!

Jinja2 risolve questo problema con l'**ereditarietà dei template**.

**1. Creiamo un Template "Base" (`base.html`)**
Questo file contiene tutta la struttura HTML comune. Al posto delle parti che cambieranno, definiamo dei **blocchi** (`{% block ... %}`).

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>La Mia App Flask</title>
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>

    <main>
        <!-- Questo blocco verrà riempito dai template "figli" -->
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2025 La Mia App</p>
    </footer>
</body>
</html>
```

**2. Creiamo un Template "Figlio" (`home.html`)**
Questo file **estende** il template base e ridefinisce solo i blocchi che gli interessano.

```html
<!-- templates/home.html -->

<!-- Diciamo a Jinja2 di usare base.html come struttura -->
{% extends "base.html" %}

<!-- Inizia la definizione del blocco 'content' -->
{% block content %}
    <h1>Benvenuto nella Homepage!</h1>
    <p>Questo è il contenuto specifico della pagina home.</p>
{% endblock %}
<!-- Fine della definizione del blocco -->
```

Quando Flask renderizzerà `home.html`, Jinja2 prenderà `base.html` e sostituirà il blocco `content` con il contenuto definito in `home.html`. Geniale!

### 4. URL Dinamici con `url_for()`

Abbiamo un ultimo problema. Nel nostro `base.html` abbiamo scritto i link così: `<a href="/">Home</a>`. Questo si chiama "hard-coding" (codifica fissa). Se un giorno decidessimo di cambiare la route della homepage da `/` a `/dashboard`, dovremmo ricordarci di aggiornare il link in tutti i file HTML.

Flask ci fornisce una funzione molto più robusta: `url_for()`. Le passi il **nome della funzione Python** che gestisce la route, e lei ti restituirà l'URL corretto.

Modifichiamo la navbar in `base.html`:

```html
<!-- templates/base.html (navbar aggiornata) -->
<nav>
    <!-- url_for('nome_della_funzione') -->
    <a href="{{ url_for('home') }}">Home</a>
    <a href="{{ url_for('about') }}">About</a>
</nav>
```
Ora, anche se cambiassimo `@app.route('/')` in `@app.route('/homepage')`, `url_for('home')` genererebbe automaticamente `/homepage`, e non dovremmo toccare l'HTML.

### 5. Mettiamo Tutto Insieme: Refactoring della Nostra App

È ora di applicare questi concetti.

**1. Crea i file dei template:**
*   Crea `templates/base.html` con il codice visto sopra (quello con `url_for`).
*   Crea `templates/home.html` (il template figlio per la homepage).
*   Crea un nuovo file `templates/about.html` per la pagina about.
    ```html
    <!-- templates/about.html -->
    {% extends "base.html" %}

    {% block content %}
        <h1>Pagina About</h1>
        <p>Qui parliamo della nostra fantastica applicazione.</p>
    {% endblock %}
    ```

**2. Aggiorna `app.py`:**
Modifichiamo il nostro file Python per usare `render_template`.

```python
# app.py (versione aggiornata)

# Importiamo anche render_template
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Invece di una stringa, ora restituiamo il template renderizzato.
    return render_template('home.html')

# Aggiungiamo la route per la pagina 'about'
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Ora, se avvii l'applicazione (`python app.py`) e visiti la homepage e la pagina about, vedrai le pagine HTML complete, con la stessa struttura definita in `base.html`.

### 6. Esercizio: Passare Dati al Template

Modifica la funzione `home()` in `app.py` in modo che passi una variabile al template `home.html`. Poi, modifica `home.html` per visualizzare quella variabile.

*   **Suggerimento in `app.py`:**
    ```python
    def home():
        nome_studente = "Mario"
        return render_template('home.html', utente=nome_studente)
    ```
*   **Suggerimento in `home.html`:**
    ```html
    <h1>Benvenuto nella Homepage, {{ utente }}!</h1>
    ```