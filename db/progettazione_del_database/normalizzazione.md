## Forme Normali nel Database Design <!-- omit in toc -->

- [Perché Normalizzare?](#perché-normalizzare)
- [Le Forme Normali](#le-forme-normali)
- [Prima Forma Normale (1NF)](#prima-forma-normale-1nf)
  - [Esempio Non 1NF](#esempio-non-1nf)
  - [Esempio 1NF](#esempio-1nf)
- [Seconda Forma Normale (2NF)](#seconda-forma-normale-2nf)
  - [Esempio Non 2NF](#esempio-non-2nf)
  - [Esempio 2NF](#esempio-2nf)
- [Terza Forma Normale (3NF)](#terza-forma-normale-3nf)
  - [Esempio Non 3NF](#esempio-non-3nf)
  - [Esempio 3NF](#esempio-3nf)

La **normalizzazione** è un processo fondamentale nella progettazione dei database relazionali, volto a organizzare i dati in modo da ridurre la ridondanza e garantire l'integrità dei dati. Lo scopo della normalizzazione è suddividere un database in più tabelle collegate tra loro, mantenendo una struttura logica coerente ed eliminando potenziali anomalie durante l'inserimento, l'aggiornamento o la cancellazione di dati.

La normalizzazione si basa su una serie di regole, note come **forme normali**, che guidano il processo di progettazione del database. Ogni forma normale ha criteri specifici per assicurare che le tabelle rispettino determinati vincoli logici.

### Perché Normalizzare?

Un database non normalizzato può contenere dati ridondanti, il che significa che la stessa informazione potrebbe essere memorizzata in più di un posto. Questo comporta vari problemi:

- **Ridondanza**: Duplicare i dati su più tabelle rende il sistema inefficiente e difficile da mantenere.
- **Anomalie di aggiornamento**: L'aggiornamento di un dato in una parte del database potrebbe non riflettersi correttamente in altre parti, causando inconsistenza.
- **Anomalie di inserimento**: Inserire nuovi dati può diventare problematico se non si dispone di tutte le informazioni necessarie per mantenere la coerenza.
- **Anomalie di cancellazione**: La cancellazione di un dato può comportare la perdita involontaria di altre informazioni.

La normalizzazione aiuta a evitare questi problemi, garantendo che i dati siano organizzati in modo efficiente e coerente.

### Le Forme Normali

Il processo di normalizzazione avviene attraverso una serie di passi progressivi, ognuno dei quali rappresenta una forma normale. Ogni passo risolve un determinato tipo di problema e introduce ulteriori regole di suddivisione dei dati. In questa lezione ci concentreremo sulle prime tre forme normali, che sono le più utilizzate.

### Prima Forma Normale (1NF)

Ogni attributo deve contenere un valore atomico (non divisibile)

#### Esempio Non 1NF

| Studente_ID | Telefoni         | Corsi         |
| ----------- | ---------------- | ------------- |
| 1           | 123-456, 789-012 | Math, Physics |

- Violazione dell'atomicità: le colonne **Telefoni** e **Corsi** contengono valori multipli separati da virgola

#### Esempio 1NF

| Studente_ID | Telefono |
| ----------- | -------- |
| 1           | 123-456  |
| 1           | 789-012  |

| Studente_ID | Corso   |
| ----------- | ------- |
| 1           | Math    |
| 1           | Physics |

### Seconda Forma Normale (2NF)

Una tabella è in 2NF se soddisfa le seguenti condizioni:

1. È già in Prima Forma Normale (1NF).
2. Ogni attributo non-chiave dipende completamente dalla chiave primaria, non solo da una parte di essa.

#### Esempio Non 2NF

| Studente_ID | Corso_ID | Corso_Nome | Studente_Città | Voto |
| ----------- | -------- | ---------- | -------------- | ---- |
| 1           | C1       | Math       | Roma           | 30   |

- **Corso_Nome** dipende completamente da **Corso_ID**, non dall'intera chiave primaria composta da **Studente_ID** e **Corso_ID**.
- **Studente_Città** dipende completamente da **Studente_ID**, non dall'intera chiave primaria.

#### Esempio 2NF

| Studente_ID | Corso_ID | Voto |
| ----------- | -------- | ---- |
| 1           | C1       | 30   |

| Corso_ID | Corso_Nome |
| -------- | ---------- |
| C1       | Math       |

| Studente_ID | Studente_Città |
| ----------- | -------------- |
| 1           | Roma           |

### Terza Forma Normale (3NF)

Una tabella è in 3NF se soddisfa le seguenti condizioni:

1. È già in 2NF.
2. Non ci sono dipendenze transitive tra attributi non-chiave. In altre parole, ogni attributo non-chiave dipende direttamente dalla chiave primaria e non da altri attributi non-chiave.

#### Esempio Non 3NF

| Dipartimento_ID | Dipartimento_Nome | Capo_Dipartimento | Stipendio_Capo |
| --------------- | ----------------- | ----------------- | -------------- |
| 1               | Informatica       | Rossi             | 50000          |

- In questo caso, **Stipendio_Capo** dipende transitivamente da **Dipartimento_ID** attraverso **Capo_Dipartimento**.

#### Esempio 3NF

| Dipartimento_ID | Dipartimento_Nome | Capo_Dipartimento |
| --------------- | ----------------- | ----------------- |
| 1               | Informatica       | Rossi             |

| Capo_Dipartimento | Stipendio_Capo |
| ----------------- | -------------- |
| Rossi             | 50000          |
