# Lezione 1: Introduzione al Repository Pattern

Nel capitolo precedente abbiamo fatto un enorme passo avanti, organizzando la nostra applicazione in **Blueprints**. Ora la nostra struttura di file è pulita: la logica di autenticazione è in `auth.py`, quella dei post in `posts.py`.

Tuttavia, se guardiamo all'interno di questi file, notiamo un problema. Prendiamo ad esempio la funzione `login`:

```python
# app/auth.py (esempio)
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Questa funzione sta facendo TROPPE cose!
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        
        # ... logica di controllo password ...
```

Questa funzione ha **due responsabilità distinte**:
1.  **Gestire la richiesta HTTP:** Legge i dati dal form (`request.form`), gestisce la sessione (`session`), e decide quale risposta inviare (`redirect`, `render_template`).
2.  **Interagire con il Database:** Si connette al DB, scrive ed esegue una query SQL, e interpreta il risultato.

Mescolare queste due responsabilità rende il codice **accoppiato (tightly coupled)**. La nostra logica web è strettamente legata a *come* i dati sono memorizzati e recuperati. Se un domani decidessimo di cambiare database o la struttura di una tabella, dovremmo andare a modificare tutte le funzioni delle route che la utilizzano.

### 1. La Soluzione: Un Livello di Astrazione per i Dati

Per risolvere questo problema, introduciamo un nuovo "strato" nella nostra architettura, chiamato **Data Access Layer (DAL)** o Livello di Accesso ai Dati.

L'idea è semplice: creiamo un insieme di moduli la cui **unica ed esclusiva responsabilità è comunicare con il database**. Tutto il codice SQL vivrà qui.

Le nostre funzioni delle route non parleranno mai più direttamente con il database. Invece, parleranno con questo nuovo strato.

### 2. Il Repository Pattern

Una delle implementazioni più comuni e pulite di un DAL è il **Repository Pattern**.

**Cos'è un Repository?**
Un Repository è un modulo (o una classe) che media tra il dominio dell'applicazione (la nostra logica web) e il livello di mappatura dei dati (il nostro database).

**Analogia del Magazziniere:**
Pensa alla tua applicazione come a un ristorante.
*   **Le Route (i Blueprints):** Sono i **camerieri**. Prendono le ordinazioni dai clienti (le richieste HTTP) e servono i piatti (le risposte HTTP).
*   **Il Database:** È il **magazzino**, dove sono conservati tutti gli ingredienti (i dati).
*   **Il Repository:** È il **magazziniere**.

Il cameriere non va personalmente nel magazzino a cercare gli ingredienti. Sarebbe inefficiente e caotico. Invece, il cameriere dà un ordine chiaro al magazziniere: *"Portami 5 pomodori e 2 mozzarelle"*.

Il magazziniere è l'unico che sa esattamente in quale scaffale si trovano i pomodori, come sono conservati e come prenderli (sa come scrivere ed eseguire la query SQL). Prende gli ingredienti e li consegna al cameriere.

Il cameriere riceve gli ingredienti (i dati grezzi) e li usa per "comporre il piatto" da servire al cliente (renderizzare il template).

**I Vantaggi di questo approccio:**

1.  **Separazione Netta delle Responsabilità:**
    *   Le route si occupano solo di HTTP.
    *   I repository si occupano solo di SQL.
2.  **Codice più Pulito e Leggibile:** Le funzioni delle route diventano molto più semplici e brevi. La loro intenzione è chiara: "prendi i dati dell'utente, chiedi al repository di trovarlo, controlla la password, gestisci la sessione".
3.  **Manutenibilità Migliorata:** Se dobbiamo ottimizzare una query SQL o cambiare il nome di una colonna, modifichiamo **un solo file**: il repository corrispondente. Tutte le route che usano quella funzione continueranno a funzionare senza bisogno di modifiche.
4.  **Riutilizzabilità:** Le funzioni del repository (es. `find_user_by_id`) possono essere riutilizzate in diverse parti dell'applicazione senza duplicare il codice SQL.

### 3. Come lo Implementeremo
Nelle prossime lezioni, faremo un ultimo, importante refactoring:
1.  Creeremo una nuova cartella `app/data/` (o `app/repositories/`).
2.  All'interno, creeremo `user_repository.py` e `post_repository.py`.
3.  Sposteremo tutto il codice SQL e di interazione con il database dal `auth.py` e `posts.py` a questi nuovi file, racchiudendolo in funzioni con nomi chiari (es. `create_post`, `find_all_posts`).
4.  Infine, riscriveremo le nostre route in modo che chiamino queste nuove funzioni, disaccoppiando completamente la logica web da quella di persistenza.