## Sistema di Gestione di Database (DBMS)

Un **DBMS** (Database Management System) è un software complesso progettato per gestire i database in modo efficiente, consentendo la memorizzazione, la gestione e il recupero dei dati in modo sicuro e affidabile. Per comprendere meglio il funzionamento di un DBMS, vediamo in dettaglio le sue funzioni chiave:

### 1. **Archiviazione dei Dati**

Il DBMS gestisce la memorizzazione fisica dei dati su disco rigido o altri dispositivi di archiviazione permanenti. I dati sono organizzati in tabelle, ognuna composta da righe (tuple) e colonne (attributi). 

- **Esempio**: In un sistema di gestione delle vendite, i dettagli di ogni transazione (data, prodotto venduto, quantità, prezzo) vengono salvati in una tabella chiamata `Transazioni`.
  
  ```sql
  CREATE TABLE Transazioni (
    id INT PRIMARY KEY,
    data DATE,
    prodotto VARCHAR(255),
    quantita INT,
    prezzo DECIMAL(10, 2)
  );
  ```

Oltre all'archiviazione, il DBMS ottimizza la disposizione fisica dei dati per migliorare le prestazioni delle query, ad esempio attraverso tecniche come la **normalizzazione** o l'uso di **indici**.

### 2. **Gestione delle Transazioni**

Una transazione è un insieme di operazioni che vengono eseguite come un'unità logica. Il DBMS garantisce che tutte le operazioni all'interno di una transazione vengano completate correttamente o, in caso di errore, annullate (rollback) per mantenere l'integrità dei dati. Questo si basa sulle proprietà **ACID**:

- **Atomicità**: tutte le operazioni della transazione devono essere completate, oppure nessuna viene eseguita.
- **Coerenza**: una transazione deve portare il database da uno stato valido a un altro.
- **Isolamento**: le transazioni in esecuzione contemporaneamente non devono interferire tra loro.
- **Durabilità**: una volta completata, una transazione deve essere permanente, anche in caso di guasti.

- **Esempio**: Supponiamo di voler trasferire denaro tra due conti bancari. Una transazione potrebbe consistere in due operazioni: detrarre un importo dal primo conto e aggiungerlo al secondo.

  ```sql
  START TRANSACTION;
  UPDATE Conti SET saldo = saldo - 100 WHERE id = 1;
  UPDATE Conti SET saldo = saldo + 100 WHERE id = 2;
  COMMIT;
  ```

Se uno degli aggiornamenti fallisce, l'intera transazione viene annullata per evitare stati incoerenti.

### 3. **Controllo della Concorrenza**

Il **controllo della concorrenza** è necessario quando più utenti o applicazioni accedono simultaneamente al database. Il DBMS deve garantire che le operazioni eseguite da un utente non interferiscano con quelle di altri utenti, mantenendo l'integrità dei dati.

Esistono due approcci principali al controllo della concorrenza:

- **Locking** (blocco): il DBMS blocca temporaneamente le risorse utilizzate da una transazione fino a quando questa non è completata.
  
- **Versioning** (multiversion concurrency control - MVCC): il DBMS mantiene diverse versioni degli stessi dati, consentendo a più utenti di leggere dati "vecchi" mentre altre transazioni li stanno modificando.

- **Esempio**: Se due utenti tentano di aggiornare contemporaneamente la stessa riga di una tabella `Inventario`, il DBMS può bloccare temporaneamente la riga per l'utente A finché non completa la sua operazione, impedendo all'utente B di apportare modifiche fino al termine.

  ```sql
  -- L'utente A blocca la riga dell'articolo con id 10
  UPDATE Inventario SET quantita = quantita - 10 WHERE id = 10;
  ```

### 4. **Recupero e Ripristino**

Il **recupero** dei dati è un aspetto cruciale per i DBMS, che devono garantire la possibilità di ripristinare il database a uno stato coerente in caso di guasti, come interruzioni dell'alimentazione, errori hardware o software.

Le tecniche di ripristino includono:

- **Backup**: il DBMS permette di creare copie periodiche del database (backup), che possono essere utilizzate per ripristinare i dati in caso di problemi.
- **Log delle transazioni**: il DBMS registra ogni modifica effettuata ai dati in un log separato, in modo che in caso di guasto si possano ripristinare le operazioni incomplete.
- **Checkpoint**: periodicamente, il DBMS scrive nel disco tutti i dati in memoria e segnala che fino a quel punto tutte le transazioni sono state correttamente eseguite.

- **Esempio**: Se durante una transazione complessa si verifica un'interruzione di corrente, il DBMS può utilizzare il log delle transazioni per identificare quali operazioni erano state completate e quali no, ripristinando così il database a uno stato coerente.

### 5. **Sicurezza**

La sicurezza è fondamentale per impedire l'accesso non autorizzato ai dati. Un DBMS offre vari meccanismi per garantire che solo gli utenti autorizzati possano accedere o modificare i dati. Le tecniche di sicurezza includono:

- **Controllo degli accessi**: il DBMS permette di definire chi può eseguire operazioni specifiche sul database (lettura, scrittura, modifica, eliminazione).
- **Autenticazione**: gli utenti devono fornire credenziali valide (come username e password) per accedere al sistema.
- **Autorizzazione**: una volta autenticato, l'utente ha determinati permessi associati al suo account. Questi permessi possono essere concessi a livello di tabella, colonna o riga.
- **Crittografia**: il DBMS può crittografare i dati, sia a riposo che in transito, per proteggerli da intercettazioni.

- **Esempio**: In un sistema di gestione del personale, solo gli amministratori possono modificare i dettagli degli stipendi. Gli utenti regolari possono visualizzare solo i propri dati.

  ```sql
  GRANT SELECT ON Salari TO utente_regolare;
  GRANT ALL PRIVILEGES ON Salari TO amministratore;
  ```

### Conclusioni

Un DBMS è uno strumento potente che gestisce tutte le complessità legate alla memorizzazione, alla sicurezza e alla manipolazione dei dati. Grazie a funzionalità come l'archiviazione efficiente, il controllo delle transazioni, il controllo della concorrenza, il recupero in caso di guasti e la sicurezza avanzata, i DBMS sono fondamentali per gestire i dati in modo affidabile e sicuro in qualsiasi sistema.