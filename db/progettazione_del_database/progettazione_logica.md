## Progettazione Logica <!-- omit in toc -->

- [Introduzione alla Progettazione Logica](#introduzione-alla-progettazione-logica)
- [Trasformazione dello Schema Concettuale](#trasformazione-dello-schema-concettuale)
- [Definizione delle Tabelle](#definizione-delle-tabelle)
- [Definizione delle Chiavi](#definizione-delle-chiavi)
  - [Chiavi Primarie](#chiavi-primarie)
  - [Chiavi Esterne](#chiavi-esterne)
- [Normalizzazione](#normalizzazione)
- [Vincoli di Integrità](#vincoli-di-integrità)
- [Esempio Completo](#esempio-completo)
- [Conclusione](#conclusione)

### Introduzione alla Progettazione Logica

La **progettazione logica** è una fase cruciale nella creazione di un database relazionale. In questa fase, lo schema concettuale, rappresentato tipicamente tramite diagrammi ER, viene trasformato in uno schema logico che può essere implementato su un sistema di gestione di database (DBMS). Questo processo include la definizione delle tabelle, delle chiavi primarie e delle chiavi esterne, nonché l'applicazione delle regole di normalizzazione per garantire l'integrità e l'efficienza dei dati.

### Trasformazione dello Schema Concettuale

Il primo passo nella progettazione logica è trasformare lo schema concettuale in uno schema logico. Questo implica la conversione delle entità e delle relazioni del diagramma ER in tabelle e colonne.

### Definizione delle Tabelle

Ogni entità del diagramma ER viene trasformata in una tabella. Gli attributi dell'entità diventano le colonne della tabella. Ad esempio, se abbiamo un'entità "Studente" con attributi "IDStudente", "Nome", "Cognome", e "DataNascita", la tabella corrispondente sarà:

| IDStudente | Nome | Cognome | DataNascita |
| ---------- | ---- | ------- | ----------- |

### Definizione delle Chiavi

#### Chiavi Primarie

La **chiave primaria** è un attributo (o un insieme di attributi) che identifica univocamente ogni record in una tabella. Deve essere unico e non nullo. Ad esempio, "IDStudente" può essere la chiave primaria della tabella "Studente".

#### Chiavi Esterne

Le **chiavi esterne** sono attributi che creano un collegamento tra due tabelle. Una chiave esterna in una tabella fa riferimento alla chiave primaria di un'altra tabella, stabilendo una relazione tra le due. Ad esempio, se un "Corso" è frequentato da più studenti, la tabella "Iscrizione" potrebbe avere "IDStudente" come chiave esterna che fa riferimento alla chiave primaria della tabella "Studente".

### Vincoli di Integrità

I vincoli di integrità assicurano che i dati nel database siano accurati e coerenti. I principali vincoli includono:

- **Vincoli di unicità**: Assicurano che i valori di una colonna (o di un insieme di colonne) siano unici.
- **Vincoli di chiave primaria**: Assicurano che la chiave primaria sia unica e non nulla.
- **Vincoli di chiave esterna**: Assicurano che i valori delle chiavi esterne corrispondano ai valori delle chiavi primarie nelle tabelle correlate.
- **Vincoli di integrità referenziale**: Assicurano che le relazioni tra le tabelle rimangano coerenti.

### Esempio Completo

Consideriamo un esempio di progettazione logica per un sistema universitario. Partendo dal diagramma ER, definiamo le tabelle e le relazioni:

**Tabella Studente:**

| IDStudente | Nome | Cognome | DataNascita |
| ---------- | ---- | ------- | ----------- |
| PK         |      |         |             |

**Tabella Corso:**

| IDCorso | NomeCorso | Crediti | IDProfessore | IDDipartimento |
| ------- | --------- | ------- | ------------ | -------------- |
| PK      |           |         | FK           | FK             |

**Tabella Iscrizione:**

| IDStudente | IDCorso | DataIscrizione | Voto |
| ---------- | ------- | -------------- | ---- |
| PK, FK     | PK, FK  |                |      |

**Tabella Professore:**

| IDProfessore | Nome | Cognome | Specializzazione | IDDipartimento |
| ------------ | ---- | ------- | ---------------- | -------------- |
| PK           |      |         |                  | FK             |

**Tabella Dipartimento:**

| IDDipartimento | Nome |
| -------------- | ---- |
| PK             |      |

**Relazioni:**

- La tabella "Iscrizione" ha chiavi esterne "IDStudente" e "IDCorso" che fanno riferimento rispettivamente alle chiavi primarie delle tabelle "Studente" e "Corso".
- La tabella "Corso" ha chiavi esterne "IDProfessore" e "IDDipartimento" che fanno riferimento rispettivamente alle chiavi primarie delle tabelle "Professore" e "Dipartimento".
- La tabella "Professore" ha una chiave esterna "IDDipartimento" che fa riferimento alla chiave primaria della tabella "Dipartimento".

### Conclusione

La progettazione logica è un passo fondamentale nella creazione di un database relazionale. Trasformando lo schema concettuale in uno schema logico, definendo tabelle, chiavi e vincoli, e applicando le regole di normalizzazione, possiamo garantire che il database sia efficiente, coerente e privo di anomalie. Una buona progettazione logica è essenziale per il successo di qualsiasi sistema informativo basato su database.
