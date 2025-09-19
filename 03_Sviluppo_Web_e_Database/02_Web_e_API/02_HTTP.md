<file path="03_Sviluppo_Web_e_Database/02_Web_e_API/lessons/02_HTTP.md">
## Il Protocollo HTTP <!-- omit in toc -->

- [Cos'è HTTP?](#cosè-http)
- [Il Modello Client-Server](#il-modello-client-server)
- [La Struttura di un Messaggio HTTP](#la-struttura-di-un-messaggio-http)
  - [Richiesta HTTP (Request)](#richiesta-http-request)
  - [Risposta HTTP (Response)](#risposta-http-response)
- [Metodi HTTP Comuni](#metodi-http-comuni)
- [Status Code Comuni](#status-code-comuni)

### Cos'è HTTP?

**HTTP (HyperText Transfer Protocol)** è il protocollo, ovvero l'insieme di regole di comunicazione, che permette ai client (come i browser web) di richiedere e ricevere risorse (come pagine HTML, immagini, dati) dai server. È il linguaggio fondamentale del web.

Una caratteristica chiave di HTTP è di essere **stateless** (senza stato): ogni richiesta è un evento indipendente e il server non conserva alcuna informazione sulle richieste precedenti dello stesso client.

### Il Modello Client-Server

La comunicazione web si basa sul modello client-server:

1.  Il **Client** (es. il tuo browser) inizia la comunicazione inviando una **richiesta HTTP** a un server per ottenere una risorsa.
2.  Il **Server** (es. un server web che ospita un sito) riceve la richiesta, la elabora e invia indietro una **risposta HTTP**, che contiene la risorsa richiesta o un messaggio di errore.

### La Struttura di un Messaggio HTTP

Sia le richieste che le risposte seguono una struttura simile, composta da:

1.  **Start-Line**: La prima riga, che definisce il tipo di messaggio.
2.  **Headers**: Coppie chiave-valore che forniscono metadati sulla richiesta/risposta.
3.  **Body (Corpo)**: Contiene i dati effettivi (opzionale).

#### Richiesta HTTP (Request)

- **Start-Line**: Contiene il **metodo HTTP**, l'**URL** della risorsa e la **versione di HTTP**.
  `GET /utenti/123 HTTP/1.1`
- **Headers**: Informazioni aggiuntive.
  - `Host: api.esempio.com` (il dominio del server)
  - `Accept: application/json` (il formato di dati che il client si aspetta di ricevere)
- **Body**: I dati inviati al server, ad esempio con una richiesta `POST`.

#### Risposta HTTP (Response)

- **Start-Line (Status-Line)**: Contiene la **versione di HTTP**, uno **status code** e un **messaggio di stato**.
  `HTTP/1.1 200 OK`
- **Headers**:
  - `Content-Type: application/json` (il formato dei dati nel corpo della risposta)
  - `Content-Length: 150` (la dimensione del corpo)
- **Body**: I dati richiesti (es. il JSON di un utente, il codice HTML di una pagina).

### Metodi HTTP Comuni

I metodi HTTP (o "verbi") specificano l'azione che il client desidera eseguire sulla risorsa. I più importanti sono:

- **`GET`**: Richiede una rappresentazione della risorsa specificata. È usato per **leggere** dati.
- **`POST`**: Invia dati a un server per **creare** una nuova risorsa.
- **`PUT`**: **Sostituisce** completamente una risorsa esistente con i dati forniti.
- **`PATCH`**: Applica modifiche **parziali** a una risorsa.
- **`DELETE`**: **Rimuove** la risorsa specificata.

### Status Code Comuni

Gli status code indicano l'esito della richiesta. Sono raggruppati in categorie:

- **2xx (Successo)**
  - `200 OK`: La richiesta è andata a buon fine.
  - `201 Created`: La richiesta è andata a buon fine e una nuova risorsa è stata creata (usato in risposta a `POST`).
- **3xx (Redirezione)**
  - `302 Found`: La risorsa è stata temporaneamente spostata a un altro URL.
- **4xx (Errori del Client)**
  - `400 Bad Request`: Il server non può elaborare la richiesta a causa di un errore del client (es. sintassi errata).
  - `401 Unauthorized`: È richiesta l'autenticazione.
  - `403 Forbidden`: Il client non ha i permessi per accedere alla risorsa.
  - `404 Not Found`: La risorsa richiesta non è stata trovata.
- **5xx (Errori del Server)**
  - `500 Internal Server Error`: Si è verificato un errore generico sul server.
