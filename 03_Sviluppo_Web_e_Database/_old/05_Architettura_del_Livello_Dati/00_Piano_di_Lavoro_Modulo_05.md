# Piano di Lavoro: Capitolo 05 - Architettura del Livello Dati (Repository Pattern)

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Aver completato il refactoring dell'applicazione in una struttura a Blueprints (`flask_2` dal Capitolo 04).
*   Piena padronanza della scrittura di query SQL grezze e parametrizzate.

### Competenze in Uscita
Al termine di questo capitolo, lo studente sarà in grado di:
*   Spiegare l'importanza di un **Data Access Layer (DAL)** e il ruolo del **Repository Pattern**.
*   Identificare e separare la logica di accesso ai dati dalla logica di gestione delle richieste web.
*   Creare un "livello repository" in un'applicazione Flask, organizzando le query SQL in moduli dedicati.
*   Riscrivere le funzioni delle route (view function) in modo che deleghino tutte le operazioni sul database al livello repository.
*   Creare un'applicazione disaccoppiata, più facile da leggere, manutenere e testare.

## 2. Contenuti Teorici e Pratici (Lezioni)
Questo capitolo è il secondo e ultimo grande **refactoring** dell'applicazione `flask_2`. L'obiettivo è "pulire" l'interno dei Blueprints, spostando tutta la logica SQL in uno strato separato.

*   **Lezione 01: Introduzione al Repository Pattern**
    *   **Teoria:** Perché mescolare SQL e logica delle route è una cattiva pratica (codice accoppiato). Introduzione al concetto di **Data Access Layer (DAL)** come strato di astrazione. Spiegazione del Repository Pattern con l'analogia del "magazziniere": un modulo specializzato che sa solo come parlare con il database.

*   **Lezione 02: Implementare i Repository**
    *   **Teoria:** Come strutturare i moduli del repository (uno per ogni entità principale).
    *   **Pratica:** Creazione della nuova cartella `app/data` (o `app/repositories`). Creazione dei file `user_repository.py` e `post_repository.py`. Spostamento di **tutto il codice SQL** (le query `SELECT`, `INSERT`, `UPDATE`, `DELETE`) e la gestione di `get_db()` all'interno di funzioni dedicate in questi nuovi file.

*   **Lezione 03: Refactoring delle Route per Usare i Repository**
    *   **Teoria:** Il flusso di dati in un'architettura a 3 livelli (Route -> Repository -> Database).
    *   **Pratica:** Modifica dei file `app/auth.py` e `app/posts.py`. Rimozione di ogni riferimento a `get_db()` e `db.execute()`. Sostituzione delle vecchie chiamate con le nuove funzioni del livello repository (es. `user = user_repository.find_by_username(username)`).

## 3. Attività Principale: Finalizzazione di `flask_2`
L'attività centrale del capitolo è il **refactoring del livello dati** dell'applicazione `flask_2`. Gli studenti prenderanno l'applicazione modulare creata nel capitolo precedente e la renderanno ancora più professionale, disaccoppiando completamente la logica web dalla logica di persistenza.

## 4. Metodologie di Valutazione
*   Valutazione del codice finale dell'applicazione `flask_2`, verificando che i Blueprints siano completamente privi di codice SQL e che tutta l'interazione con il database avvenga tramite il livello repository.
*   Una verifica pratica in cui si chiede di aggiungere una nuova funzionalità all'applicazione, richiedendo la creazione di un nuovo file repository e il suo corretto utilizzo all'interno di una nuova route.

## 5. Strumenti Necessari
*   Tutti gli strumenti del capitolo precedente. Non sono richieste nuove installazioni.