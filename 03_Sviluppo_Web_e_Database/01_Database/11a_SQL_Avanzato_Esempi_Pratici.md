# SQL Avanzato: Esempi Pratici con JOIN e GROUP BY

Scrivere query di base è semplice, ma la vera potenza di SQL risiede nella sua capacità di combinare e aggregare dati da più tabelle per rispondere a domande complesse. In questa lezione, vedremo esempi pratici delle clausole più importanti: `JOIN` e `GROUP BY`.

### Lo Scenario: Il Nostro Database Universitario

Useremo un piccolo database composto da tre tabelle per tutti i nostri esempi.

**Tabella `Studenti`**
| id | nome |
| :-- | :-- |
| 1 | Marco |
| 2 | Laura |
| 3 | Simone|
| 4 | Elena |

**Tabella `Corsi`**
| id | nome_corso |
| :-- | :-- |
| 10 | Matematica |
| 20 | Fisica |
| 30 | Chimica |

**Tabella `Iscrizioni` (Tabella di Raccordo)**
| studente_id | corso_id |
| :-- | :-- |
| 1 | 10 |
| 1 | 20 |
| 2 | 10 |
| 3 | 20 |

---

### 1. JOIN: Combinare solo i dati corrispondenti

`JOIN` restituisce solo le righe in cui c'è una corrispondenza in **entrambe** le tabelle collegate.

**Domanda:** "Mostrami il nome di ogni studente e il nome del corso a cui è iscritto."

```sql
SELECT
    Studenti.nome,
    Corsi.nome_corso
FROM
    Studenti
JOIN Iscrizioni ON Studenti.id = Iscrizioni.studente_id
JOIN Corsi ON Iscrizioni.corso_id = Corsi.id;
```

**Risultato:**

| nome | nome_corso |
| :-- | :-- |
| Marco | Matematica |
| Marco | Fisica |
| Laura | Matematica |
| Simone| Fisica |

*   **Spiegazione:** La query abbina `Studenti` con `Iscrizioni` e poi con `Corsi`. Nota che **Elena non compare**, perché il suo ID non è presente nella tabella `Iscrizioni`.

---

### 2. LEFT JOIN: Includere tutti i dati dalla tabella di sinistra

`LEFT JOIN` restituisce **tutte** le righe della tabella di sinistra (la prima menzionata) e le righe corrispondenti della tabella di destra. Se non c'è corrispondenza, le colonne della tabella di destra avranno valore `NULL`.

**Domanda:** "Mostrami TUTTI gli studenti e, se sono iscritti a un corso, mostra il nome del corso. Voglio vedere anche gli studenti che non frequentano nessun corso."

```sql
SELECT
    Studenti.nome,
    Corsi.nome_corso
FROM
    Studenti
LEFT JOIN Iscrizioni ON Studenti.id = Iscrizioni.studente_id
LEFT JOIN Corsi ON Iscrizioni.corso_id = Corsi.id;
```

**Risultato:**

| nome | nome_corso |
| :-- | :-- |
| Marco | Matematica |
| Marco | Fisica |
| Laura | Matematica |
| Simone| Fisica |
| **Elena** | **NULL** |

*   **Spiegazione:** Ora Elena compare nel risultato. Poiché non è stata trovata una corrispondenza per lei nella tabella `Iscrizioni`, il valore per `nome_corso` è `NULL`. Questo è utilissimo per trovare "elementi orfani".

---

### 3. GROUP BY con HAVING: Raggruppare e Filtrare i Gruppi

`GROUP BY` raggruppa le righe che hanno gli stessi valori in colonne specificate, per poter eseguire funzioni di aggregazione (`COUNT`, `SUM`, etc.) su ogni gruppo.

**Domanda:** "Calcola il numero di studenti iscritti a ciascun corso. Mostra solo i corsi che hanno 2 o più studenti iscritti."

```sql
SELECT
    Corsi.nome_corso,
    COUNT(Iscrizioni.studente_id) AS numero_iscritti
FROM
    Corsi
JOIN Iscrizioni ON Corsi.id = Iscrizioni.corso_id
GROUP BY
    Corsi.nome_corso
HAVING
    numero_iscritti >= 2;
```

**Risultato:**

| nome_corso | numero_iscritti |
| :-- | :-- |
| Matematica | 2 |
| Fisica | 2 |

*   **Spiegazione del processo:**
    1.  `JOIN` combina i dati.
    2.  `GROUP BY Corsi.nome_corso` crea i gruppi: uno per "Matematica", uno per "Fisica" e uno per "Chimica".
    3.  `COUNT(...)` conta gli studenti in ogni gruppo (2 per Matematica, 2 per Fisica, 0 per Chimica).
    4.  `HAVING numero_iscritti >= 2` filtra via il gruppo "Chimica" perché non soddisfa la condizione.

**Ricorda la differenza fondamentale:**
*   `WHERE` filtra le righe **prima** che vengano raggruppate.
*   `HAVING` filtra i gruppi **dopo** che sono stati creati.