## Gestione degli Utenti e Permessi <!-- omit in toc -->

- [Concetti di Base](#concetti-di-base)
  - [Utenti e Ruoli](#utenti-e-ruoli)
  - [Permessi](#permessi)
- [Assegnazione dei Permessi](#assegnazione-dei-permessi)
  - [GRANT: Concessione di Permessi](#grant-concessione-di-permessi)
  - [REVOKE: Revoca di Permessi](#revoke-revoca-di-permessi)
  - [Ruoli Dinamici](#ruoli-dinamici)
- [Principi di Sicurezza](#principi-di-sicurezza)
  - [Privilegi Minimi](#privilegi-minimi)
  - [Controllo degli Accessi Basato sui Ruoli (RBAC)](#controllo-degli-accessi-basato-sui-ruoli-rbac)
  - [Monitoraggio e Audit](#monitoraggio-e-audit)
- [Esempi Pratici](#esempi-pratici)
  - [Creazione di un Utente con Permessi Limitati](#creazione-di-un-utente-con-permessi-limitati)
  - [Creazione di un Ruolo e Assegnazione di Permessi](#creazione-di-un-ruolo-e-assegnazione-di-permessi)

La gestione degli utenti e dei permessi all'interno di un database è un aspetto fondamentale per garantire la sicurezza e la corretta organizzazione delle risorse. Un sistema di gestione robusto permette di limitare l'accesso alle informazioni solo agli utenti autorizzati, prevenendo così accessi non desiderati e potenziali violazioni della sicurezza. In questa lezione esploreremo come gestire utenti, ruoli e permessi nei database relazionali, approfondendo i concetti e le pratiche che rendono sicuro l'accesso ai dati.

### Concetti di Base

#### Utenti e Ruoli
Un utente in un database è una persona o un'entità che ha accesso a uno o più schemi di database. Ogni utente ha un identificatore unico (tipicamente un nome utente) e può essere associato a determinati **ruoli**. Un ruolo è un insieme predefinito di permessi, che consente una gestione più semplice degli accessi a risorse del database.

I ruoli permettono di gestire gli accessi in modo scalabile. Invece di assegnare permessi specifici a ogni singolo utente, è possibile raggruppare gli utenti in ruoli e assegnare i permessi a questi ultimi. Alcuni ruoli comuni in un database includono:
- **DBA (Database Administrator)**: ha accesso completo e può eseguire qualsiasi operazione.
- **Sviluppatore**: ha accesso per creare e modificare strutture del database, ma non necessariamente ai dati di produzione.
- **Utente finale**: può visualizzare e modificare solo i dati necessari per il proprio lavoro, con restrizioni sui tipi di operazioni eseguibili.

#### Permessi
I **permessi** definiscono cosa un utente o un ruolo può fare all'interno di un database. I permessi possono essere concessi a livello di database, tabella, riga o colonna. Esempi di permessi comuni includono:
- **SELECT**: consente di leggere i dati.
- **INSERT**: consente di aggiungere nuovi dati.
- **UPDATE**: permette di modificare dati esistenti.
- **DELETE**: consente di cancellare dati.
- **GRANT**: consente di assegnare permessi ad altri utenti.

### Assegnazione dei Permessi

#### GRANT: Concessione di Permessi
Il comando SQL **GRANT** viene utilizzato per assegnare permessi specifici a un utente o un ruolo. Il formato di base del comando è il seguente:

```sql
GRANT <permesso> ON <oggetto> TO <utente_o_ruolo>;
```

Esempio:
```sql
GRANT SELECT, INSERT ON tabella_clienti TO sviluppatore;
```
In questo esempio, il ruolo "sviluppatore" ottiene i permessi di lettura (SELECT) e inserimento (INSERT) sulla tabella "tabella_clienti".

#### REVOKE: Revoca di Permessi
Il comando **REVOKE** viene utilizzato per rimuovere permessi precedentemente concessi. Il formato del comando è il seguente:

```sql
REVOKE <permesso> ON <oggetto> FROM <utente_o_ruolo>;
```

Esempio:
```sql
REVOKE UPDATE ON tabella_clienti FROM utente_finale;
```
Questo comando revoca all'utente "utente_finale" il permesso di aggiornare i dati nella tabella "tabella_clienti".

#### Ruoli Dinamici
Molti sistemi di gestione di database supportano la creazione e gestione di **ruoli dinamici**, che possono essere utilizzati per assegnare in modo efficiente permessi comuni a più utenti. Un ruolo dinamico può essere creato con il comando **CREATE ROLE**:

```sql
CREATE ROLE sviluppatore;
```

Successivamente, i permessi possono essere concessi al ruolo e il ruolo può essere assegnato agli utenti:

```sql
GRANT SELECT, INSERT ON tabella_clienti TO sviluppatore;
GRANT sviluppatore TO utente1, utente2;
```

In questo modo, se si modifica il ruolo "sviluppatore", tutti gli utenti associati riceveranno immediatamente i nuovi permessi.

### Principi di Sicurezza

#### Privilegi Minimi
Un concetto chiave nella gestione degli utenti e dei permessi è quello dei **privilegi minimi**. Questo principio stabilisce che ogni utente dovrebbe avere solo i permessi necessari per eseguire le attività richieste dal proprio ruolo. Limitare i permessi riduce il rischio di errori e di accessi non autorizzati ai dati sensibili.

Ad esempio, un utente che ha bisogno solo di leggere i dati non dovrebbe avere permessi di scrittura (INSERT, UPDATE, DELETE), perché questi ultimi potrebbero essere usati in modo improprio o involontario.

#### Controllo degli Accessi Basato sui Ruoli (RBAC)
Il **controllo degli accessi basato sui ruoli (RBAC)** è un modello di sicurezza che assegna i permessi in base ai ruoli, piuttosto che direttamente agli utenti. Questo approccio facilita la gestione dei permessi in sistemi di grandi dimensioni, rendendo più semplice modificare i permessi di un gruppo di utenti allo stesso tempo. È particolarmente utile in ambienti aziendali dove vi sono molti utenti che svolgono ruoli simili.

#### Monitoraggio e Audit
Oltre a definire ruoli e permessi, è importante monitorare l'accesso al database e creare log di audit per tracciare chi ha eseguito determinate operazioni. Gli audit aiutano a:
- Identificare potenziali violazioni della sicurezza.
- Tenere traccia delle modifiche ai dati critici.
- Garantire la conformità a normative e politiche di sicurezza.

### Esempi Pratici

#### Creazione di un Utente con Permessi Limitati
Supponiamo di voler creare un nuovo utente chiamato "analista" che ha accesso solo in lettura alla tabella "tabella_analisi". Ecco i passaggi per farlo:

1. Creazione dell'utente:
   ```sql
   CREATE USER analista IDENTIFIED BY 'password_sicura';
   ```

2. Assegnazione dei permessi:
   ```sql
   GRANT SELECT ON tabella_analisi TO analista;
   ```

In questo modo, l'utente "analista" può accedere alla tabella "tabella_analisi", ma non può modificarne i dati.

#### Creazione di un Ruolo e Assegnazione di Permessi
Se dovessimo gestire un gruppo di utenti che lavorano su più tabelle, potremmo creare un ruolo che assegna loro i permessi adeguati:

1. Creazione del ruolo:
   ```sql
   CREATE ROLE data_scientist;
   ```

2. Assegnazione di permessi al ruolo:
   ```sql
   GRANT SELECT, INSERT ON tabella_clienti TO data_scientist;
   ```

3. Assegnazione del ruolo agli utenti:
   ```sql
   GRANT data_scientist TO utente3, utente4;
   ```

Ora, gli utenti "utente3" e "utente4" avranno i permessi associati al ruolo "data_scientist".
