## SQL: Il Linguaggio per i Database Relazionali <!-- omit in toc -->

- [Sottolinguaggi di SQL](#sottolinguaggi-di-sql)
  - [Data Definition Language (DDL)](#data-definition-language-ddl)
  - [Data Manipulation Language (DML)](#data-manipulation-language-dml)
- [La Query di Selezione: `SELECT`](#la-query-di-selezione-select)
- [Filtrare i Dati: `WHERE`](#filtrare-i-dati-where)
- [Ordinare i Dati: `ORDER BY`](#ordinare-i-dati-order-by)
- [Raggruppare i Dati: `GROUP BY`](#raggruppare-i-dati-group-by)
- [Combinare le Tabelle: `JOIN`](#combinare-le-tabelle-join)

**SQL (Structured Query Language)** è il linguaggio standard utilizzato per comunicare con i database relazionali. Permette di definire la struttura dei dati, manipolarli e interrogarli. SQL è un linguaggio **dichiarativo**: dici _cosa_ vuoi ottenere, non _come_ ottenerlo.

### Sottolinguaggi di SQL

SQL è comunemente suddiviso in due categorie principali:

#### Data Definition Language (DDL)

Il DDL si usa per definire e gestire la struttura del database e delle sue tabelle.

- **`CREATE TABLE`**: Crea una nuova tabella.
  ```sql
  CREATE TABLE Studenti (
      Matricola INT PRIMARY KEY,
      Nome VARCHAR(50) NOT NULL,
      Cognome VARCHAR(50) NOT NULL,
      DataNascita DATE,
      ID_Corso INT,
      FOREIGN KEY (ID_Corso) REFERENCES Corsi(ID_Corso)
  );
  ```
- **`ALTER TABLE`**: Modifica la struttura di una tabella esistente (es. aggiunge una colonna).
- **`DROP TABLE`**: Elimina una tabella.

#### Data Manipulation Language (DML)

Il DML si usa per inserire, modificare, eliminare e interrogare i dati all'interno delle tabelle.

- **`INSERT INTO`**: Aggiunge nuove righe a una tabella.
  ```sql
  INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (101, 'Mario', 'Rossi');
  ```
- **`UPDATE`**: Modifica righe esistenti.
  ```sql
  UPDATE Studenti SET Cognome = 'Verdi' WHERE Matricola = 101;
  ```
- **`DELETE FROM`**: Rimuove righe da una tabella.
  ```sql
  DELETE FROM Studenti WHERE Matricola = 101;
  ```
- **`SELECT`**: Estrae dati da una o più tabelle.

### La Query di Selezione: `SELECT`

È il comando più usato. La sua struttura base è:

```sql
SELECT colonna1, colonna2, ...
FROM nome_tabella;
```

- `SELECT *` seleziona tutte le colonne.

### Filtrare i Dati: `WHERE`

La clausola `WHERE` permette di filtrare le righe in base a una condizione.

```sql
SELECT Nome, Cognome FROM Studenti WHERE Matricola > 100;
```

Si possono usare operatori logici (`AND`, `OR`, `NOT`) e di confronto (`=`, `>`, `<`, `>=`, `<=`, `!=`).

### Ordinare i Dati: `ORDER BY`

La clausola `ORDER BY` ordina i risultati in base a una o più colonne.

- `ASC` per l'ordine ascendente (default).
- `DESC` per l'ordine discendente.

```sql
SELECT * FROM Studenti ORDER BY Cognome ASC, Nome ASC;
```

### Raggruppare i Dati: `GROUP BY`

La clausola `GROUP BY` raggruppa le righe che hanno gli stessi valori in colonne specificate, in modo da poter eseguire funzioni aggregate su di esse.

- **`COUNT()`**: conta il numero di righe.
- **`SUM()`**: somma i valori.
- **`AVG()`**: calcola la media.
- **`MAX()`**, **`MIN()`**: trovano il massimo e il minimo.

```sql
SELECT ID_Corso, COUNT(*) AS NumeroStudenti
FROM Iscrizioni
GROUP BY ID_Corso;
```

Questa query conta quanti studenti sono iscritti a ciascun corso. La clausola `HAVING` può essere usata per filtrare i gruppi.

### Combinare le Tabelle: `JOIN`

Il `JOIN` è l'operazione più potente del modello relazionale. Permette di combinare righe da due o più tabelle basandosi su una colonna in comune.

```sql
SELECT Studenti.Nome, Studenti.Cognome, Corsi.Nome_Corso
FROM Studenti
INNER JOIN Corsi ON Studenti.ID_Corso = Corsi.ID_Corso;
```

Questa query combina le informazioni delle tabelle `Studenti` e `Corsi` per mostrare il nome del corso a cui ogni studente è iscritto.
