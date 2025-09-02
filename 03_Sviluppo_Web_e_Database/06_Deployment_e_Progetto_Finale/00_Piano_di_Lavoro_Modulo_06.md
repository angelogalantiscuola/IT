# Piano di Lavoro: Modulo 06 - Deployment e Progetto Finale

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Piena padronanza di tutti i concetti e le competenze sviluppate nei moduli precedenti (Database, Flask, ORM, Testing).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Gestire un progetto software web completo, dall'analisi dei requisiti fino al rilascio.
*   Distinguere tra ambienti di sviluppo e di produzione e gestire le relative configurazioni.
*   Utilizzare le variabili d'ambiente per la gestione sicura di dati sensibili (secret key, credenziali del database).
*   Preparare un'applicazione Flask per il deployment, utilizzando un server WSGI di produzione come Gunicorn.
*   Eseguire il deployment di un'applicazione web su una piattaforma PaaS (Platform-as-a-Service) come Render.
*   Sintetizzare tutte le competenze acquisite (OOP, UML, ER, SQL, Flask, ORM, Pytest) in un unico progetto coerente e funzionante.

## 2. Contenuti Teorici
La teoria di questo modulo è mirata a finalizzare l'applicazione per il mondo reale.

1.  **Preparazione per la Produzione**:
    *   **Ambienti di Sviluppo vs. Produzione**: Differenze chiave (es. `DEBUG=False`).
    *   **Gestione della Configurazione**: L'importanza di non inserire mai "segreti" (password, API keys) nel codice. Utilizzo della libreria `python-dotenv` per caricare configurazioni da un file `.env`.
    *   **Server WSGI di Produzione**: Perché il server di sviluppo di Flask non è adatto alla produzione. Introduzione a `Gunicorn`.
    *   **Gestione delle Dipendenze**: Il ruolo fondamentale del file `requirements.txt`.

2.  **Deployment su una Piattaforma PaaS (Render.com)**:
    *   Cos'è una PaaS e perché semplifica il deployment.
    *   **Processo di Deployment**:
        1.  Collegare il repository GitHub alla piattaforma.
        2.  Configurare il servizio (es. "Web Service").
        3.  Impostare le variabili d'ambiente sulla piattaforma.
        4.  Definire i comandi di build e di avvio (`start command`, es. `gunicorn app:app`).
        5.  Analizzare i log di build e di runtime per il debug.

## 3. Attività Pratiche / Esercitazioni

L'intero modulo è un unico, grande laboratorio incentrato sul progetto finale.

1.  **Refactoring per il Deployment**:
    *   Gli studenti prenderanno l'applicazione `flask_2` e la modificheranno per renderla "production-ready":
        *   Rimuoveranno le configurazioni hard-coded e le sostituiranno con variabili d'ambiente.
        *   Creeranno un file `requirements.txt` (`pip freeze > requirements.txt`).
        *   Testeranno l'avvio locale con Gunicorn.

2.  **Deployment di Prova**:
    *   Come esercizio guidato, ogni studente eseguirà il deploy della propria versione di `flask_2` su Render.com per familiarizzare con il processo.

3.  **Sviluppo del Progetto Finale**:
    *   Gli studenti (individualmente o in piccoli gruppi) lavoreranno al loro progetto finale, che dovrà essere sviluppato seguendo tutte le best practice apprese.
    *   **Fase 1: Progettazione**: Analisi dei requisiti, creazione del diagramma ER e del diagramma delle classi UML. Questa è la prima consegna obbligatoria.
    *   **Fase 2: Sviluppo e Testing**: Implementazione dell'applicazione Flask con architettura a Blueprints, modelli SQLModel e una suite di test con `pytest-flask`.
    *   **Fase 3: Deployment**: Consegna finale del link al repository GitHub e del link all'applicazione funzionante e deployata su Render.

## 4. Metodologie di Valutazione

La valutazione del progetto finale sarà olistica e rappresenterà la sintesi del percorso triennale.

1.  **Qualità della Progettazione (25%)**: Valutazione dei diagrammi ER e UML.
2.  **Correttezza e Qualità del Codice (45%)**: Coerenza con il design, corretta applicazione di Flask, ORM, Blueprints e principi di sicurezza.
3.  **Qualità dei Test (15%)**: Copertura delle funzionalità principali con test significativi.
4.  **Successo del Deployment e Funzionamento (15%)**: L'applicazione deve essere funzionante e accessibile tramite l'URL pubblico.

## 5. Strumenti Necessari

*   Tutti gli strumenti dei moduli precedenti.
*   `python-dotenv` (`pip install python-dotenv`).
*   `gunicorn` (`pip install gunicorn`).
*   Un account GitHub.
*   Un account gratuito su una piattaforma PaaS (es. [Render.com](https://render.com/)).