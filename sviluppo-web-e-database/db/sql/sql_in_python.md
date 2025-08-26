## Uso di SQL in un Linguaggio di Programmazione <!-- omit in toc -->

- [Connessione al Database](#connessione-al-database)
  - [Esempio di Connessione in Python con `sqlite3`](#esempio-di-connessione-in-python-con-sqlite3)
- [Esecuzione di Query SQL](#esecuzione-di-query-sql)
  - [Query di Selezione in Python con `sqlite3`](#query-di-selezione-in-python-con-sqlite3)
- [Prevenzione delle Iniezioni SQL](#prevenzione-delle-iniezioni-sql)
  - [Query Parametrizzata in Python](#query-parametrizzata-in-python)
- [Gestione delle Transazioni](#gestione-delle-transazioni)
  - [Esempio di Transazione in Python](#esempio-di-transazione-in-python)


L'uso di SQL all'interno di un linguaggio di programmazione è fondamentale per la creazione di applicazioni che interagiscono con database relazionali. SQL (Structured Query Language) è il linguaggio standard per la gestione e la manipolazione dei dati nei database relazionali. In un contesto di programmazione, SQL viene utilizzato per eseguire query, inserire, aggiornare e cancellare dati, nonché per gestire la struttura dei database stessi. In questa lezione vedremo come SQL può essere integrato all'interno di un linguaggio di programmazione e quali sono le pratiche migliori per farlo.

### Connessione al Database

Prima di poter eseguire qualsiasi comando SQL in un'applicazione, è necessario stabilire una connessione tra l'applicazione e il database. Questa connessione può variare leggermente in base al linguaggio di programmazione e al database utilizzato, ma in genere avviene tramite una "stringa di connessione" che specifica il database, il server, l'utente e la password.

#### Esempio di Connessione in Python con `sqlite3`
```python
import sqlite3

conn = sqlite3.connect('miodatabase.db') # Connessione al database SQLite

cursor = conn.cursor() # Creazione di un cursore
```
In questo esempio, utilizziamo la libreria `sqlite3` per connetterci a un database SQLite. Se si trattasse di un database diverso (ad esempio MySQL o PostgreSQL), la connessione potrebbe richiedere una libreria specifica (come `mysql-connector` o `psycopg2`).

### Esecuzione di Query SQL

Una volta stabilita la connessione, possiamo eseguire le query SQL tramite il linguaggio di programmazione scelto. Generalmente, si utilizzano metodi che inviano comandi SQL al database e restituiscono risultati. 

#### Query di Selezione in Python con `sqlite3`
```python

cursor.execute("SELECT * FROM utenti") # Esecuzione di una query di selezione

rows = cursor.fetchall() # Recupero dei risultati

for row in rows: # Iterazione sui risultati
    print(row)
```

In questo esempio, stiamo eseguendo una query di inserimento in una tabella chiamata `utenti`. Notiamo che, in molti linguaggi di programmazione, le query di inserimento, aggiornamento o cancellazione utilizzano metodi diversi dalle query di selezione per ottenere risultati.

### Prevenzione delle Iniezioni SQL

L'inserimento di stringhe direttamente in query SQL può essere rischioso e aprire l'applicazione a vulnerabilità come la SQL Injection. Per evitare questo rischio, è consigliabile usare query parametrizzate o statement preparati.

#### Query Parametrizzata in Python
```python
cursor.execute("INSERT INTO utenti (nome, cognome) VALUES (?, ?)", ('Mario', 'Rossi')) # Usare parametri per prevenire l'SQL Injection
```

Le query parametrizzate non solo migliorano la sicurezza, ma anche le prestazioni, poiché i database possono ottimizzare l'esecuzione di query ripetitive.

> **Nota**: Le SQL injection verranno approfondite in una lezione successiva.

### Gestione delle Transazioni

Le transazioni consentono di eseguire una serie di operazioni SQL come un'unica unità atomica. Se una parte della transazione fallisce, l'intera operazione può essere annullata. Molti linguaggi di programmazione supportano le transazioni attraverso l'uso di metodi come `commit()` e `rollback()`.

#### Esempio di Transazione in Python
```python
try:
    
    conn.begin() # Inizio transazione
    
    cursor.execute("INSERT INTO utenti (nome, cognome) VALUES ('Luigi', 'Verdi')") # Esecuzione delle query
    cursor.execute("UPDATE utenti SET cognome = 'Bianchi' WHERE nome = 'Mario'") # Esecuzione delle query

    conn.commit() # Conferma della transazione
except Exception as e:
    conn.rollback() # In caso di errore, annulla la transazione
    print(f"Errore: {e}")
```
