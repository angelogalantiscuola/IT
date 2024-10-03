## Analisi dei Requisiti  <!-- omit in toc -->

- [Comunicazione con il committente](#comunicazione-con-il-committente)
- [Obiettivi dell'analisi dei requisiti](#obiettivi-dellanalisi-dei-requisiti)
- [Identificazione delle entità e relazioni](#identificazione-delle-entità-e-relazioni)


L'**analisi dei requisiti** è la prima e fondamentale fase della progettazione di un database. In questa fase, l'obiettivo è comprendere in modo dettagliato le necessità del committente e tradurle in specifiche tecniche per il database. Non si tratta solo di raccogliere informazioni, ma di interpretarle correttamente e organizzare una visione chiara e strutturata delle funzionalità richieste.

### Comunicazione con il committente

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

### Identificazione delle entità e relazioni

Una volta compresi i requisiti, il passo successivo è identificare le **entità** (oggetti principali del sistema) e le **relazioni** tra di esse. Questa fase è cruciale per passare alla progettazione concettuale.

- **Entità**: sono oggetti rilevanti per il sistema, come "Libro", "Utente", "Autore".
- **Relazioni**: descrivono come le entità sono collegate tra loro. Ad esempio, un utente può prendere in prestito più libri (relazione "prestito").

La sfida in questa fase è assicurarsi che tutte le entità e le relazioni riflettano accuratamente i processi aziendali. Un errore comune è quello di identificare troppe o troppo poche entità. Un approccio iterativo, in cui le specifiche vengono riviste e affinate, può aiutare a evitare questo problema.

