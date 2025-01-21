# Architettura dell'Applicazione Flask

## Struttura del Progetto

```
flask/
├── app/                      # Directory principale del pacchetto
│   ├── __init__.py          # Factory dell'applicazione
│   ├── models/              # Modelli per l'interazione con il database
│   │   ├── __init__.py
│   │   ├── user.py         # Modello User per gli utenti
│   │   └── entry.py        # Modello Entry per i messaggi
│   ├── routes/             # Blueprints per il routing
│   │   ├── __init__.py
│   │   ├── auth.py        # Route per l'autenticazione
│   │   ├── entries.py     # Route per la gestione dei messaggi
│   │   └── profile.py     # Route per la gestione del profilo
│   ├── database.py        # Gestione della connessione al database
│   └── auth.py           # Utilità per l'autenticazione
├── static/               # File statici (CSS, JS, ecc.)
├── templates/           # Template HTML
├── config.py           # Configurazione dell'applicazione
└── run.py             # Punto di ingresso dell'applicazione
```

## Componenti Principali

### Models (app/models/)

I modelli definiscono la struttura dei dati e l'interazione con il database.

#### User (models/user.py)

- Gestisce le operazioni CRUD per gli utenti
- Implementa la verifica della password
- Fornisce metodi di ricerca per ID e username

#### Entry (models/entry.py)

- Gestisce le operazioni CRUD per i messaggi
- Implementa la ricerca di messaggi
- Gestisce l'eliminazione sicura dei record

### Routes (app/routes/)

I blueprint organizzano le route in moduli logici.

#### Auth (routes/auth.py)

- Gestione registrazione utenti
- Login e logout
- Reset della password
- Implementa la protezione delle route

#### Entries (routes/entries.py)

- Visualizzazione lista messaggi
- Creazione nuovi messaggi
- Modifica messaggi esistenti
- Eliminazione messaggi
- Implementa la protezione delle route autenticate

#### Profile (routes/profile.py)

- Visualizzazione profilo utente
- Aggiornamento dati utente
- Gestione sessione utente

### Utilità

#### Database (app/database.py)

- Gestione connessione al database MySQL
- Inizializzazione schema database
- Funzioni helper per le query

#### Auth (app/auth.py)

- Decoratore login_required
- Gestione sessione utente
- Utilità per l'autenticazione

### Configurazione

#### Config (config.py)

- Configurazioni del database
- Chiave segreta dell'applicazione
- Altre impostazioni dell'ambiente

#### Factory (app/**init**.py)

- Inizializzazione dell'applicazione Flask
- Registrazione dei blueprint
- Configurazione iniziale del database
- Caricamento dati iniziali

## Flusso dell'Applicazione

1. L'applicazione viene avviata da `run.py`
2. La factory in `__init__.py` crea l'istanza dell'applicazione
3. Vengono caricate le configurazioni da `config.py`
4. Il database viene inizializzato con `database.py`
5. I blueprint vengono registrati per gestire le route
6. I modelli gestiscono l'interazione con il database
7. Le route gestiscono le richieste HTTP
8. I template rendono le pagine HTML

## Utilizzo

Per avviare l'applicazione:

```bash
python run.py
```

L'applicazione sarà accessibile all'indirizzo `http://localhost:5000`
