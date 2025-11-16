## WSGI e ASGI: Il Ponte tra Server e Applicazione Python <!-- omit in toc -->

- [Il Problema: Come parlano un Web Server e un'App Python?](#il-problema-come-parlano-un-web-server-e-unapp-python)
- [WSGI: Web Server Gateway Interface](#wsgi-web-server-gateway-interface)
- [ASGI: Asynchronous Server Gateway Interface](#asgi-asynchronous-server-gateway-interface)

### Il Problema: Come parlano un Web Server e un'App Python?

Quando un utente visita un sito web, la richiesta HTTP non arriva direttamente alla nostra applicazione Flask. Arriva prima a un **Web Server** (come Nginx o Apache), un software specializzato nel gestire connessioni di rete in modo efficiente.

Il Web Server, però, non sa come eseguire codice Python. La nostra applicazione Flask, d'altra parte, sa come gestire le route e generare risposte, ma non è ottimizzata per gestire migliaia di connessioni di rete contemporaneamente.

Serve quindi uno **standard di comunicazione**, un "traduttore" che faccia da ponte tra i due.

### WSGI: Web Server Gateway Interface

**WSGI (Web Server Gateway Interface)** è lo standard storico e più diffuso nel mondo Python per la comunicazione tra un web server e un'applicazione web **sincrona**.

Definisce un'interfaccia semplice: il web server invoca un "callable" (una funzione o un oggetto) fornito dall'applicazione, passandole i dettagli della richiesta. L'applicazione processa la richiesta e restituisce la risposta.

- **Analogia**: Pensa a una presa elettrica standard. Qualsiasi elettrodomestico (l'applicazione Python) con la spina giusta (l'interfaccia WSGI) può collegarsi a qualsiasi muro (il web server).

**Gunicorn**, che useremo per il deployment, è un esempio di **Server WSGI**. Prende le richieste dal web server e le passa alla nostra applicazione Flask.

### ASGI: Asynchronous Server Gateway Interface

Con la crescente popolarità della programmazione **asincrona**, WSGI ha mostrato i suoi limiti: era stato progettato per un modello sincrono "una richiesta, una risposta".

**ASGI (Asynchronous Server Gateway Interface)** è il successore spirituale di WSGI. È uno standard progettato per gestire applicazioni Python **asincrone**.

I principali vantaggi di ASGI sono:

- **Supporto Nativo per `async/await`**: Permette di gestire un gran numero di connessioni I/O in modo molto efficiente, ideale per applicazioni che fanno molte chiamate a database o API esterne.
- **Supporto per Protocolli a Lunga Durata**: Oltre a HTTP, può gestire protocolli come i **WebSockets**, usati per comunicazioni bidirezionali in tempo reale (es. chat, notifiche live).

Framework moderni come **FastAPI** e **Starlette** sono basati su ASGI. **Uvicorn** è il server ASGI più comune.

**In sintesi**:

- **WSGI** è lo standard per le applicazioni **sincrone** (come Flask di base).
- **ASGI** è lo standard per le applicazioni **asincrone** (come FastAPI).
