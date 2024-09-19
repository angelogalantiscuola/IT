## Vincoli di Integrità  <!-- omit in toc -->

- [Tipologie di Vincoli di Integrità](#tipologie-di-vincoli-di-integrità)
  - [Integrità dell'Entità](#integrità-dellentità)
  - [Integrità Referenziale](#integrità-referenziale)
  - [Vincoli di Dominio](#vincoli-di-dominio)
  - [Vincoli di Unicità](#vincoli-di-unicità)
  - [Vincoli di Nullità](#vincoli-di-nullità)
  - [Vincoli di Check](#vincoli-di-check)
- [Applicazione dei Vincoli nel DBMS](#applicazione-dei-vincoli-nel-dbms)


I **vincoli di integrità** sono regole che garantiscono la correttezza, la consistenza e la validità dei dati all'interno di un database. Questi vincoli vengono definiti durante la progettazione del database e sono implementati dai sistemi di gestione dei database (DBMS) per evitare inserimenti, aggiornamenti o eliminazioni di dati non validi. Essi svolgono un ruolo cruciale nel mantenere l'integrità dei dati, prevenendo anomalie e garantendo che le relazioni tra tabelle siano coerenti.

### Tipologie di Vincoli di Integrità

Esistono diverse tipologie di vincoli di integrità che possono essere applicate ai dati di un database. I principali sono:

- **Integrità dell'entità**: riguarda l'unicità delle righe in una tabella.
- **Integrità referenziale**: assicura la validità delle relazioni tra tabelle.
- **Vincoli di dominio**: limitano i valori che possono essere inseriti in una colonna.
- **Vincoli di unicità**: garantiscono che i valori di una colonna siano unici.
- **Vincoli di nullità**: stabiliscono se una colonna può contenere valori nulli.

#### Integrità dell'Entità

L'integrità dell'entità garantisce che ogni riga di una tabella sia univocamente identificabile. Questo si ottiene attraverso la **chiave primaria** (discussa nella lezione precedente), che non permette la duplicazione dei dati e impedisce l'inserimento di valori nulli nelle colonne che costituiscono la chiave.

**Esempio**: In una tabella "Studenti", la colonna "IDStudente" è la chiave primaria. Questo significa che ogni valore in "IDStudente" deve essere unico e non può essere nullo. Se si cerca di inserire due righe con lo stesso "IDStudente", il DBMS genererà un errore.

#### Integrità Referenziale

L'integrità referenziale garantisce la coerenza delle relazioni tra tabelle. Questo viene fatto tramite le **chiavi esterne** (anch'esse discusse nella lezione precedente). Una chiave esterna in una tabella deve sempre fare riferimento a una chiave primaria in un'altra tabella, assicurando che i dati collegati esistano e che non vengano inseriti riferimenti non validi.

**Esempio**: Se esiste una relazione tra le tabelle "Studenti" e "Corsi", in cui "IDStudente" nella tabella "Corsi" è una chiave esterna che punta alla chiave primaria "IDStudente" nella tabella "Studenti", non sarà possibile inserire un corso per uno studente inesistente.

#### Vincoli di Dominio

I **vincoli di dominio** limitano i valori che possono essere inseriti in una colonna, definendo un intervallo o un insieme di valori validi. Questi vincoli permettono di assicurare che i dati siano conformi a regole specifiche.

**Esempio**: In una tabella "Studenti", è possibile definire che la colonna "Età" può accettare solo valori compresi tra 18 e 100. Se si tenta di inserire un'età inferiore a 18 o superiore a 100, il DBMS impedirà l'operazione.

I vincoli di dominio possono essere definiti tramite **tipi di dati** (come `INTEGER`, `VARCHAR`, `DATE`) o regole più complesse definite con espressioni di controllo dei dati.

#### Vincoli di Unicità

I **vincoli di unicità** assicurano che tutti i valori di una determinata colonna (o combinazione di colonne) siano unici. Questo vincolo è simile alla chiave primaria, ma a differenza della chiave primaria, può accettare valori nulli.

**Esempio**: In una tabella "Corsi", è possibile applicare un vincolo di unicità alla colonna "NomeCorso", in modo che non sia possibile inserire due corsi con lo stesso nome.

#### Vincoli di Nullità

I **vincoli di nullità** stabiliscono se una colonna può accettare valori nulli o meno. Un valore nullo rappresenta l'assenza di un dato, non un valore zero o una stringa vuota, ma proprio l'assenza totale di informazione.

**Esempio**: In una tabella "Studenti", la colonna "Nome" potrebbe avere un vincolo di nullità che non permette di inserire righe senza un valore per "Nome". Questo assicura che tutti gli studenti abbiano un nome definito.

#### Vincoli di Check

Il **vincolo di check** permette di definire condizioni personalizzate che devono essere soddisfatte per inserire o modificare i dati di una tabella. Si tratta di regole aggiuntive che permettono di validare i dati in modo più specifico rispetto ai semplici vincoli di dominio.

**Esempio**: In una tabella "Dipendenti", è possibile definire un vincolo `CHECK` sulla colonna "Salario" che impedisca l'inserimento di un salario inferiore a un certo valore, ad esempio `CHECK (Salario >= 1000)`.

### Applicazione dei Vincoli nel DBMS

I vincoli vengono implementati e gestiti automaticamente dal DBMS. Quando si definisce una tabella, i vincoli possono essere inclusi nella definizione della tabella tramite il linguaggio SQL (questo aspetto sarà approfondito nella lezione su SQL).

Ecco un esempio di definizione di una tabella con vincoli in SQL:

```sql
CREATE TABLE Studenti (
    IDStudente INT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Età INT CHECK (Età >= 18 AND Età <= 100),
    CodiceCorso INT,
    FOREIGN KEY (CodiceCorso) REFERENCES Corsi(IDCorso)
);
```

In questo esempio:
- "IDStudente" è definito come chiave primaria.
- "Nome" ha un vincolo `NOT NULL`, quindi non può essere nullo.
- "Età" ha un vincolo `CHECK` che limita i valori accettabili.
- "CodiceCorso" è una chiave esterna che fa riferimento alla colonna "IDCorso" della tabella "Corsi", garantendo l'integrità referenziale.

I vincoli di integrità sono cruciali per mantenere la qualità dei dati in un database e prevenire l'inserimento di informazioni incoerenti o errate. L'uso appropriato di chiavi primarie, esterne, vincoli di dominio e altri vincoli assicura che i dati siano consistenti e validi. La loro corretta applicazione è un passo fondamentale nella progettazione e gestione dei database relazionali.
