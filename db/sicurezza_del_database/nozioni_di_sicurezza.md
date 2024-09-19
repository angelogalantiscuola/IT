# Nozioni di Sicurezza <!-- omit in toc -->

- [Tipi di Minacce alla Sicurezza](#tipi-di-minacce-alla-sicurezza)
- [Principali Misure di Sicurezza](#principali-misure-di-sicurezza)
  - [Autenticazione](#autenticazione)
  - [Autorizzazione e Controllo degli Accessi](#autorizzazione-e-controllo-degli-accessi)
  - [Crittografia](#crittografia)
  - [Audit e Log](#audit-e-log)
  - [Backup Sicuro](#backup-sicuro)
  - [Minimizzazione delle Superfici di Attacco](#minimizzazione-delle-superfici-di-attacco)
- [Protezione dalle Minacce Comuni](#protezione-dalle-minacce-comuni)
  - [SQL Injection](#sql-injection)
    - [Come prevenire l'SQL Injection:](#come-prevenire-lsql-injection)
  - [Gestione degli Utenti e Permessi](#gestione-degli-utenti-e-permessi)
  - [Configurazione e Aggiornamenti di Sicurezza](#configurazione-e-aggiornamenti-di-sicurezza)


La sicurezza dei database è un aspetto fondamentale per garantire l'integrità, la riservatezza e la disponibilità dei dati. Senza adeguate misure di protezione, un database può diventare vulnerabile a una serie di minacce, tra cui accessi non autorizzati, furto di dati e attacchi malevoli. Questa lezione si focalizza sulle principali nozioni di sicurezza che devono essere considerate durante la progettazione, implementazione e gestione di un database.

## Tipi di Minacce alla Sicurezza

Prima di esplorare le misure di sicurezza, è utile comprendere le principali minacce che possono colpire un sistema di database:

- **Accesso non autorizzato**: utenti o entità non autorizzate che cercano di accedere al database e ai suoi dati.
- **Modifica dei dati non autorizzata**: un utente malintenzionato potrebbe cercare di modificare dati sensibili.
- **Furto di dati**: il prelievo illecito di informazioni private o sensibili, come numeri di carte di credito o dati personali.
- **Negazione del servizio (DoS)**: attacchi che mirano a rendere il sistema indisponibile, sovraccaricandolo con richieste.

## Principali Misure di Sicurezza

### Autenticazione
L'autenticazione è il processo di verifica dell'identità di un utente che tenta di accedere al database. È il primo livello di protezione e richiede che ogni utente si identifichi con un nome utente e una password, o con altri metodi più sicuri come l'autenticazione a due fattori (2FA).

### Autorizzazione e Controllo degli Accessi
Una volta autenticato, un utente deve avere solo i permessi necessari per eseguire operazioni specifiche sul database. Il **controllo degli accessi basato sui ruoli (RBAC)** è un approccio comunemente utilizzato, dove gli utenti sono assegnati a ruoli con permessi predefiniti.

> _Approfondimento: La gestione degli utenti e dei permessi sarà trattata più in dettaglio nella lezione successiva_.

### Crittografia
La crittografia viene utilizzata per proteggere i dati sia durante la trasmissione sia durante l'archiviazione. Si possono crittografare:
- **Dati in transito**: durante lo scambio tra il client e il database, utilizzando protocolli sicuri come SSL/TLS.
- **Dati a riposo**: cifrare i dati memorizzati su disco per proteggerli da accessi non autorizzati diretti all’hardware.

### Audit e Log
La registrazione degli eventi attraverso i log di sistema e le funzionalità di audit permette di monitorare le attività degli utenti e individuare eventuali comportamenti sospetti o violazioni di sicurezza. I log possono tracciare l'accesso ai dati, le modifiche effettuate, e qualsiasi tentativo di violazione.

### Backup Sicuro
Oltre a garantire la protezione dei dati contro l’accesso non autorizzato, è essenziale prevedere un meccanismo di **backup sicuro** dei dati. Questo consente di recuperare informazioni in caso di perdita o danneggiamento e dovrebbe includere pratiche come la crittografia dei backup e la loro conservazione in luoghi sicuri.

### Minimizzazione delle Superfici di Attacco
Limitare i vettori di attacco riducendo il numero di punti di ingresso disponibili per utenti malintenzionati. Ad esempio, disattivare funzionalità del database non necessarie e utilizzare solo le porte e i protocolli strettamente necessari per il funzionamento del sistema.

## Protezione dalle Minacce Comuni

### SQL Injection
Una delle vulnerabilità più note nei database è l'**SQL Injection**. Questo attacco si verifica quando un hacker inserisce codice SQL malevolo in un input destinato a una query SQL, potendo potenzialmente accedere, modificare o cancellare dati dal database.

#### Come prevenire l'SQL Injection:
- **Sanificazione degli input**: verificare sempre i dati forniti dagli utenti.
- **Query parametrizzate**: utilizzare query preparate o statement parametrizzati per impedire l'inserimento di codice SQL.
- **ORM**: l'uso di un Object-Relational Mapping (ORM) può ridurre il rischio di attacchi SQL Injection (vedi lezione sull'ORM).

> _Nota: La SQL Injection e altre tecniche di attacco saranno trattate in dettaglio nella lezione “SQL Injection e Sicurezza nelle Query”._

### Gestione degli Utenti e Permessi
Garantire che ogni utente del database abbia accesso solo alle risorse di cui ha realmente bisogno è una delle misure più efficaci per prevenire attacchi interni o errori accidentali. Questo implica un'attenta gestione dei permessi, sia a livello di singolo utente, sia per gruppi di utenti tramite l'assegnazione di ruoli.

### Configurazione e Aggiornamenti di Sicurezza
Mantenere aggiornato il software del database è fondamentale per ridurre le vulnerabilità. Le patch di sicurezza vengono rilasciate regolarmente dai fornitori di database per correggere eventuali falle conosciute. Inoltre, la configurazione corretta del database, come la disabilitazione delle funzionalità non utilizzate, può ridurre il rischio di attacchi.
