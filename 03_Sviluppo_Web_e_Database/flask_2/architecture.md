# Architettura dell'Applicazione Flask

## Diagrammi UML

L'architettura dell'applicazione è documentata attraverso tre diagrammi UML:

1. **Diagramma delle Classi** (diagramma_classi.md)

   - Mostra le relazioni tra le classi principali
   - Illustra i metodi e gli attributi delle classi
   - Evidenzia le dipendenze tra i componenti

2. **Diagramma ER** (diagramma_er.md)

   - Rappresenta la struttura del database
   - Mostra le relazioni tra le entità
   - Definisce i vincoli e le chiavi

3. **Diagramma di Sequenza** (diagramma_sequenza.md)
   - Illustra il flusso di autenticazione
   - Mostra il processo di creazione delle entries
   - Evidenzia le interazioni tra i componenti

## Struttura del Progetto

```
flask_2/
├── app/                  # Directory principale dell'applicazione
│   ├── __init__.py      # Inizializzazione dell'app Flask
│   ├── app.py           # Configurazione e creazione dell'app
│   ├── auth.py          # Gestione dell'autenticazione
│   ├── database.py      # Gestione del database MySQL
│   ├── routes/          # Blueprint per il routing
│   │   ├── auth.py      # Route per l'autenticazione
│   │   ├── entries.py   # Route per la gestione dei messaggi
│   │   └── profile.py   # Route per la gestione del profilo
│   ├── models/          # Modelli dei dati
│   │   ├── user.py      # Modello utente
│   │   └── entry.py     # Modello entry
├── static/              # File statici (CSS, JSON)
│   ├── styles.css       # Stili dell'applicazione
│   └── messages.json    # Dati iniziali per i messaggi
├── templates/           # Template HTML
│   ├── layout.html      # Template base
│   ├── index.html       # Pagina principale
│   ├── list.html        # Lista dei messaggi
│   ├── login.html       # Pagina di login
│   ├── menu.html        # Menu di navigazione
│   ├── profile.html     # Pagina del profilo
│   └── register.html    # Pagina di registrazione
└── run.py               # Script per l'avvio dell'applicazione
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
- Configurazione delle sessioni
- Impostazioni di sicurezza

### Modelli (app/models/)

#### User (models/user.py)

- Gestione degli utenti
- Metodi per:
  - Autenticazione
  - Gestione profilo
  - Hashing password
  - Verifica password

#### Entry (models/entry.py)

- Gestione delle entries
- Funzionalità per:
  - CRUD operations
  - Ricerca
  - Filtraggio
  - Validazione dati

### Database (app/database.py)

Il modulo gestisce l'interazione con MySQL:

```sql
-- Tabella users
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabella entries
CREATE TABLE entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(80) NOT NULL,
    message VARCHAR(200) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### Blueprint Routes (app/routes/)

L'applicazione utilizza il pattern Blueprint per organizzare le route:

1. **Auth** (routes/auth.py)

   - Login/Logout (`/auth/login`, `/auth/logout`)
   - Registrazione (`/auth/register`)
   - Reset password (`/auth/reset`)
   - Protezione route con decoratori

2. **Entries** (routes/entries.py)

   - Lista entries (`/entries`)
   - Creazione (`/entries/create`)
   - Modifica (`/entries/<id>/edit`)
   - Eliminazione (`/entries/<id>/delete`)
   - Ricerca e filtri

3. **Profile** (routes/profile.py)
   - Visualizzazione profilo (`/profile`)
   - Modifica profilo (`/profile/edit`)
   - Cambio password (`/profile/password`)

## Flusso dell'Applicazione

1. **Inizializzazione**

   - Avvio da `run.py`
   - Creazione app Flask
   - Configurazione database
   - Registrazione blueprint

2. **Gestione Richieste**

   - Routing attraverso blueprint
   - Autenticazione e autorizzazione
   - Validazione input
   - Gestione sessioni

3. **Interazione Database**

   - Connessione pooling
   - Query parametrizzate
   - Gestione transazioni
   - Sicurezza dati

4. **Rendering**
   - Template Jinja2
   - Gestione errori
   - Messaggi flash
   - Redirect sicuri

## Sicurezza

- **Autenticazione**

  - Password hashate con Werkzeug
  - Protezione sessioni
  - Token CSRF
  - Rate limiting

- **Database**

  - Query parametrizzate
  - Escape automatico
  - Validazione input
  - Gestione permessi

- **Applicazione**
  - Headers di sicurezza
  - Protezione XSS
  - Sanitizzazione input
  - Logging errori

## Utilizzo

Per avviare l'applicazione:

```bash
python run.py
```

L'applicazione sarà accessibile all'indirizzo `http://localhost:5000`

### Utente Default

- Username: admin
- Password: password (da cambiare al primo accesso)

Per maggiori dettagli sulle interazioni tra i componenti, consultare i diagrammi UML nella documentazione.
