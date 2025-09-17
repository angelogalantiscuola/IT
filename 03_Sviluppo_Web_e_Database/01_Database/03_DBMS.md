## Sistema di Gestione di Database (DBMS) <!-- omit in toc -->

- [Archiviazione dei Dati](#archiviazione-dei-dati)
- [Gestione delle Transazioni](#gestione-delle-transazioni)
- [Controllo della Concorrenza](#controllo-della-concorrenza)
- [Recupero e Ripristino](#recupero-e-ripristino)
- [Sicurezza](#sicurezza)

Un **DBMS** (Database Management System) è un software complesso progettato per gestire i database in modo efficiente, consentendo la memorizzazione, la gestione e il recupero dei dati in modo sicuro e affidabile. Per comprendere meglio il funzionamento di un DBMS, vediamo in dettaglio le sue funzioni chiave:

### Archiviazione dei Dati

Il DBMS gestisce la memorizzazione fisica dei dati su disco rigido o altri dispositivi di archiviazione permanenti. I dati sono organizzati in tabelle, ognuna composta da righe (tuple) e colonne (attributi).

Oltre all'archiviazione, il DBMS ottimizza la disposizione fisica dei dati per migliorare le prestazioni delle query, ad esempio attraverso tecniche come la **normalizzazione** o l'uso di **indici**.

### Gestione delle Transazioni

Una transazione è un insieme di operazioni che vengono eseguite come un'unità logica. Il DBMS garantisce che tutte le operazioni all'interno di una transazione vengano completate correttamente o, in caso di errore, annullate (rollback) per mantenere l'integrità dei dati. Questo si basa sulle proprietà **ACID**:

- **Atomicità**: tutte le operazioni della transazione devono essere completate, oppure nessuna viene eseguita.
- **Coerenza**: una transazione deve portare il database da uno stato valido a un altro.
- **Isolamento**: le transazioni in esecuzione contemporaneamente non devono interferire tra loro.
- **Durabilità**: una volta completata, una transazione deve essere permanente, anche in caso di guasti.

### Controllo della Concorrenza

Il **controllo della concorrenza** è necessario quando più utenti o applicazioni accedono simultaneamente al database. Il DBMS deve garantire che le operazioni eseguite da un utente non interferiscano con quelle di altri utenti, mantenendo l'integrità dei dati. Questo avviene spesso tramite **locking** (blocco): il DBMS blocca temporaneamente le risorse utilizzate da una transazione fino a quando questa non è completata.

### Recupero e Ripristino

Il **recupero** dei dati è un aspetto cruciale per i DBMS, che devono garantire la possibilità di ripristinare il database a uno stato coerente in caso di guasti (interruzioni di corrente, errori hardware o software). Le tecniche di ripristino includono:

- **Backup**: copie periodiche del database.
- **Log delle transazioni**: un registro di ogni modifica effettuata, per poter annullare o ripetere le operazioni in modo sicuro.

### Sicurezza

La sicurezza è fondamentale per impedire l'accesso non autorizzato ai dati. Un DBMS offre vari meccanismi per garantire che solo gli utenti autorizzati possano accedere o modificare i dati:

- **Controllo degli accessi**: il DBMS permette di definire chi può eseguire operazioni specifiche sul database (lettura, scrittura, modifica, eliminazione).
- **Autenticazione**: gli utenti devono fornire credenziali valide (come username e password) per accedere al sistema.
- **Autorizzazione**: una volta autenticato, l'utente ha determinati permessi associati al suo account.
- **Crittografia**: il DBMS può crittografare i dati, sia "a riposo" (su disco) che "in transito" (sulla rete).
