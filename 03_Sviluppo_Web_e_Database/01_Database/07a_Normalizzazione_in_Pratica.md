# Normalizzazione in Pratica: Da un Foglio Excel a un Database Pulito

La normalizzazione può sembrare un concetto teorico e astratto. Vediamo come applicarla in uno scenario pratico per trasformare una singola tabella disordinata (come un foglio di calcolo) in un database relazionale ben strutturato, eliminando le anomalie dei dati.

### Lo Scenario: La Tabella "Incubo"

Immagina di dover gestire i dati delle vendite di un negozio usando questa singola tabella.

**Tabella Iniziale: `REGISTRO_VENDITE`**

| ID_Ordine | Data | ID_Cliente | Nome_Cliente | Indirizzo_Cliente | Prodotti_Ordinati (ID:Nome:Qtà) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 101 | 2025-11-15 | C01 | Mario Rossi | Via Roma 1, Milano | A1:Mouse:1, B2:Tastiera:1 |
| 102 | 2025-11-16 | C02 | Anna Bianchi| Via Milano 5, Torino| A1:Mouse:2 |
| 103 | 2025-11-17 | C01 | Mario Rossi | Via Roma 1, Milano | C3:Monitor:1 |

**Problemi evidenti:**
1.  **Anomalia di Aggiornamento:** Se Mario Rossi cambia indirizzo, dobbiamo modificare **tutte** le righe dei suoi ordini, rischiando errori.
2.  **Dati non Atomici:** La colonna `Prodotti_Ordinati` contiene più valori. È impossibile fare una ricerca per singolo prodotto.
3.  **Anomalia di Inserimento:** Non possiamo aggiungere un nuovo cliente finché non ha effettuato almeno un ordine.
4.  **Anomalia di Cancellazione:** Se cancelliamo l'ordine 102, perdiamo l'unica informazione che abbiamo su Anna Bianchi.

---

### Passo 1: Raggiungere la Prima Forma Normale (1NF)

**Regola:** Ogni cella della tabella deve contenere un valore singolo (atomico) e ogni riga deve essere unica.

**Azione:** Dividiamo la colonna `Prodotti_Ordinati` in righe separate, una per ogni prodotto acquistato in un ordine.

**Risultato (Tabella in 1NF):**

| ID_Ordine | Data | ID_Cliente | Nome_Cliente | Indirizzo_Cliente | ID_Prodotto | Quantità |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 101 | 2025-11-15 | C01 | Mario Rossi | Via Roma 1, Milano | A1 | 1 |
| 101 | 2025-11-15 | C01 | Mario Rossi | Via Roma 1, Milano | B2 | 1 |
| 102 | 2025-11-16 | C02 | Anna Bianchi| Via Milano 5, Torino| A1 | 2 |
| 103 | 2025-11-17 | C01 | Mario Rossi | Via Roma 1, Milano | C3 | 1 |

*   **Commento:** Abbiamo risolto il problema dei dati non atomici, ma la ridondanza dei dati del cliente e dell'ordine è addirittura peggiorata! Questo è normale e ci prepara per il passo successivo.

---

### Passo 2: Raggiungere la Seconda Forma Normale (2NF)

**Regola:** Ogni attributo non-chiave deve dipendere dall'**intera** chiave primaria. (Questo si applica quando abbiamo una chiave primaria composta).

**Azione:**
1.  La chiave primaria della nostra tabella in 1NF è `(ID_Ordine, ID_Prodotto)`.
2.  Notiamo che `Data`, `ID_Cliente`, `Nome_Cliente` e `Indirizzo_Cliente` dipendono solo da `ID_Ordine`, non dall'intera chiave.
3.  Per risolvere, dividiamo la tabella in due: una per gli ordini e una per i dettagli dei prodotti in ogni ordine.

**Risultato (Tabelle in 2NF):**

**Tabella `Ordini`**
| ID_Ordine | Data | ID_Cliente | Nome_Cliente | Indirizzo_Cliente |
| :--- | :--- | :--- | :--- | :--- |
| 101 | 2025-11-15 | C01 | Mario Rossi | Via Roma 1, Milano |
| 102 | 2025-11-16 | C02 | Anna Bianchi| Via Milano 5, Torino|
| 103 | 2025-11-17 | C01 | Mario Rossi | Via Roma 1, Milano |

**Tabella `Dettagli_Ordine`**
| ID_Ordine | ID_Prodotto | Quantità |
| :--- | :--- | :--- |
| 101 | A1 | 1 |
| 101 | B2 | 1 |
| 102 | A1 | 2 |
| 103 | C3 | 1 |

*   **Commento:** Ora la struttura è molto più pulita. La maggior parte della ridondanza è sparita. Rimane solo quella dei dati del cliente.

---

### Passo 3: Raggiungere la Terza Forma Normale (3NF)

**Regola:** Non devono esistere dipendenze transitive. Un attributo non-chiave non deve dipendere da un altro attributo non-chiave.

**Azione:** Nella tabella `Ordini`, notiamo che `Nome_Cliente` e `Indirizzo_Cliente` dipendono da `ID_Cliente`, che non è la chiave primaria. Questa è una dipendenza transitiva. Per risolverla, separiamo i dati del cliente in una loro tabella.

**Risultato (Schema Finale Normalizzato in 3NF):**

**Tabella `Clienti`**
| ID_Cliente | Nome_Cliente | Indirizzo_Cliente |
| :--- | :--- | :--- |
| C01 | Mario Rossi | Via Roma 1, Milano |
| C02 | Anna Bianchi| Via Milano 5, Torino|

**Tabella `Ordini`**
| ID_Ordine | Data | ID_Cliente (FK) |
| :--- | :--- | :--- |
| 101 | 2025-11-15 | C01 |
| 102 | 2025-11-16 | C02 |
| 103 | 2025-11-17 | C01 |

**Tabella `Dettagli_Ordine`** (invariata)
| ID_Ordine (FK) | ID_Prodotto (FK) | Quantità |
| :--- | :--- | :--- |
| 101 | A1 | 1 |
| 101 | B2 | 1 |
| 102 | A1 | 2 |
| 103 | C3 | 1 |

*   **Nota:** Per completare lo schema, avremmo bisogno anche di una tabella `Prodotti(ID_Prodotto, Nome_Prodotto, Prezzo)`.

Abbiamo raggiunto uno schema robusto, privo di ridondanze e che previene le anomalie. Ogni pezzo di informazione è memorizzato una sola volta.