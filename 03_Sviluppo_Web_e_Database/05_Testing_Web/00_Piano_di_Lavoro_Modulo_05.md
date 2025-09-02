# Piano di Lavoro: Modulo 05 - Qualità e Testing per il Web

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Aver completato e compreso l'applicazione `flask_2`.
*   Conoscenza dei concetti di base di `pytest` (test functions, assert).
*   Familiarità con il concetto di richiesta/risposta HTTP.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Spiegare perché il testing è fondamentale in un'applicazione web per prevenire regressioni.
*   Configurare un ambiente di testing per un'applicazione Flask.
*   Utilizzare le **fixtures** di `pytest`, in particolare il `client` di test fornito da `pytest-flask`.
*   Scrivere unit test per le funzioni di utility e i metodi dei modelli.
*   Scrivere **integration test** per gli endpoint dell'applicazione, simulando richieste HTTP (GET, POST).
*   Verificare lo status code, gli header e il contenuto (HTML) delle risposte.
*   Testare la logica di autenticazione: testare che le pagine protette siano inaccessibili da non autenticati e accessibili dopo il login.
*   Testare le operazioni CRUD verificando non solo la risposta HTTP, ma anche lo stato del database prima e dopo l'operazione.

## 2. Contenuti Teorici
Questo modulo si concentra sull'applicazione pratica del testing, riprendendo e specializzando concetti già noti.

1.  **Setup dell'Ambiente di Testing**:
    *   Installazione di `pytest` e `pytest-flask`.
    *   Creazione di una configurazione di Flask specifica per il testing (es. con un database separato o in memoria).
    *   Struttura della cartella `tests/`.

2.  **Il Test Client di Flask**:
    *   Cos'è una "fixture" di `pytest`.
    *   Come usare la fixture `client` per simulare richieste all'applicazione senza avviare un server reale.
    *   Esempi: `client.get('/login')`, `client.post('/login', data={'username': '...'})`.

3.  **Tipologie di Test per il Web**:
    *   **Unit Test**: Testare i modelli (es. `user.verify_password()`) in isolamento.
    *   **Integration Test**: Testare un flusso completo, dall'invio di una richiesta a una route fino alla verifica della risposta e della modifica sul database. Questo sarà il nostro focus principale.

4.  **Strategie di Testing**:
    *   **Testare le Pagine Pubbliche (GET)**: Verificare che le pagine come il login o la registrazione rispondano con uno status code `200 OK` e che contengano un testo specifico nell'HTML.
    *   **Testare le Pagine Protette**: Verificare che l'accesso a una pagina protetta senza login produca un redirect (status code `302 Found`).
    *   **Testare i Form (POST)**:
        *   Simulare l'invio di dati validi e verificare che l'operazione vada a buon fine (es. un utente viene creato nel DB, si viene reindirizzati alla pagina di login).
        *   Simulare l'invio di dati non validi e verificare che venga mostrato un messaggio d'errore.
    *   **Testare la Sessione**: Come simulare un utente loggato per i test che richiedono autenticazione.

## 3. Attività Pratiche / Esercitazioni

L'attività principale sarà scrivere una suite di test completa per l'applicazione `flask_2`.

1.  **Test di Base**:
    *   Scrivere un test che verifichi che la pagina di login (`/login`) sia accessibile.
    *   Scrivere un test per un modello, ad esempio `test_password_hashing()` per la classe `User`.

2.  **Test del Flusso di Autenticazione**:
    *   `test_successful_registration()`: Simula una registrazione e controlla che il nuovo utente esista nel database.
    *   `test_successful_login_logout()`: Simula un login, verifica che una pagina protetta diventi accessibile, e poi simula il logout.
    *   `test_protected_route_access()`: Verifica che un utente non loggato venga reindirizzato se tenta di accedere a una pagina protetta.

3.  **Test delle Funzionalità CRUD**:
    *   `test_create_entry()`: Simula il login, poi l'invio del form per creare una nuova entry e infine verifica che la nuova entry sia presente nella lista e nel database.
    *   `test_delete_entry()`: Simula il login, l'eliminazione di un'entry e verifica che non sia più presente nel database.

## 4. Metodologie di Valutazione

*   Correzione della suite di test scritta per il progetto `flask_2`, valutando la copertura dei casi d'uso principali (autenticazione, CRUD).
*   Una verifica pratica dove viene fornita un'applicazione con una nuova funzionalità (es. un sistema di commenti) e si chiede di scrivere i test per validarne il comportamento.

## 5. Strumenti Necessari

*   `pytest` (`pip install pytest`).
*   `pytest-flask` (`pip install pytest-flask`).
*   Tutti gli strumenti dei moduli precedenti.