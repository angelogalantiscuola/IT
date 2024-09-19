# Esercizi sui Fondamenti di Database e Modello Relazionale

## Esercizio 1: Identificazione di Entità, Attributi e Relazioni
**Livello: Principiante**

Scenario: Una piccola libreria vuole creare un database per gestire i suoi libri e clienti.

Compito:
1. Identifica almeno 3 entità principali.
2. Per ogni entità, elenca almeno 3 attributi.
3. Descrivi almeno 2 relazioni tra le entità.

## Esercizio 2: Creazione di uno Schema ER
**Livello: Intermedio**

Scenario: Un'università vuole creare un database per gestire corsi, studenti e professori.

Compito:
1. Crea un diagramma ER che includa le seguenti entità: Studente, Corso, Professore.
2. Aggiungi almeno 4 attributi per ogni entità.
3. Definisci le relazioni appropriate tra le entità, specificando la cardinalità.
4. Aggiungi almeno un'entità aggiuntiva che potrebbe essere rilevante (es. Dipartimento).

## Esercizio 3: Conversione da Schema ER a Schema Relazionale
**Livello: Avanzato**

Scenario: Utilizza lo schema ER creato nell'Esercizio 2.

Compito:
1. Converti lo schema ER in uno schema relazionale.
2. Identifica le chiavi primarie per ogni tabella.
3. Definisci le chiavi esterne necessarie per rappresentare le relazioni.
4. Scrivi la definizione delle tabelle usando la sintassi SQL (CREATE TABLE).

## Esercizio 4: Analisi e Miglioramento di uno Schema
**Livello: Esperto**

Scenario: Ti viene fornito il seguente schema relazionale per un sistema di gestione ordini:

```
Cliente(ID, Nome, Cognome, Email)
Ordine(NumeroOrdine, DataOrdine, Totale, ClienteID)
ProdottoOrdine(ID, NumeroOrdine, NomeProdotto, Quantità, Prezzo)
```

Compito:
1. Analizza lo schema e identifica eventuali problemi o limitazioni.
2. Proponi miglioramenti allo schema, giustificando le tue scelte.
3. Crea un nuovo schema ER che risolva i problemi identificati e includa eventuali nuove entità o relazioni necessarie.
4. Converti il nuovo schema ER in uno schema relazionale, specificando chiavi primarie e esterne.