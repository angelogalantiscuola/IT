## Fondamenti di Database <!-- omit in toc -->

- [Definizione di Database](#definizione-di-database)
- [Sistema di Gestione di Database (DBMS)](#sistema-di-gestione-di-database-dbms)
- [Tipologie di Database](#tipologie-di-database)


I database sono un elemento cruciale nell'informatica moderna, in quanto permettono la raccolta, la gestione e il recupero efficiente di grandi quantità di dati. Questa lezione introduce i concetti fondamentali che costituiscono la base dei sistemi di database.

### Definizione di Database

Un **database** è un insieme organizzato di dati strutturati, tipicamente archiviati e gestiti tramite un sistema di gestione di database (DBMS). L'obiettivo principale di un database è quello di consentire l'archiviazione e il recupero efficiente delle informazioni, oltre a garantire la loro integrità, consistenza e sicurezza.

### Sistema di Gestione di Database (DBMS)

Un **DBMS** è un software che permette di interagire con il database. Questo sistema si occupa di gestire la struttura dei dati, l'accesso simultaneo di più utenti e l'integrità delle informazioni. Alcuni esempi di DBMS popolari includono MySQL, PostgreSQL, Microsoft SQL Server e Oracle.

Il DBMS svolge diverse funzioni chiave:
- **Archiviazione dei dati**: gestisce la memorizzazione e l'organizzazione fisica dei dati sul disco.
- **Gestione delle transazioni**: assicura che le operazioni sui dati siano eseguite correttamente, anche in caso di guasti.
- **Controllo della concorrenza**: garantisce che più utenti possano accedere ai dati contemporaneamente senza conflitti.
- **Recupero e ripristino**: protegge i dati da eventuali errori o guasti, permettendo il ripristino dello stato corretto.
- **Sicurezza**: controlla l'accesso ai dati, definendo chi può leggere, modificare o cancellare determinate informazioni.

### Tipologie di Database

I database si possono classificare in diverse tipologie, in base alla loro struttura e alle esigenze che soddisfano. Di seguito, le categorie principali:

- **Database relazionali**: questi database organizzano i dati in tabelle collegate tra loro attraverso relazioni. Ogni tabella è costituita da righe (tuple) e colonne (attributi). Questo tipo di database è basato sul *modello relazionale* (approfondito nella lezione dedicata), e utilizza il linguaggio SQL per interagire con i dati.
  
- **Database NoSQL**: questi database sono progettati per gestire grandi volumi di dati non strutturati o semi-strutturati. Sono flessibili e spesso utilizzati in contesti che richiedono alta scalabilità e velocità, come le applicazioni web in tempo reale. Alcuni esempi includono MongoDB (basato su documenti) e Redis (basato su chiavi-valori).

- **Database gerarchici e a rete**: utilizzano modelli meno comuni in cui i dati sono strutturati come gerarchie o grafi. Questi modelli sono stati utilizzati più spesso in passato, ma sono ancora utili per specifiche applicazioni industriali.
