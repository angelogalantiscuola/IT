## Uso di SQL in un Linguaggio di Programmazione <!-- omit in toc -->

- [Il Flusso di Lavoro Standard](#il-flusso-di-lavoro-standard)
- [Esempio 1: SQLite (Database basato su file)](#esempio-1-sqlite-database-basato-su-file)
- [Esempio 2: MariaDB/MySQL (Database client-server)](#esempio-2-mariadbmysql-database-client-server)
- [Sicurezza: Prevenire la SQL Injection con Query Parametrizzate](#sicurezza-prevenire-la-sql-injection-con-query-parametrizzate)

Per creare applicazioni dinamiche, non basta saper scrivere SQL: bisogna eseguirlo tramite un linguaggio di programmazione come Python. L'interazione tra l'applicazione e il database segue un flusso di lavoro ben definito.

### Il Flusso di Lavoro Standard

Indipendentemente dal linguaggio o dal database, i passaggi sono quasi sempre gli stessi:

1.  **Importare la libreria** del driver del database.
2.  **Stabilire una connessione** al database.
3.  **Creare un "cursore"**, un oggetto per eseguire comandi.
4.  **Eseguire la query SQL** tramite il cursore.
5.  **Recuperare i risultati** (`fetch`) o **confermare le modifiche** (`commit`).
6.  **Chiudere la connessione** per rilasciare le risorse.

### Esempio 1: SQLite (Database basato su file)

SQLite è il modo più semplice per iniziare perché è incluso in Python e non richiede un server. Il database è un singolo file.

```python
import sqlite3

# 2. Connessione: crea il file 'scuola.db' se non esiste
conn = sqlite3.connect('scuola.db')
# 3. Creazione Cursore
cursor = conn.cursor()

try:
    # Eseguo DDL per creare la tabella se non esiste
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Studenti (
            Matricola INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Cognome TEXT NOT NULL
        )
    """)

    # 4. Esecuzione Query DML (parametrizzata)
    # Il segnaposto per SQLite è '?'
    cursor.execute(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        (101, 'Mario', 'Rossi')
    )

    # 5. Conferma delle modifiche
    conn.commit()

    # Eseguo una SELECT
    cursor.execute("SELECT Nome, Cognome FROM Studenti WHERE Matricola = ?", (101,))
    studente = cursor.fetchone() # I risultati sono tuple
    if studente:
        print(f"Studente trovato (SQLite): {studente} {studente}")

finally:
    # 6. Chiusura Connessione
    conn.close()
```

### Esempio 2: MariaDB/MySQL (Database client-server)

Questo approccio è usato per applicazioni più complesse che richiedono un server di database dedicato.

```python
import mysql.connector

# 2. Connessione
db_connection = mysql.connector.connect(
    host="localhost",
    user="tuo_utente",
    password="tua_password",
    database="scuola"
)

# 3. Creazione Cursore
cursor = db_connection.cursor(dictionary=True) # dictionary=True restituisce righe come dizionari

try:
    # 4. Esecuzione Query (parametrizzata)
    # Il segnaposto per mysql-connector è '%s'
    query = "SELECT Nome, Cognome FROM Studenti WHERE Matricola = %s"

    # 5. Recupero Risultati
    cursor.execute(query, (101,))
    studente = cursor.fetchone()
    if studente:
        print(f"Studente trovato (MariaDB): {studente['Nome']} {studente['Cognome']}")

finally:
    # 6. Chiusura Connessione
    cursor.close()
    db_connection.close()
```

### Sicurezza: Prevenire la SQL Injection con Query Parametrizzate

Un errore gravissimo è costruire query concatenando stringhe con l'input dell'utente. La soluzione è usare le **query parametrizzate**, dove la query e i dati vengono inviati separatamente al database.

**Ogni libreria ha il suo segnaposto:**

- **SQLite (`sqlite3`)**: Usa il punto di domanda (`?`).

  ```python
  matricola = 101
  cursor.execute("SELECT * FROM Studenti WHERE Matricola = ?", (matricola,))
  ```

- **MariaDB/MySQL (`mysql.connector`)**: Usa `%s`.
  ```python
  matricola = 101
  cursor.execute("SELECT * FROM Studenti WHERE Matricola = %s", (matricola,))
  ```

**Regola d'oro**: Mai, mai inserire l'input dell'utente direttamente in una stringa SQL. Usa sempre i parametri forniti dalla tua libreria.
