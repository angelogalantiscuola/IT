# Esercizi di Normalizzazione

## Esercizio 1: Identificazione di Dipendenze Funzionali
**Livello: Principiante**

Data la seguente tabella:
```
Ordine(NumeroOrdine, DataOrdine, IDCliente, NomeCliente, ProdottoID, NomeProdotto, Quantità, PrezzoUnitario)
```

Compito:
1. Identifica la chiave primaria.
2. Elenca tutte le dipendenze funzionali presenti nella tabella.
3. Spiega brevemente il concetto di dipendenza funzionale.

## Esercizio 2: Prima Forma Normale (1NF)
**Livello: Intermedio**

Data la seguente tabella:
```
Studente(MatricolaStudente, Nome, Cognome, Corsi, Voti)
```
Dove Corsi e Voti sono attributi multi-valore che contengono rispettivamente la lista dei corsi seguiti e i voti ottenuti.

Compito:
1. Spiega perché questa tabella non è in Prima Forma Normale.
2. Converti la tabella in 1NF.
3. Descrivi i passaggi che hai seguito per raggiungere la 1NF.

## Esercizio 3: Seconda Forma Normale (2NF)
**Livello: Avanzato**

Data la seguente tabella in 1NF:
```
CorsoStudente(CodiceCorso, NomeCorso, MatricolaStudente, NomeStudente, Professore)
```
Dove la chiave primaria è (CodiceCorso, MatricolaStudente).

Compito:
1. Determina se la tabella è in 2NF. Se non lo è, spiega perché.
2. Se necessario, decomponi la tabella per portarla in 2NF.
3. Descrivi le dipendenze funzionali presenti nelle nuove tabelle.

## Esercizio 4: Terza Forma Normale (3NF)
**Livello: Esperto**

Data la seguente tabella in 2NF:
```
Impiegato(IDImpiegato, Nome, Cognome, Dipartimento, NomeDirettore, StipendioBase)
```

Compito:
1. Identifica eventuali dipendenze transitive.
2. Decomponi la tabella per portarla in 3NF.
3. Spiega come la 3NF elimina le dipendenze transitive e quali benefici porta.
4. Crea un diagramma ER che rappresenti lo schema finale in 3NF.

## Esercizio 5: Analisi e Normalizzazione Completa
**Livello: Avanzato Plus**

Data la seguente tabella:
```
Biblioteca(CodicePrestito, TitoloLibro, AutoreLibro, ISBNLibro, NomeMembro, IDMembro, DataPrestito, DataRestituzionePrevista, CategoriaLibro)
```

Compito:
1. Identifica tutte le dipendenze funzionali presenti.
2. Partendo dalla tabella iniziale, esegui passo dopo passo il processo di normalizzazione fino alla 3NF.
3. Per ogni passaggio (1NF, 2NF, 3NF):
   a. Spiega le modifiche apportate.
   b. Giustifica le tue decisioni di decomposizione.
4. Crea un diagramma ER finale che rappresenti lo schema in 3NF.
5. Discuti brevemente i vantaggi e gli eventuali svantaggi della normalizzazione in questo caso specifico.