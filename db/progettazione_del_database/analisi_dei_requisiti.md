# Analisi dei Requisiti  <!-- omit in toc -->

- [Progettazione Concettuale](#progettazione-concettuale)
  - [1. Creazione del Diagramma ER](#1-creazione-del-diagramma-er)
    - [Componenti principali del diagramma ER:](#componenti-principali-del-diagramma-er)
    - [Esempio:](#esempio)
  - [2. Definizione delle regole di business](#2-definizione-delle-regole-di-business)
    - [Relazione con altre lezioni](#relazione-con-altre-lezioni)


L'**analisi dei requisiti** è la prima e fondamentale fase della progettazione di un database. In questa fase, l'obiettivo è comprendere in modo dettagliato le necessità del committente e tradurle in specifiche tecniche per il database. Non si tratta solo di raccogliere informazioni, ma di interpretarle correttamente e organizzare una visione chiara e strutturata delle funzionalità richieste.

## 1. Comunicazione con il committente

La prima attività consiste nel dialogare con il committente per identificare i requisiti principali. È cruciale usare un linguaggio accessibile, evitando tecnicismi che potrebbero non essere chiari al committente. Alcuni strumenti utili in questa fase sono:

- **Interviste**: colloqui diretti con i committenti e gli utenti finali del sistema.
- **Questionari**: raccolta di informazioni tramite moduli strutturati.
- **Workshop**: sessioni di lavoro con gruppi di utenti e stakeholder per definire i requisiti in modo collaborativo.

### Obiettivi dell'analisi dei requisiti

1. **Identificare i dati chiave**: quali informazioni devono essere memorizzate?
   - Esempio: per un sistema di gestione di una biblioteca, i dati chiave includono libri, utenti, prestiti, autori, ecc.
   
2. **Comprendere i processi**: quali operazioni devono essere eseguite sui dati?
   - Esempio: un utente deve poter prendere in prestito un libro, restituirlo, o cercare nel catalogo.

3. **Definire vincoli e regole**: quali restrizioni o regole di integrità devono essere applicate?
   - Esempio: un utente non può prendere in prestito più di cinque libri contemporaneamente.

## 2. Identificazione delle entità e relazioni

Una volta compresi i requisiti, il passo successivo è identificare le **entità** (oggetti principali del sistema) e le **relazioni** tra di esse. Questa fase è cruciale per passare alla progettazione concettuale.

- **Entità**: sono oggetti rilevanti per il sistema, come "Libro", "Utente", "Autore".
- **Relazioni**: descrivono come le entità sono collegate tra loro. Ad esempio, un utente può prendere in prestito più libri (relazione "prestito").

La sfida in questa fase è assicurarsi che tutte le entità e le relazioni riflettano accuratamente i processi aziendali. Un errore comune è quello di identificare troppe o troppo poche entità. Un approccio iterativo, in cui le specifiche vengono riviste e affinate, può aiutare a evitare questo problema.

---

# Progettazione Concettuale

La **progettazione concettuale** è la fase in cui i requisiti raccolti vengono trasformati in un modello concettuale del database, rappresentato tipicamente da un **diagramma ER** (Entity-Relationship). Questo modello non è ancora un'implementazione tecnica, ma un modo per visualizzare le informazioni e le relazioni.

## 1. Creazione del Diagramma ER

Il **diagramma ER** rappresenta le entità e le relazioni identificate durante l'analisi dei requisiti. È uno strumento grafico che consente di visualizzare le interazioni tra i dati in modo intuitivo.

### Componenti principali del diagramma ER:

- **Entità**: rappresentate da rettangoli, sono gli oggetti del sistema che hanno un significato.
- **Relazioni**: rappresentate da rombi, collegano due o più entità e descrivono come queste interagiscono.
- **Attributi**: rappresentati da ovali, descrivono le proprietà di un'entità. Ad esempio, un'entità "Libro" può avere attributi come "Titolo", "ISBN", "Anno di Pubblicazione".
- **Cardinalità**: indicano quante occorrenze di un'entità possono essere associate a un'altra entità. Ad esempio, un autore può scrivere più libri (relazione 1 a molti).

### Esempio:

Immaginiamo un sistema di gestione di una biblioteca. Le entità principali sono "Libro", "Utente" e "Prestito". La relazione "Prestito" collega l'entità "Utente" con l'entità "Libro", e la cardinalità stabilisce che un utente può prendere in prestito molti libri, ma ogni libro può essere preso in prestito da un solo utente alla volta.

```
Utente ------------- Prestito ------------- Libro
```

## 2. Definizione delle regole di business

Durante la progettazione concettuale, è importante includere le **regole di business**, ovvero le restrizioni specifiche che governano il funzionamento del sistema.

- **Esempio di regola di business**: Un utente non può prendere in prestito più di cinque libri contemporaneamente. Questa regola deve essere riflessa nel modello, eventualmente includendo un vincolo nell'entità "Utente" o nella relazione "Prestito".

---

### Relazione con altre lezioni

Questo materiale si concentra sull'analisi dei requisiti e sulla progettazione concettuale. Nella lezione successiva si approfondirà la **Progettazione Logica**, dove si vedrà come il diagramma ER verrà tradotto in uno schema relazionale per l'implementazione nel database.
