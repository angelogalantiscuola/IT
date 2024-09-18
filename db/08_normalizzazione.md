## Normalizzazione <!-- omit in toc -->

- [Perché Normalizzare?](#perché-normalizzare)
- [Le Forme Normali](#le-forme-normali)
  - [Prima Forma Normale (1NF)](#prima-forma-normale-1nf)
    - [Requisiti della 1NF](#requisiti-della-1nf)
    - [Esempio](#esempio)
  - [Seconda Forma Normale (2NF)](#seconda-forma-normale-2nf)
    - [Requisiti della 2NF](#requisiti-della-2nf)
    - [Esempio](#esempio-1)
  - [Terza Forma Normale (3NF)](#terza-forma-normale-3nf)
    - [Requisiti della 3NF](#requisiti-della-3nf)
    - [Esempio](#esempio-2)
- [Conclusione](#conclusione)

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

Il processo di normalizzazione avviene attraverso una serie di passi progressivi, ognuno dei quali rappresenta una "forma normale". Ogni passo risolve un determinato tipo di problema e introduce ulteriori regole di suddivisione dei dati. In questa lezione ci concentreremo sulle prime tre forme normali, che sono le più utilizzate.

#### Prima Forma Normale (1NF)

La **Prima Forma Normale (1NF)** richiede che ogni colonna in una tabella contenga solo valori atomici (indivisibili) e che ogni riga sia identificata univocamente. In altre parole, non ci devono essere campi che contengono più valori e non ci devono essere righe duplicate.

##### Requisiti della 1NF
1. **Valori atomici**: Ogni colonna deve contenere un solo valore.
2. **Assenza di duplicati**: Le righe non possono essere duplicate.

##### Esempio

Immaginiamo di avere una tabella non normalizzata in cui un campo contiene più valori:

| Studente | Corsi Seguiti           |
| -------- | ----------------------- |
| Mario    | Matematica, Informatica |
| Laura    | Fisica                  |

Questa tabella viola la 1NF, perché la colonna "Corsi Seguiti" contiene più valori. Per normalizzarla, possiamo suddividere i dati in più righe:

| Studente | Corso       |
| -------- | ----------- |
| Mario    | Matematica  |
| Mario    | Informatica |
| Laura    | Fisica      |

#### Seconda Forma Normale (2NF)

La **Seconda Forma Normale (2NF)** si basa sulla 1NF e aggiunge il requisito che ogni attributo non chiave deve dipendere interamente dalla chiave primaria della tabella. Questo implica che, se una tabella ha una chiave composta (ovvero una chiave formata da più di un attributo), tutti gli attributi non chiave devono dipendere da tutti gli attributi della chiave e non solo da una parte di essa.

##### Requisiti della 2NF
1. **Essere in 1NF**.
2. **Eliminare la dipendenza parziale**: Gli attributi non chiave devono dipendere interamente dalla chiave primaria.

##### Esempio

Consideriamo una tabella che registra i corsi e gli insegnanti, dove la chiave primaria è composta da "Studente" e "Corso":

| Studente | Corso       | Insegnante    |
| -------- | ----------- | ------------- |
| Mario    | Matematica  | Prof. Rossi   |
| Mario    | Informatica | Prof. Bianchi |
| Laura    | Fisica      | Prof. Verdi   |

In questo esempio, l'attributo "Insegnante" dipende solo dal "Corso" e non dallo "Studente". Per normalizzare la tabella in 2NF, possiamo separare i dati in due tabelle:

**Tabella Studenti-Corsi:**

| Studente | Corso       |
| -------- | ----------- |
| Mario    | Matematica  |
| Mario    | Informatica |
| Laura    | Fisica      |

**Tabella Corsi-Insegnanti:**

| Corso       | Insegnante    |
| ----------- | ------------- |
| Matematica  | Prof. Rossi   |
| Informatica | Prof. Bianchi |
| Fisica      | Prof. Verdi   |

In questo modo, abbiamo eliminato la dipendenza parziale.

#### Terza Forma Normale (3NF)

La **Terza Forma Normale (3NF)** richiede che, oltre a soddisfare la 2NF, tutti gli attributi non chiave siano indipendenti tra loro. Questo significa che ogni attributo non chiave deve dipendere esclusivamente dalla chiave primaria e non da altri attributi non chiave. In altre parole, non ci devono essere dipendenze transitive tra gli attributi.

##### Requisiti della 3NF
1. **Essere in 2NF**.
2. **Eliminare le dipendenze transitive**: Nessun attributo non chiave può dipendere da un altro attributo non chiave.

##### Esempio

Consideriamo una tabella che include studenti, corsi e il dipartimento del corso:

| Studente | Corso      | Insegnante  | Dipartimento |
| -------- | ---------- | ----------- | ------------ |
| Mario    | Matematica | Prof. Rossi | Scienze      |
| Laura    | Fisica     | Prof. Verdi | Scienze      |

In questo caso, "Dipartimento" dipende da "Corso" e non da "Studente". Per portare questa tabella in 3NF, possiamo rimuovere la dipendenza transitiva dividendo la tabella in due:

**Tabella Studenti-Corsi:**

| Studente | Corso      |
| -------- | ---------- |
| Mario    | Matematica |
| Laura    | Fisica     |

**Tabella Corsi-Dipartimenti:**

| Corso      | Dipartimento |
| ---------- | ------------ |
| Matematica | Scienze      |
| Fisica     | Scienze      |

In questo modo, ogni attributo dipende direttamente dalla chiave primaria e le dipendenze transitive sono eliminate.

### Conclusione

La normalizzazione è essenziale per garantire un database efficiente e privo di anomalie. Attraverso l'applicazione delle varie forme normali, è possibile migliorare la struttura logica del database, riducendo la ridondanza e assicurando che i dati siano organizzati in modo coerente. Tuttavia, la normalizzazione deve essere bilanciata con le esigenze di prestazioni e complessità, poiché un'eccessiva divisione delle tabelle può rendere le query più lente e difficili da gestire.

> **Nota**: Le forme normali più avanzate, come la **Boyce-Codd Normal Form (BCNF)** e la **Quarta e Quinta Forma Normale**, saranno trattate in una lezione successiva.