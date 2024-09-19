# Esercizi su Chiavi e Vincoli di Integrità

## Esercizio 1: Identificazione di Chiavi
**Livello: Principiante**

Dato il seguente schema di relazione per una libreria:

```
Libro(ISBN, Titolo, Autore, AnnoPubblicazione, Prezzo)
```

Compito:
1. Identifica la chiave primaria più adatta.
2. Elenca tutte le possibili chiavi candidate.
3. Spiega perché hai scelto quella specifica chiave primaria.

## Esercizio 2: Definizione di Chiavi Esterne
**Livello: Intermedio**

Date le seguenti relazioni per un sistema universitario:

```
Studente(MatricolaStudente, Nome, Cognome, DataNascita)
Corso(CodiceCorso, NomeCorso, Crediti)
Iscrizione(ID, MatricolaStudente, CodiceCorso, DataIscrizione)
```

Compito:
1. Identifica le chiavi primarie per ciascuna relazione.
2. Definisci le chiavi esterne necessarie nella relazione Iscrizione.
3. Spiega come queste chiavi esterne garantiscono l'integrità referenziale tra le relazioni.

## Esercizio 3: Implementazione di Vincoli di Integrità
**Livello: Avanzato**

Considera il seguente schema per un sistema di gestione ordini:

```
Cliente(IDCliente, Nome, Email)
Ordine(NumeroOrdine, DataOrdine, IDCliente, TotaleOrdine)
DettaglioOrdine(ID, NumeroOrdine, ProdottoID, Quantità, PrezzoUnitario)
Prodotto(ProdottoID, NomeProdotto, PrezzoCatalogo, Disponibilità)
```

Compito:
1. Definisci le chiavi primarie e esterne per tutte le relazioni.
2. Descrivi quale vincolo di dominio applicare su Quantità in DettaglioOrdine.
3. Descrivi quale vincolo di unicità applicare sull'Email del Cliente.
4. Descrivi quale vincolo di integrità applicare su TotaleOrdine considerando Quantità e PrezzoUnitario in DettaglioOrdine.

## Esercizio 4: Analisi e Correzione di Vincoli di Integrità
**Livello: Esperto**

Ti viene fornito il seguente schema di database per un sistema di gestione di una clinica veterinaria:

```
Proprietario (ID, Nome, Cognome, Telefono)
Animale (ID, Nome, Specie, DataNascita, ProprietarioID)
Visita (ID, AnimalID, DataVisita, Descrizione, Costo)
```

Compito:
1. Analizza lo schema e identifica eventuali problemi o carenze nei vincoli di integrità.
2. Proponi miglioramenti allo schema, giustificando le tue scelte.
3. Descrivi vincoli aggiuntivi per garantire l'integrità dei dati (es. assicurarsi che la DataNascita dell'Animale non sia nel futuro).
4. Crea una nuova relazione per i Veterinari e stabilisci la relazione appropriata con la relazione Visita.
