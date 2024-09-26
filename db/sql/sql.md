## SQL: Linguaggio per DB Relazionali <!-- omit in toc -->

- [Caratteristiche Principali di SQL](#caratteristiche-principali-di-sql)
  - [Operazioni Principali](#operazioni-principali)
  - [Linguaggio di Definizione Dati (DDL)](#linguaggio-di-definizione-dati-ddl)
  - [Linguaggio di Manipolazione Dati (DML)](#linguaggio-di-manipolazione-dati-dml)
  - [Linguaggio di Controllo Dati (DCL)](#linguaggio-di-controllo-dati-dcl)
- [Query di Selezione: Il Cuore di SQL](#query-di-selezione-il-cuore-di-sql)
  - [Ordinamento e Raggruppamento](#ordinamento-e-raggruppamento)
- [Funzioni Aggregate](#funzioni-aggregate)
- [SQL Tutorial Completo](#sql-tutorial-completo)

Il **Structured Query Language (SQL)** è il linguaggio standard utilizzato per la gestione e la manipolazione di dati all'interno di database relazionali. Introdotto per la prima volta negli anni '70, SQL è diventato il linguaggio di riferimento per creare, modificare, interrogare e gestire i dati nei database relazionali. Il suo successo deriva dalla semplicità e dalla potenza espressiva che consente di definire complessi modelli di dati e operazioni senza dover entrare nei dettagli dell'implementazione interna.

### Caratteristiche Principali di SQL

SQL è un linguaggio **dichiarativo**, il che significa che consente di descrivere cosa ottenere, piuttosto che come ottenerlo. Questa caratteristica lo rende accessibile e intuitivo per molti utenti, pur essendo altamente efficiente e flessibile. SQL è anche un linguaggio **standardizzato**, con implementazioni che variano leggermente tra i diversi sistemi di gestione di database relazionali (DBMS) come MySQL, PostgreSQL, SQL Server, e Oracle.

#### Operazioni Principali

SQL è diviso in vari sottolinguaggi, ognuno con uno scopo specifico per la gestione dei dati e delle strutture del database.

#### Linguaggio di Definizione Dati (DDL)
Il **Data Definition Language (DDL)** è utilizzato per definire e modificare la struttura del database. Le operazioni principali includono la creazione, la modifica e l'eliminazione di tabelle e altri oggetti del database.

- **`CREATE DATABASE`**: Crea un nuovo database.
- **`CREATE`**: Crea una nuova tabella, vista, indice o altro oggetto del database.
- **`ALTER`**: Modifica la struttura di una tabella esistente.
- **`DROP`**: Elimina una tabella o un altro oggetto dal database.

Esempio:
```sql
CREATE DATABASE Scuola;

CREATE TABLE Studenti (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Cognome VARCHAR(100),
    DataNascita DATE
);
```
In questo esempio viene creata una tabella **Studenti** con tre campi (ID, Nome, Cognome, DataNascita) e una chiave primaria su `ID`.

#### Linguaggio di Manipolazione Dati (DML)
Il **Data Manipulation Language (DML)** è utilizzato per operare sui dati presenti nelle tabelle. Include comandi per inserire, aggiornare, eliminare e interrogare i dati.

- **`INSERT`**: Aggiunge nuovi dati a una tabella.
- **`UPDATE`**: Modifica dati esistenti in una tabella.
- **`DELETE`**: Elimina dati da una tabella.
- **`SELECT`**: Recupera dati da una o più tabelle.

Esempio:
```sql
INSERT INTO Studenti (ID, Nome, Cognome, DataNascita) 
VALUES (1, 'Luca', 'Rossi', '2002-05-10');
```
In questo esempio viene inserito un nuovo record nella tabella **Studenti**.

#### Linguaggio di Controllo Dati (DCL)
Il **Data Control Language (DCL)** gestisce i permessi e il controllo di accesso ai dati.

- **`GRANT`**: Concede privilegi a un utente su oggetti del database.
- **`REVOKE`**: Revoca i privilegi precedentemente concessi.

Esempio:
```sql
GRANT SELECT ON Studenti TO 'utente1';
```
Questo comando concede all'utente `utente1` il permesso di eseguire query **SELECT** sulla tabella **Studenti**.

### Query di Selezione: Il Cuore di SQL

Il comando **`SELECT`** è probabilmente il più utilizzato in SQL, essendo il fulcro per il recupero dei dati dai database. La sintassi di base di una query di selezione è la seguente:

```sql
SELECT [colonne]
FROM [tabelle]
WHERE [condizioni];
```

- **`SELECT`**: Specifica le colonne da includere nei risultati.
- **`FROM`**: Specifica la tabella da cui recuperare i dati.
- **`WHERE`**: Filtra i dati in base a una condizione.

Esempio:
```sql
SELECT Nome, Cognome
FROM Studenti
WHERE DataNascita > '2000-01-01';
```
Questa query recupera i nomi e i cognomi di tutti gli studenti nati dopo il 1° gennaio 2000.

#### Ordinamento e Raggruppamento

È possibile ordinare e raggruppare i dati utilizzando i comandi **`ORDER BY`** e **`GROUP BY`**.

- **`ORDER BY`**: Ordina i risultati in base a una o più colonne.
- **`GROUP BY`**: Raggruppa i risultati in base a una o più colonne, solitamente in combinazione con funzioni aggregate come **`COUNT`**, **`SUM`**, **`AVG`**, etc.

Esempio:
```sql
SELECT Cognome, COUNT(*)
FROM Studenti
GROUP BY Cognome
ORDER BY COUNT(*) DESC;
```
Questa query raggruppa gli studenti per cognome, contando quanti studenti hanno lo stesso cognome, e ordina il risultato in ordine decrescente.

### Funzioni Aggregate

SQL fornisce una serie di funzioni aggregate che consentono di eseguire operazioni sui dati recuperati. Alcuni esempi sono:

- **`COUNT()`**: Conta il numero di record.
- **`SUM()`**: Somma i valori di una colonna.
- **`AVG()`**: Calcola la media dei valori.
- **`MIN()`**: Restituisce il valore minimo.
- **`MAX()`**: Restituisce il valore massimo.

Esempio:
```sql
SELECT AVG(DataNascita)
FROM Studenti;
```
Questa query calcola la media delle date di nascita degli studenti.

### SQL Tutorial Completo

Per ulteriori informazioni su SQL, puoi consultare il seguente link: [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)