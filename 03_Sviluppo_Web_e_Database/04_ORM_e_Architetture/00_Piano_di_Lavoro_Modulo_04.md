# Piano di Lavoro: Modulo 04 - Architetture Robuste e ORM

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Aver completato e compreso l'applicazione `flask_1` del Modulo 03.
*   Piena padronanza dei concetti di Programmazione Orientata agli Oggetti (classi, metodi, attributi).
*   Conoscenza del modello relazionale e dei diagrammi ER.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Spiegare i vantaggi di un'architettura modulare rispetto a un'applicazione monolitica.
*   Ristrutturare un'applicazione Flask utilizzando i **Blueprints** per separare le diverse aree funzionali (es. autenticazione, gestione entries).
*   Spiegare il concetto di Object-Relational Mapping (ORM) e i suoi benefici (produttività, sicurezza, astrazione).
*   Definire modelli di dati utilizzando **SQLModel**, mappando classi Python a tabelle di database.
*   Sostituire le query SQL dirette con le operazioni dell'ORM (creazione di oggetti, query con `select`, aggiornamenti, eliminazioni).
*   Implementare relazioni tra modelli (uno-a-molti, molti-a-molti) direttamente nel codice Python.
*   Applicare il pattern "Model-View-Controller" (o una sua variante come Model-View-Template) per organizzare il codice in modo logico e manutenibile.

## 2. Contenuti Teorici
Questo modulo si concentra sul "come" scrivere codice di qualità, manutenibile e scalabile.

1.  **Architettura dell'Applicazione**:
    *   `architettura_flask.md`: Dalla singola applicazione (`app.py`) a una struttura a pacchetto.
    *   **Flask Blueprints**: Come registrare e utilizzare i blueprint per dividere le route in file logici (`routes/auth.py`, `routes/entries.py`).
    *   **Application Factory Pattern**: L'uso di una funzione `create_app()` per un'inizializzazione più flessibile e testabile dell'applicazione.

2.  **Object-Relational Mapping (ORM)**:
    *   `orm/mapping_object_to_data.md`: La teoria dietro la mappatura tra il modello a oggetti e il modello relazionale.
    *   `orm/SQLModel.md`: Introduzione a SQLModel, la sua sintassi e la sua integrazione con Pydantic e SQLAlchemy.
    *   **Definizione dei Modelli**: Come creare una classe che rappresenti una tabella (`class User(SQLModel, table=True): ...`).
    *   **Sessione ORM**: Il concetto di sessione come intermediario per le operazioni sul database.
    *   **Query con ORM**: Utilizzare `select()` per interrogare il database in modo "Pythonico", senza scrivere SQL.
    *   **Relazioni con ORM**: Definire `Relationship()` per gestire le chiavi esterne e le tabelle associative a livello di oggetti.

## 3. Attività Pratiche / Esercitazioni

L'attività centrale del modulo sarà il **refactoring guidato** dell'applicazione `flask_1` per trasformarla in `flask_2`.

1.  **Ristrutturazione del Progetto**:
    *   Creare la nuova struttura a pacchetto (`app/`, `run.py`, `config.py`).
    *   Implementare l'application factory `create_app()`.
    *   Spostare le route esistenti in Blueprints separati.

2.  **Integrazione dell'ORM**:
    *   Definire i modelli `User` ed `Entry` con SQLModel, sostituendo la necessità di scrivere `CREATE TABLE` manualmente.
    *   Riscrivere tutta la logica di accesso al database (tutte le funzioni in `routes/`) per usare l'ORM invece di `mysql.connector` e SQL grezzo.
        *   *Esempio*: La funzione di login non userà più una `SELECT` SQL, ma `session.exec(select(User).where(User.username == ...)).first()`.
        *   *Esempio*: La creazione di un nuovo utente non sarà più una `INSERT` SQL, ma la creazione di un'istanza `User()` e l'uso di `session.add()` e `session.commit()`.

3.  **Aggiunta di Nuove Funzionalità**: Sfruttando la nuova architettura, aggiungere funzionalità più complesse come la gestione del profilo utente (`routes/profile.py`).

## 4. Metodologie di Valutazione

*   Valutazione del codice del progetto `flask_2` ristrutturato, con particolare attenzione alla corretta applicazione dei Blueprints e all'uso dell'ORM.
*   Una verifica pratica in cui si fornisce un'applicazione basata su `flask_2` e si chiede di aggiungere una nuova entità (es. `Commento`) con il relativo modello ORM, le route e le viste.

## 5. Strumenti Necessari

*   Tutti gli strumenti del modulo precedente.
*   **SQLModel**: (`pip install sqlmodel`).