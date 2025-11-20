# Piano di Lavoro: Capitolo 05 - Interazione con il Database tramite ORM

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Aver completato e compreso l'applicazione `flask_2` con la sua architettura a Blueprints (Capitolo 04).
*   Piena padronanza dei concetti di Programmazione Orientata agli Oggetti (classi, oggetti, metodi).
*   Conoscenza del modello relazionale e di come le tabelle sono collegate tramite chiavi esterne.

### Competenze in Uscita
Al termine di questo capitolo, lo studente sarà in grado di:
*   Spiegare cos'è un Object-Relational Mapper (ORM) e quali vantaggi offre (produttività, sicurezza, manutenibilità).
*   Definire la struttura del database utilizzando **modelli Peewee** (classi Python) invece di uno `schema.sql`.
*   Configurare e integrare Peewee in un'applicazione Flask che usa il pattern Application Factory.
*   Sostituire completamente le query SQL grezze (`db.execute(...)`) con i metodi forniti dall'ORM per tutte le operazioni CRUD.
*   Gestire le relazioni tra tabelle (es. uno-a-molti) a livello di oggetti Python.
*   Aggiornare un diagramma di architettura UML per includere i modelli ORM e le loro relazioni.

## 2. Contenuti Teorici e Pratici (Lezioni)
Questo capitolo è un secondo, importante **refactoring** dell'applicazione `flask_2`. Questa volta, non toccheremo la struttura dei Blueprints, ma ci concentreremo esclusivamente sul livello di accesso ai dati.

*   **Lezione 01: Introduzione all'ORM con Peewee**
    *   **Teoria:** Cos'è un ORM e perché astrae il database. Presentazione dei vantaggi rispetto all'SQL grezzo. Introduzione a Peewee come ORM leggero e "Pythonico".
    *   **Pratica:** Installazione di Peewee. Creazione del file `app/models.py`. Definizione dei modelli `User` e `Post` come classi Peewee, specificando campi e relazioni (`ForeignKeyField`).

*   **Lezione 02: Integrazione di Peewee nell'Applicazione Flask**
    *   **Teoria:** Come gestire il ciclo di vita della connessione al database con un ORM in un contesto web.
    *   **Pratica:** Modifica del file `app/__init__.py` (la Application Factory) per inizializzare Peewee e creare automaticamente le tabelle a partire dai modelli. Rimuovere il vecchio sistema di gestione del DB (`db.py`).

*   **Lezione 03: Sostituire SQL con l'ORM (CRUD in Pratica)**
    *   **Teoria:** Studio della sintassi di Peewee per le operazioni CRUD: `.create()`, `.get_or_none()`, `.select()`, `.save()`, `.delete_instance()`.
    *   **Pratica:** Refactoring completo dei file `app/auth.py` e `app/posts.py`. Sostituzione di ogni chiamata a `get_db().execute(...)` con i metodi equivalenti di Peewee. Adattamento dei template per lavorare con gli oggetti modello invece che con i dizionari `sqlite3.Row`.

*   **Lezione 04: Aggiornare il Diagramma di Architettura**
    *   **Teoria:** Come rappresentare i modelli ORM e le loro relazioni in un diagramma UML.
    *   **Pratica:** Ripresa del diagramma UML creato nel capitolo precedente e aggiunta delle classi `<<Model>> User` e `<<Model>> Post`, mostrando la relazione "uno-a-molti" tra di loro e le dipendenze dai Blueprints.

## 3. Attività Principale: Evoluzione di `flask_2`
L'attività centrale del capitolo è il **refactoring del livello di persistenza** dell'applicazione `flask_2`, sostituendo tutto il codice di accesso al database basato su SQL grezzo con l'ORM Peewee.

## 4. Metodologie di Valutazione
*   Valutazione del codice dell'applicazione `flask_2` finale, verificando la corretta e completa sostituzione dell'SQL con l'ORM.
*   Una verifica pratica in cui si chiede di aggiungere una nuova entità (es. `Commento`) all'applicazione, richiedendo la creazione del modello Peewee e l'implementazione delle route CRUD tramite ORM.

## 5. Strumenti Necessari
*   Tutti gli strumenti del capitolo precedente.
*   **Peewee**: (`pip install peewee`).