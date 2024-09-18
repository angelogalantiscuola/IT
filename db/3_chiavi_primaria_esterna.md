## Chiavi: Primaria, Esterna <!-- omit in toc -->

- [Chiave Primaria](#chiave-primaria)
  - [Caratteristiche della Chiave Primaria](#caratteristiche-della-chiave-primaria)
  - [Esempio di Chiave Primaria](#esempio-di-chiave-primaria)
  - [Importanza della Chiave Primaria](#importanza-della-chiave-primaria)
- [Chiave Esterna](#chiave-esterna)
  - [Caratteristiche della Chiave Esterna](#caratteristiche-della-chiave-esterna)
  - [Esempio di Chiave Esterna](#esempio-di-chiave-esterna)
  - [Importanza della Chiave Esterna](#importanza-della-chiave-esterna)


Le **chiavi** sono elementi fondamentali nel modello relazionale, in quanto garantiscono l'integrità dei dati e permettono di stabilire relazioni tra le tabelle di un database. In particolare, le due principali tipologie di chiavi sono la **chiave primaria** e la **chiave esterna**. In questa lezione, analizzeremo in dettaglio il ruolo di ciascuna e il loro impatto sul mantenimento dell'integrità del database.

### Chiave Primaria

La **chiave primaria** (o *primary key*) è un vincolo che assicura che ogni riga in una tabella sia univocamente identificata. In altre parole, nessuna due righe in una tabella possono avere lo stesso valore nella colonna o combinazione di colonne designate come chiave primaria.

#### Caratteristiche della Chiave Primaria

- **Unicità**: ogni valore nella chiave primaria deve essere unico. Questo garantisce che non ci siano duplicati all'interno della tabella.
  
- **Non nulla**: la chiave primaria non può contenere valori nulli (*NULL*), poiché ogni riga deve avere un identificatore valido e unico.

- **Singola o Composta**: una chiave primaria può essere costituita da una singola colonna (chiave semplice) o da più colonne (chiave composta). In quest'ultimo caso, la combinazione dei valori nelle colonne deve essere unica.

#### Esempio di Chiave Primaria

Immagina di avere una tabella chiamata "Studenti", che contiene le seguenti colonne:

| IDStudente | Nome  | Cognome | DataNascita |
| ---------- | ----- | ------- | ----------- |
| 1          | Mario | Rossi   | 2000-05-20  |
| 2          | Anna  | Bianchi | 1999-12-15  |

In questa tabella, la colonna "IDStudente" può essere definita come chiave primaria, poiché il valore in questa colonna è unico per ogni studente. Nessun altro studente potrà avere lo stesso "IDStudente", garantendo l'unicità.

#### Importanza della Chiave Primaria

La chiave primaria è essenziale per mantenere l'integrità delle entità all'interno di una tabella. Essa permette di:
- Identificare univocamente ciascuna riga della tabella.
- Stabilire relazioni con altre tabelle tramite l'uso di chiavi esterne (argomento trattato nella prossima sezione).
- Garantire che i dati siano privi di duplicati.

### Chiave Esterna

La **chiave esterna** (o *foreign key*) è un vincolo utilizzato per creare e mantenere relazioni tra due tabelle. Una chiave esterna in una tabella fa riferimento alla chiave primaria di un'altra tabella, creando un collegamento tra le due.

#### Caratteristiche della Chiave Esterna

- **Relazione tra tabelle**: la chiave esterna permette di stabilire un legame tra due tabelle, definendo una relazione logica basata sui dati.
  
- **Riferimento a una chiave primaria**: la chiave esterna punta sempre a una colonna o a una combinazione di colonne che rappresentano una chiave primaria in un'altra tabella. Questo assicura che il valore presente nella chiave esterna esista anche nella tabella a cui fa riferimento.

- **Integrità referenziale**: la chiave esterna garantisce che non vengano inseriti valori orfani, cioè valori che non hanno un corrispondente nella tabella collegata. Ad esempio, non dovrebbe essere possibile assegnare un corso a uno studente se questo studente non esiste nella tabella "Studenti".

#### Esempio di Chiave Esterna

Consideriamo due tabelle: "Studenti" e "Corsi". La tabella "Corsi" potrebbe avere una chiave esterna che fa riferimento alla chiave primaria "IDStudente" della tabella "Studenti":

**Tabella Studenti:**

| IDStudente | Nome  | Cognome |
| ---------- | ----- | ------- |
| 1          | Mario | Rossi   |
| 2          | Anna  | Bianchi |

**Tabella Corsi:**

| IDCorsi | Corso       | IDStudente |
| ------- | ----------- | ---------- |
| 101     | Informatica | 1          |
| 102     | Matematica  | 2          |

In questo esempio, la colonna "IDStudente" nella tabella "Corsi" è una chiave esterna che fa riferimento alla colonna "IDStudente" nella tabella "Studenti". Questo crea una relazione tra gli studenti e i corsi a cui sono iscritti.

#### Importanza della Chiave Esterna

La chiave esterna è fondamentale per mantenere l'integrità referenziale in un database relazionale. Attraverso l'uso delle chiavi esterne, si possono costruire relazioni tra le tabelle, garantendo che i dati rimangano consistenti e correlati. La chiave esterna permette di:
- Stabilire legami tra tabelle, creando un sistema di dati interrelati.
- Assicurare che i dati inseriti siano validi, facendo riferimento a entità esistenti in altre tabelle.
