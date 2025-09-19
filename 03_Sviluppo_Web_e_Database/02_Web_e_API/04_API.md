## API: Application Programming Interface <!-- omit in toc -->

- [Cos'è un'Interfaccia?](#cosè-uninterfaccia)
- [Cos'è un'API?](#cosè-unapi)
- [Cos'è una Web API?](#cosè-una-web-api)
- [Analogia: Il Ristorante](#analogia-il-ristorante)

### Cos'è un'Interfaccia?

In informatica, un'**interfaccia** è un punto di contatto, un confine condiviso attraverso il quale due o più componenti separati di un sistema si scambiano informazioni. L'interfaccia definisce le regole di questa interazione.

_Esempio_: Il volante, i pedali e il cambio sono l'**interfaccia** tra te (il pilota) e il motore dell'auto. Non hai bisogno di sapere come funziona il motore, ma sai che premendo l'acceleratore l'auto andrà più veloce.

### Cos'è un'API?

Un'**API (Application Programming Interface)** è un'interfaccia specificamente progettata per permettere a due **applicazioni software** di comunicare tra loro. Definisce un insieme di regole, protocolli e strumenti per costruire software e applicazioni.

Un'API espone delle funzionalità di un'applicazione in modo controllato, permettendo ad altre applicazioni di usarle senza conoscere i dettagli della sua implementazione interna.

_Esempio_: Quando usi un'app di meteo sul tuo telefono, l'app non contiene tutti i dati meteorologici del mondo. Invece, utilizza l'**API** di un servizio meteorologico per richiedere i dati di una specifica città. L'app sa _come chiedere_ i dati (le regole dell'API), ma non sa _come il servizio li calcola o li archivia_.

### Cos'è una Web API?

Una **Web API** è un'API accessibile tramite il web, che utilizza il protocollo **HTTP**. È l'interfaccia che permette la comunicazione tra client e server su Internet.

Quando parliamo di sviluppo web moderno, quasi sempre ci riferiamo a Web API. Queste API permettono a un'applicazione frontend (es. un sito in JavaScript o un'app mobile) di interagire con la logica e i dati che risiedono su un server backend.

### Analogia: Il Ristorante

Questa è l'analogia più famosa per spiegare una Web API:

- **Tu (il Cliente)**: Sei il **client**, l'applicazione che ha bisogno di un servizio (il cibo).
- **La Cucina**: È il **server**, il sistema che possiede le risorse (gli ingredienti) e la logica per preparare il piatto.
- **Il Cameriere**: È l'**API**.
  - Tu non vai in cucina a prepararti il cibo.
  - Consulti il **menu (la documentazione dell'API)**, che ti dice quali piatti sono disponibili e come ordinarli.
  - Fai una **richiesta (richiesta HTTP)** al cameriere in un formato che lui capisce.
  - Il cameriere (API) porta la tua richiesta alla cucina (server).
  - La cucina prepara il piatto e lo affida al cameriere.
  - Il cameriere (API) ti porta la **risposta (risposta HTTP)** con il tuo piatto (i dati in formato JSON, HTML, etc.).

L'API è l'intermediario che definisce le regole per una comunicazione ordinata ed efficiente tra client e server.
