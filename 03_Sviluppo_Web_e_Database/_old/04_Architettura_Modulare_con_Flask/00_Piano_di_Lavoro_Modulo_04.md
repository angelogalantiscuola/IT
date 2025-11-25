# Piano di Lavoro: Capitolo 04 - Architettura Modulare con Flask

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Aver completato e compreso l'applicazione monolitica `flask_1` del Capitolo 03.
*   Familiarità con la struttura di base di un'applicazione Flask.

### Competenze in Uscita
Al termine di questo capitolo, lo studente sarà in grado di:
*   Spiegare i limiti di un'applicazione monolitica e i vantaggi di un'architettura modulare.
*   Applicare il principio della **Separazione delle Responsabilità (SoC)** all'interno di un progetto web.
*   Ristrutturare un'applicazione Flask da un singolo file a una **struttura a pacchetto**.
*   Implementare il pattern **Application Factory** per creare e configurare l'istanza dell'app in modo flessibile.
*   Organizzare e isolare la logica delle route in moduli separati utilizzando i **Blueprints**.
*   Rappresentare la struttura logica di un'applicazione basata su Blueprints con un **Diagramma delle Classi UML**.

## 2. Contenuti Teorici e Pratici (Lezioni)
Questo capitolo è interamente focalizzato sul **refactoring** dell'applicazione `flask_1`. Non introdurremo nuove funzionalità, ma miglioreremo radicalmente la qualità e l'organizzazione del codice esistente.

*   **Lezione 01: I Limiti di un'Applicazione Monolitica**
    *   **Teoria:** Analisi critica del file `app.py` di `flask_1`. Discussione sui problemi di manutenibilità, leggibilità e scalabilità. Introduzione al principio della Separazione delle Responsabilità.

*   **Lezione 02: Refactoring: Application Factory e Struttura a Pacchetto**
    *   **Teoria:** Il pattern Application Factory (`create_app`) e i suoi vantaggi. Come Python gestisce i pacchetti (`__init__.py`).
    *   **Pratica:** Creazione della nuova struttura di cartelle del progetto `flask_2`. Scrittura del file `app/__init__.py` con la funzione `create_app()` e centralizzazione della configurazione e della gestione del database.

*   **Lezione 03: Organizzare le Route con i Blueprints**
    *   **Teoria:** Cos'è un Blueprint e come funziona. Sintassi per la creazione e la registrazione di un Blueprint.
    *   **Pratica:** Creazione dei file `app/auth.py` e `app/posts.py`. Spostamento delle funzioni delle route da `flask_1` nei rispettivi Blueprints. Adattamento delle chiamate `render_template` e `url_for` alla nuova struttura.

*   **Lezione 04: Disegnare l'Architettura Modulare con UML**
    *   **Teoria:** Come usare un Diagramma delle Classi UML per rappresentare componenti logici (non solo dati). Uso degli stereotipi `<<Blueprint>>` e `<<Application>>`.
    *   **Pratica:** Creazione di un diagramma UML che descrive la nuova architettura di `flask_2`, mostrando come l'applicazione principale registra i Blueprints e quali sono le principali funzionalità di ciascuno.

## 3. Attività Principale: Progetto `flask_2` (Refactoring Architetturale)
L'attività centrale del capitolo è il **refactoring guidato** dell'applicazione `flask_1`. L'obiettivo è ottenere una nuova applicazione, `flask_2`, che sia funzionalmente identica alla precedente ma con una struttura del codice professionale e modulare.

## 4. Metodologie di Valutazione
*   Valutazione del codice del progetto `flask_2` ristrutturato, con particolare attenzione alla corretta implementazione dell'Application Factory e alla separazione logica ottenuta con i Blueprints.
*   Analisi del diagramma UML prodotto per verificare la comprensione della nuova architettura.

## 5. Strumenti Necessari
*   Tutti gli strumenti del capitolo precedente.
*   Strumenti per la creazione di diagrammi UML (es. Mermaid in VS Code).