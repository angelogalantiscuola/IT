# Esercizi di Base su SQL

## Esercizio 1: Creazione di Tabelle e Inserimento Dati
**Livello: Principiante**

Scenario: Crea un database per una piccola libreria.

Compito:
1. Scrivi i comandi SQL per creare le seguenti tabelle:
   - Libri (ID, Titolo, Autore, AnnoPubblicazione)
   - Clienti (ID, Nome, Cognome, Email)
2. Inserisci almeno 3 record in ciascuna tabella.

Esempio di soluzione:
```sql
CREATE TABLE Libri (
    ID INT PRIMARY KEY,
    Titolo VARCHAR(100),
    Autore VARCHAR(50),
    AnnoPubblicazione INT
);

INSERT INTO Libri (ID, Titolo, Autore, AnnoPubblicazione)
VALUES (1, '1984', 'George Orwell', 1949);

-- Aggiungi altri comandi CREATE e INSERT per completare l'esercizio
```

## Esercizio 2: Query di Selezione di Base
**Livello: Principiante**

Utilizzando le tabelle create nell'Esercizio 1, scrivi query SQL per:

1. Selezionare tutti i libri.
2. Selezionare solo il titolo e l'autore dei libri pubblicati dopo il 2000.
3. Selezionare tutti i clienti il cui cognome inizia con 'S'.

Esempio di soluzione:
```sql
-- Query 1
SELECT * FROM Libri;

-- Completa le altre query
```

## Esercizio 3: Join di Base
**Livello: Intermedio**

Scenario: Aggiungi una tabella Prestiti al database della libreria.

Compito:
1. Crea una tabella Prestiti (ID, LibroID, ClienteID, DataPrestito, DataRestituzione).
2. Inserisci alcuni record di prestiti.
3. Scrivi una query per ottenere un elenco di tutti i prestiti con i dettagli del libro e del cliente.

Esempio di soluzione:
```sql
CREATE TABLE Prestiti (
    ID INT PRIMARY KEY,
    LibroID INT,
    ClienteID INT,
    DataPrestito DATE,
    DataRestituzione DATE
);

-- Aggiungi INSERT INTO Prestiti ...

SELECT P.ID, L.Titolo, C.Nome, C.Cognome, P.DataPrestito
FROM Prestiti P
JOIN Libri L ON P.LibroID = L.ID
JOIN Clienti C ON P.ClienteID = C.ID;
```

## Esercizio 4: Aggregazioni e Raggruppamenti
**Livello: Avanzato**

Utilizzando le tabelle create negli esercizi precedenti, scrivi query SQL per:

1. Trovare il numero totale di libri per ogni autore.
2. Identificare il cliente che ha preso in prestito il maggior numero di libri.
3. Calcolare la durata media dei prestiti (in giorni) per ogni libro.

Esempio di soluzione:
```sql
-- Query 1
SELECT Autore, COUNT(*) AS NumeroDiLibri
FROM Libri
GROUP BY Autore;

-- Completa le altre query
```

## Esercizio 5: Subquery e Query Avanzate
**Livello: Esperto**

Compito:
1. Trova tutti i libri che non sono mai stati presi in prestito.
2. Identifica i clienti che hanno preso in prestito tutti i libri di un determinato autore.
3. Crea una vista che mostri per ogni cliente il numero di libri attualmente in prestito.

Esempio di soluzione:
```sql
-- Query 1
SELECT *
FROM Libri
WHERE ID NOT IN (SELECT DISTINCT LibroID FROM Prestiti);

-- Completa le altre query
```