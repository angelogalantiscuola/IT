# Esercizi su Modello Relazionale

## Esercizio 1: Identificazione di Entità, Attributi e Relazioni
**Livello: Principiante**

Scenario: Una piccola libreria vuole creare un database per gestire i suoi libri e clienti.

Compito:
1. Identifica almeno 3 entità principali.
2. Per ogni entità, elenca almeno 3 attributi.
3. Descrivi almeno 2 relazioni tra le entità.

### Esempio di Output:
Entità:
- Libro(ID, Titolo, Autore, Genere)
- Cliente(ID, Nome, Cognome, Email)

Relazioni:
- Un Cliente può prendere in prestito più Libri.
- Un Libro può essere preso in prestito da più Clienti nel tempo.

## Esercizio 2: Creazione di uno Schema Relazionale
**Livello: Intermedio**

Scenario: Un'università vuole creare un database per gestire corsi, studenti e professori.

Compito:
1. Crea uno schema relazionale che includa le seguenti entità: Studente, Corso, Professore.
2. Aggiungi almeno 4 attributi per ogni entità.
3. Definisci le relazioni appropriate tra le entità.
4. Aggiungi almeno un'entità aggiuntiva che potrebbe essere rilevante (es. Dipartimento).

## Esercizio 3: Analisi e Miglioramento di uno Schema
**Livello: Avanzato**

Scenario: Ti viene fornito il seguente schema relazionale per un sistema di gestione ordini:

```
Cliente(ID, Nome, Cognome, Email)
Ordine(NumeroOrdine, DataOrdine, Totale, ClienteID)
ProdottoOrdine(ID, NumeroOrdine, NomeProdotto, Quantità, Prezzo)
```

Compito:
1. Analizza lo schema e identifica eventuali problemi o limitazioni.
2. Proponi miglioramenti allo schema, giustificando le tue scelte.
3. Crea un nuovo schema relazionale che risolva i problemi identificati e includa eventuali nuove entità o relazioni necessarie.
