# Esercizi sulle Forme Normali Avanzate

## Esercizio 1: Introduzione alla Forma Normale di Boyce-Codd (BCNF)
**Livello: Intermedio**

Data la seguente relazione in 3NF:
```
Corso(CodiceCorso, NomeCorso, Professore, Dipartimento)
```
Dove:
- CodiceCorso → NomeCorso, Professore
- Professore → Dipartimento
- CodiceCorso è la chiave primaria

Compito:
1. Determina se questa relazione è in BCNF. Se non lo è, spiega perché.
2. Se necessario, decomponi la relazione per portarla in BCNF.
3. Spiega la differenza tra 3NF e BCNF in questo contesto.

## Esercizio 2: Analisi e Decomposizione BCNF
**Livello: Avanzato**

Data la seguente relazione:
```
Progetto(IDProgetto, NomeProgetto, Dipendente, Competenza, DataInizio)
```
Con le seguenti dipendenze funzionali:
- IDProgetto, Dipendente → NomeProgetto, Competenza, DataInizio
- IDProgetto → NomeProgetto
- Dipendente → Competenza

Compito:
1. Identifica la chiave primaria della relazione.
2. Determina se la relazione è in 3NF e spiega perché.
3. Verifica se la relazione è in BCNF. Se non lo è, esegui la decomposizione necessaria.
4. Spiega ogni passo del processo di decomposizione.

## Esercizio 3: Introduzione alla Quarta Forma Normale (4NF)
**Livello: Avanzato**

Data la seguente relazione in BCNF:
```
StudenteClub(Studente, Club, Sport)
```
Dove uno studente può appartenere a diversi club e praticare diversi sport, e non c'è relazione diretta tra club e sport.

Compito:
1. Spiega perché questa relazione, pur essendo in BCNF, potrebbe presentare problemi.
2. Definisci il concetto di dipendenza multivalore.
3. Determina se la relazione è in 4NF. Se non lo è, esegui la decomposizione necessaria.
4. Discuti i vantaggi della 4NF rispetto alla BCNF in questo scenario.

## Esercizio 4: Analisi Completa e Normalizzazione Avanzata
**Livello: Esperto**

Data la seguente relazione:
```
Insegnamento(Professore, Corso, Libro, Editore)
```
Con le seguenti dipendenze:
- Professore, Corso → Libro
- Libro → Editore
- Professore → Corso
- Corso → Professore

Compito:
1. Identifica tutte le chiavi candidate della relazione.
2. Determina se la relazione è in 3NF, BCNF e 4NF. Giustifica le tue risposte.
3. Se necessario, decomponi la relazione per portarla alla massima forma normale possibile tra quelle studiate.
4. Per ogni decomposizione:
   a. Spiega il motivo della decomposizione.
   b. Verifica che non ci sia perdita di informazioni.
5. Crea un diagramma ER che rappresenti lo schema finale dopo tutte le decomposizioni.
6. Discuti i pro e i contro della normalizzazione a questo livello avanzato in un contesto reale.