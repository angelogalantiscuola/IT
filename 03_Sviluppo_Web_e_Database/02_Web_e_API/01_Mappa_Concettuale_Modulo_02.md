# Mappa Concettuale: Basi dello Sviluppo Web e API REST

Questa mappa delinea i due pilastri concettuali del modulo: il protocollo di comunicazione HTTP e lo stile architetturale per l'interazione tra applicazioni API REST.

```mermaid
graph TD
    A[Sviluppo Web & API] --> B[Come Funziona il Web<br>I Protocolli];
    A --> C[Come Parlano le Applicazioni<br>Le Architetture];
    A --> D[Come si Implementa<br>Gli Strumenti];

    subgraph "Le Regole del Gioco"
        B --> B1[Modello Client-Server];
        B --> B2[Protocollo HTTP/HTTPS];
        B2 --> B3[Ciclo Richiesta-Risposta];
        B3 --> B4[Metodi GET, POST... e Status Code];
    end

    subgraph "Il Linguaggio Comune"
        C --> C1[API Application Programming Interface];
        C1 --> C2[Stile Architetturale REST];
        C2 --> C3[Risorse ed Endpoint URL];
        C2 --> C4[Formato Dati: JSON];
    end

    subgraph "La Pratica"
        D --> D1[Client Python<br>Libreria `requests`];
        D --> D2[Server Python<br>WSGI / ASGI];
        D --> D3[Introduzione ai<br>Web Framework];
    end

    B --- C;
    C --- D;
```
