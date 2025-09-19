## REST: Lo Stile Architetturale per le Web API <!-- omit in toc -->

- [Cos'è REST?](#cosè-rest)
- [I Principi Fondamentali di REST](#i-principi-fondamentali-di-rest)
- [REST in Pratica: Risorse, Verbi e Nomi](#rest-in-pratica-risorse-verbi-e-nomi)
- [RESTful API](#restful-api)

### Cos'è REST?

**REST (REpresentational State Transfer)** non è un protocollo o uno standard, ma uno **stile architetturale** per la progettazione di sistemi in rete, come le Web API. Definisce un insieme di vincoli e principi che, se seguiti, portano a sistemi scalabili, manutenibili e facili da usare.

L'idea centrale è che la comunicazione tra client e server avvenga tramite lo scambio di **rappresentazioni** dello stato delle **risorse**.

### I Principi Fondamentali di REST

1.  **Client-Server**: Il client e il server sono separati e indipendenti. Il client si occupa dell'interfaccia utente, il server della gestione dei dati.
2.  **Stateless (Senza Stato)**: Ogni richiesta dal client al server deve contenere tutte le informazioni necessarie per essere compresa. Il server non memorizza lo stato del client tra una richiesta e l'altra.
3.  **Cacheable**: Le risposte del server dovrebbero indicare se possono essere messe in cache dal client. La cache migliora le prestazioni riducendo la necessità di richieste ripetute.
4.  **Uniform Interface (Interfaccia Uniforme)**: Questo è il principio chiave di REST e si basa su quattro pilastri:
    - **Identificazione delle Risorse**: Ogni risorsa è identificata in modo univoco da un URI (Uniform Resource Identifier), come un URL. Esempio: `/utenti/123`.
    - **Manipolazione tramite Rappresentazioni**: Il client non interagisce direttamente con la risorsa sul server, ma con una sua _rappresentazione_ (es. un documento JSON o XML).
    - **Messaggi Auto-Descrittivi**: Ogni messaggio (richiesta/risposta) contiene abbastanza informazioni per descrivere come essere processato (es. l'header `Content-Type: application/json` dice al server di interpretare il body come JSON).
    - **HATEOAS (Hypermedia as the Engine of Application State)**: Le risposte del server dovrebbero includere link (hypermedia) che guidano il client sulle prossime azioni possibili (es. una risposta su un utente potrebbe contenere il link per visualizzare i suoi ordini).

### REST in Pratica: Risorse, Verbi e Nomi

L'architettura REST si sposa perfettamente con il protocollo HTTP.

- **Le Risorse sono i Nomi (Sostantivi)**: Gli URL dovrebbero identificare le risorse in modo intuitivo. Si usano sostantivi al plurale.
  - Corretto: `/utenti`, `/ordini/789`
  - Sbagliato: `/getUtenti`, `/creaOrdine`
- **I Metodi HTTP sono le Azioni (Verbi)**: L'azione da compiere sulla risorsa è definita dal metodo HTTP.
  - `GET /utenti`: Ottieni la lista di tutti gli utenti.
  - `GET /utenti/123`: Ottieni i dettagli dell'utente con ID 123.
  - `POST /utenti`: Crea un nuovo utente.
  - `PUT /utenti/123`: Sostituisci/aggiorna l'utente con ID 123.
  - `DELETE /utenti/123`: Elimina l'utente con ID 123.

### RESTful API

Una Web API che segue i principi e i vincoli di REST viene definita una **RESTful API**. È l'approccio più diffuso e consolidato per la progettazione di API web.
