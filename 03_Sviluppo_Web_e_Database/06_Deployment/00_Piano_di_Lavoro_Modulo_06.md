# Piano di Lavoro: Modulo 06 - Deployment in Cloud

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Applicazione Flask completa e funzionante (dal Modulo 05).
*   Progetto pushato su un repository GitHub.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Distinguere tra ambiente di **Sviluppo** (Debug attivo, server leggero) e **Produzione** (Performance, Sicurezza).
*   Configurare un server **WSGI di produzione** (Gunicorn) per servire l'applicazione Flask.
*   Gestire le dipendenze del progetto tramite il file `requirements.txt`.
*   Utilizzare le **Variabili d'Ambiente** per nascondere dati sensibili (Secret Key, URL Database).
*   Effettuare il deployment di un'applicazione su una piattaforma **PaaS** (Render.com).
*   Collegare l'applicazione a un database di produzione (PostgreSQL su Render) sostituendo SQLite.

## 2. Contenuti Teorici e Pratici

Il passaggio a produzione è spesso traumatico per gli studenti. Questo modulo rende il processo lineare e comprensibile.

*   **Lezione 01: Preparazione per la Produzione**
    *   **Teoria:** Perché `flask run` non va bene per internet. Cos'è un WSGI Server (Gunicorn). Gestione delle librerie (`pip freeze > requirements.txt`).
    *   **Pratica:** Installazione di Gunicorn. Creazione di `requirements.txt`. Test locale dell'app lanciata con Gunicorn.

*   **Lezione 02: Configurazione e Sicurezza (Environment Variables)**
    *   **Teoria:** "Hardcoding" vs Configurazione dinamica. Perché non si committano mai le password su Git. La libreria `python-dotenv`.
    *   **Pratica:** Modifica di `config.py` (o `__init__.py`) per leggere `SECRET_KEY` e `DATABASE_URL` dalle variabili d'ambiente (`os.environ`). Creazione del file `.env` (e inserimento in `.gitignore`).

*   **Lezione 03: Deployment su Render.com**
    *   **Teoria:** IaaS vs PaaS. Continuous Deployment (Git push -> Deploy automatico).
    *   **Pratica:** Creazione account Render. Collegamento repository GitHub. Configurazione del servizio Web ("Build Command", "Start Command"). Setup del database PostgreSQL (facoltativo ma consigliato per evitare la perdita dati di SQLite su Render).

## 3. Attività Principale: "It's Live!"
Gli studenti prenderanno il loro Blog (sviluppato nei moduli precedenti) e lo pubblicheranno su Render.com.
Alla fine del modulo, ogni studente avrà un URL pubblico (es. `mio-blog.onrender.com`) da poter condividere e testare da smartphone.

## 4. Metodologie di Valutazione
*   L'applicazione è raggiungibile online?
*   Il codice su GitHub **NON** contiene la Secret Key (verifica di sicurezza).
*   Se l'app viene riavviata su Render, i dati persistono (successo nel passaggio a PostgreSQL) o si resettano (uso di SQLite effimero - accettabile ma da notare).