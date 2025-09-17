## Il Modello Relazionale <!-- omit in toc -->

- [Relazioni e Tabelle](#relazioni-e-tabelle)
- [Proprietà di una Tabella Relazionale](#proprietà-di-una-tabella-relazionale)

Il **modello relazionale**, introdotto da Edgar F. Codd nel 1970, è il fondamento teorico su cui si basano la maggior parte dei moderni sistemi di gestione di database (RDBMS). Questo modello organizza i dati in modo semplice e intuitivo utilizzando le **relazioni**, che sono più comunemente conosciute come **tabelle**.

### Relazioni e Tabelle

Nel modello relazionale, una **relazione** è una struttura bidimensionale composta da righe e colonne.

- **Tabella**: La rappresentazione pratica di una relazione.
- **Attributo (o Campo)**: Una colonna della tabella, che rappresenta una specifica proprietà dei dati (es. `Nome`, `Eta`). Ogni attributo ha un **dominio**, ovvero l'insieme dei valori che può assumere (es. `INTEGER`, `VARCHAR(50)`).
- **Tupla (o Record)**: Una riga della tabella, che rappresenta una singola istanza o un singolo elemento dei dati (es. i dati di un specifico studente).

```
Tabella: Studenti
+-----------+---------+---------+
| Matricola | Nome    | Cognome |  <-- Attributi
+-----------+---------+---------+
| 101       | Mario   | Rossi   |  <-- Tupla 1
| 102       | Anna    | Bianchi |  <-- Tupla 2
+-----------+---------+---------+
```

### Proprietà di una Tabella Relazionale

Una tabella, per essere considerata una relazione valida, deve rispettare alcune proprietà fondamentali:

1.  **I valori sono atomici**: Ogni cella contiene un solo valore. (Questo corrisponde alla Prima Forma Normale).
2.  **Tutte le righe sono uniche**: Non possono esistere due righe identiche. Questo è garantito dall'uso di una **chiave primaria**.
3.  **L'ordine delle righe è irrilevante**: Le righe non hanno un ordine intrinseco.
4.  **L'ordine delle colonne è irrilevante**: Le colonne possono essere riordinate senza alterare il significato dei dati, poiché sono identificate dal loro nome.
5.  **Ogni colonna ha un nome unico** all'interno della stessa tabella.
