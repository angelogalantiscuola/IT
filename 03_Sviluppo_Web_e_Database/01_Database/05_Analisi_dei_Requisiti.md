## Analisi dei Requisiti <!-- omit in toc -->

- [Obiettivi dell'Analisi dei Requisiti](#obiettivi-dellanalisi-dei-requisiti)
- [Identificazione di Entità e Relazioni](#identificazione-di-entità-e-relazioni)

L'**analisi dei requisiti** è la prima e fondamentale fase della progettazione di un database. L'obiettivo è comprendere in modo dettagliato le necessità del committente e tradurle in specifiche tecniche. Non si tratta solo di raccogliere informazioni, ma di interpretarle correttamente per costruire una visione chiara del sistema da realizzare.

### Obiettivi dell'Analisi dei Requisiti

1.  **Identificare i dati chiave**: Quali informazioni devono essere memorizzate?

    - _Esempio_: Per un sistema di gestione di una biblioteca, i dati chiave includono libri, utenti, prestiti, autori.

2.  **Comprendere i processi**: Quali operazioni devono essere eseguite sui dati?

    - _Esempio_: Un utente deve poter prendere in prestito un libro, restituirlo o cercare nel catalogo.

3.  **Definire vincoli e regole**: Quali restrizioni devono essere applicate?
    - _Esempio_: Un utente non può prendere in prestito più di cinque libri contemporaneamente.

### Identificazione di Entità e Relazioni

Una volta compresi i requisiti, il passo successivo è identificare le **entità** (gli oggetti principali del sistema) e le **relazioni** tra di esse. Questa fase è cruciale per passare alla progettazione concettuale.

- **Entità**: Sono i "sostantivi" importanti del nostro sistema. Rappresentano oggetti o concetti rilevanti, come "Libro", "Utente", "Autore".
- **Relazioni**: Descrivono come le entità sono collegate tra loro. Sono i "verbi" che legano le entità. Ad esempio, un `Utente` **prende in prestito** un `Libro`.

La sfida in questa fase è assicurarsi che tutte le entità e le relazioni riflettano accuratamente i processi reali. Un errore comune è quello di identificare troppe o troppo poche entità. Un approccio iterativo, in cui le specifiche vengono riviste e affinate, è spesso la soluzione migliore.
