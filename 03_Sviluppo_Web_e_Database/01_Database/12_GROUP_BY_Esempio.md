## Spiegazione di GROUP BY in SQL con Esempio Passo Passo

La clausola `GROUP BY` in SQL è utilizzata per raggruppare le righe che hanno gli stessi valori in colonne specificate, permettendo di eseguire funzioni aggregate su ciascun gruppo. Questo è essenziale per calcolare statistiche riassuntive, come conteggi, somme, medie, ecc.

### Funzioni Aggregate Comuni
- **`COUNT()`**: Conta il numero di righe in ciascun gruppo.
- **`SUM()`**: Somma i valori di una colonna numerica in ciascun gruppo.
- **`AVG()`**: Calcola la media dei valori in ciascun gruppo.
- **`MAX()`**, **`MIN()`**: Trova il valore massimo o minimo in ciascun gruppo.

### Esempio Passo Passo

Utilizzeremo una tabella di esempio chiamata `Vendite` con le seguenti colonne: `ID_Vendita`, `Prodotto`, `Quantita`, `Prezzo`.

#### Dati di Esempio nella Tabella `Vendite`

| ID_Vendita | Prodotto  | Quantita | Prezzo |
|------------|-----------|----------|--------|
| 1          | Mela      | 10       | 2.00   |
| 2          | Banana    | 5        | 1.50   |
| 3          | Mela      | 8        | 2.00   |
| 4          | Arancia   | 12       | 3.00   |
| 5          | Banana    | 7        | 1.50   |
| 6          | Mela      | 6        | 2.00   |

#### Passo 1: Query Senza GROUP BY
Per vedere tutti i prodotti e le quantità senza raggruppamento:

```sql
SELECT Prodotto, Quantita FROM Vendite;
```

**Risultato:**
| Prodotto | Quantita |
|----------|----------|
| Mela     | 10       |
| Banana   | 5        |
| Mela     | 8        |
| Arancia  | 12       |
| Banana   | 7        |
| Mela     | 6        |

Questa query mostra ogni singola vendita individualmente.

#### Passo 2: Raggruppare per Prodotto e Contare le Vendite
Per contare quante vendite ci sono per ciascun prodotto:

```sql
SELECT Prodotto, COUNT(*) AS NumeroVendite
FROM Vendite
GROUP BY Prodotto;
```

Quando SQL esegue `GROUP BY Prodotto`, divide la tabella in gruppi basati sui valori unici della colonna `Prodotto`. Ecco come vengono creati i gruppi:

**Gruppo 1: Prodotto = 'Mela'** (3 righe)
| ID_Vendita | Prodotto | Quantita | Prezzo |
|------------|----------|----------|--------|
| 1          | Mela     | 10       | 2.00   |
| 3          | Mela     | 8        | 2.00   |
| 6          | Mela     | 6        | 2.00   |

**Gruppo 2: Prodotto = 'Banana'** (2 righe)
| ID_Vendita | Prodotto | Quantita | Prezzo |
|------------|----------|----------|--------|
| 2          | Banana   | 5        | 1.50   |
| 5          | Banana   | 7        | 1.50   |

**Gruppo 3: Prodotto = 'Arancia'** (1 riga)
| ID_Vendita | Prodotto | Quantita | Prezzo |
|------------|----------|----------|--------|
| 4          | Arancia  | 12       | 3.00   |

- `GROUP BY Prodotto` raggruppa le righe per prodotto (Mela, Banana, Arancia).
- `COUNT(*)` conta il numero di righe in ciascun gruppo.

**Risultato:**
| Prodotto | NumeroVendite |
|----------|---------------|
| Mela     | 3             |
| Banana   | 2             |
| Arancia  | 1             |

#### Passo 3: Sommare le Quantità per Gruppo
Per calcolare la quantità totale venduta per ciascun prodotto:

```sql
SELECT Prodotto, SUM(Quantita) AS QuantitaTotale
FROM Vendite
GROUP BY Prodotto;
```

**Risultato:**
| Prodotto | QuantitaTotale |
|----------|----------------|
| Mela     | 24             |
| Banana   | 12             |
| Arancia  | 12             |

#### Passo 4: Calcolare il Ricavo Totale
Per calcolare il ricavo totale (Quantita * Prezzo) per ciascun prodotto:

```sql
SELECT Prodotto, SUM(Quantita * Prezzo) AS RicavoTotale
FROM Vendite
GROUP BY Prodotto;
```

**Risultato:**
| Prodotto | RicavoTotale |
|----------|--------------|
| Mela     | 48.00        |
| Banana   | 18.00        |
| Arancia  | 36.00        |

#### Passo 5: Filtrare i Gruppi con HAVING
La clausola `HAVING` filtra i gruppi dopo il raggruppamento (a differenza di `WHERE` che filtra le righe prima del raggruppamento).

Per mostrare solo i prodotti con più di 2 vendite:

```sql
SELECT Prodotto, COUNT(*) AS NumeroVendite
FROM Vendite
GROUP BY Prodotto
HAVING COUNT(*) > 2;
```

**Risultato:**
| Prodotto | NumeroVendite |
|----------|---------------|
| Mela     | 3             |

### Note Importanti
- Le colonne nella `SELECT` che non sono aggregate devono essere incluse nella `GROUP BY`.
- `WHERE` filtra le righe prima del raggruppamento; `HAVING` filtra i gruppi dopo.
- `GROUP BY` è spesso usato con funzioni aggregate per ottenere insights sui dati.