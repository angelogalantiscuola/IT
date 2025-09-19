## Endpoint: Le Porte di Accesso di un'API <!-- omit in toc -->

- [Cos'è un Endpoint?](#cosè-un-endpoint)
- [Anatomia di un Endpoint](#anatomia-di-un-endpoint)
- [Esempi Pratici](#esempi-pratici)

### Cos'è un Endpoint?

Nel contesto di una Web API, un **endpoint** è un URL specifico dove un'API può essere raggiunta da un'applicazione client. È il punto di contatto, l'indirizzo a cui inviare una richiesta per interagire con una specifica risorsa o un insieme di risorse.

Se l'API è il "cameriere", gli endpoint sono le singole voci sul "menu" a cui il cameriere sa come rispondere.

### Anatomia di un Endpoint

Un endpoint combina due elementi che abbiamo già visto:

1.  **L'URL della Risorsa**: Il "sostantivo" che identifica a cosa vogliamo accedere.
2.  **Il Metodo HTTP**: Il "verbo" che definisce l'azione che vogliamo compiere.

La combinazione di `Metodo + URL` definisce un'operazione unica.

- `GET /utenti` è un endpoint.
- `POST /utenti` è un altro endpoint, diverso dal primo, anche se condividono lo stesso URL.

### Esempi Pratici

Consideriamo un'API RESTful per la gestione di un blog. Ecco alcuni dei suoi possibili endpoint:

- **Ottenere tutti gli articoli**

  - **Endpoint**: `GET /articoli`
  - **Azione**: Richiede una lista di tutti gli articoli del blog.

- **Ottenere un singolo articolo**

  - **Endpoint**: `GET /articoli/123`
  - **Azione**: Richiede i dettagli dell'articolo con ID 123.

- **Creare un nuovo articolo**

  - **Endpoint**: `POST /articoli`
  - **Azione**: Invia i dati di un nuovo articolo (titolo, contenuto) nel corpo della richiesta per crearlo.

- **Aggiornare un articolo esistente**

  - **Endpoint**: `PUT /articoli/123`
  - **Azione**: Sostituisce i dati dell'articolo con ID 123 con quelli nuovi inviati nel corpo della richiesta.

- **Eliminare un articolo**

  - **Endpoint**: `DELETE /articoli/123`
  - **Azione**: Rimuove l'articolo con ID 123.

- **Ottenere i commenti di un articolo** (esempio di risorsa nidificata)
  - **Endpoint**: `GET /articoli/123/commenti`
  - **Azione**: Richiede la lista di tutti i commenti associati all'articolo con ID 123.

La progettazione di un'API consiste in gran parte nella definizione di un insieme di endpoint chiari, intuitivi e coerenti.
