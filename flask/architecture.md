# Architettura dell'Applicazione Flask

## Struttura del Progetto

```
flask/
├── app/                  # Directory principale dell'applicazione
│   ├── __init__.py       # Inizializzazione dell'app Flask
│   ├── app.py            # Configurazione e creazione dell'app
│   ├── auth.py           # Gestione dell'autenticazione
│   ├── database.py       # Gestione del database MySQL
│   ├── routes/           # Blueprint per il routing
│   │   ├── auth.py       # Route per l'autenticazione
│   │   ├── entries.py    # Route per la gestione dei messaggi
│   │   └── profile.py    # Route per la gestione del profilo
├── static/               # File statici (CSS, JSON)
│   ├── styles.css        # Stili dell'applicazione
│   └── messages.json     # Dati iniziali per i messaggi
├── templates/            # Template HTML
│   ├── layout.html       # Template base
│   ├── index.html        # Pagina principale
│   ├── list.html         # Lista dei messaggi
│   ├── login.html        # Pagina di login
│   ├── menu.html         # Menu di navigazione
│   ├── profile.html      # Pagina del profilo
│   └── register.html     # Pagina di registrazione
└── run.py                # Script per l'avvio dell'applicazione
```

## Componenti Principali

### Configurazione (app/app.py)

La classe `Config` gestisce le configurazioni principali dell'applicazione:

- Chiave segreta per la sicurezza
- Parametri di connessione MySQL:
  - Host
  - Utente
  - Password
  - Nome del database

### Database (app/database.py)

Il modulo gestisce l'interazione con MySQL:

- `get_db_connection()`: Crea una connessione al database
- `init_db()`: Inizializza lo schema del database con:
  - Tabella `users` per gli utenti
  - Tabella `entries` per i messaggi

Schema del Database:

```sql
-- Tabella users
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)

-- Tabella entries
CREATE TABLE entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    message VARCHAR(200) NOT NULL
)
```

### Factory dell'Applicazione (app/app.py)

La funzione `create_app()`:

- Crea l'istanza Flask
- Carica la configurazione
- Inizializza il database
- Crea un utente iniziale
- Carica i messaggi da JSON se il database è vuoto
- Registra i blueprint per il routing

### Blueprint Routes (app/routes/)

L'applicazione è organizzata in tre blueprint principali:

1. **Auth** (routes/auth.py)

   - Gestione login/logout
   - Registrazione utenti
   - Reset password

2. **Entries** (routes/entries.py)

   - Visualizzazione messaggi
   - Creazione messaggi
   - Modifica messaggi
   - Eliminazione messaggi

3. **Profile** (routes/profile.py)
   - Gestione profilo utente
   - Aggiornamento informazioni personali

## Flusso dell'Applicazione

1. L'applicazione viene avviata da `run.py`
2. `create_app()` inizializza l'applicazione:
   - Carica la configurazione
   - Inizializza il database
   - Crea l'utente predefinito
   - Carica i dati iniziali dei messaggi
   - Registra i blueprint
3. Il database MySQL gestisce la persistenza dei dati
4. I blueprint gestiscono le richieste HTTP
5. I template Jinja2 renderizzano le pagine HTML

## Inizializzazione dei Dati

L'applicazione include:

- Creazione automatica di un utente predefinito
- Caricamento iniziale dei messaggi da `static/messages.json`
- Inizializzazione automatica dello schema del database

## Utilizzo

Per avviare l'applicazione:

```bash
python run.py
```

L'applicazione sarà accessibile all'indirizzo `http://localhost:5000`

## Sicurezza

- Password hashate con Werkzeug security
- Protezione della sessione utente
- Chiave segreta configurabile
- Validazione dei dati in input
