# Mappa Concettuale: Modellazione e Oggetti

Questa mappa riassume il flusso logico del modulo: dall'idea astratta di "oggetto" fino alla sua concreta implementazione, usando UML come ponte tra il design e il codice.

```mermaid
graph TD
    A[Paradigma a Oggetti] --> B{Concetti Chiave};
    A --> C{Strumenti di Rappresentazione};

    subgraph Concetti
        B --> B1[Classe: Il Progetto];
        B --> B2[Oggetto: L'Istanza Concreta];
        B1 --> B3[Attributi: I Dati];
        B1 --> B4[Metodi: I Comportamenti];
    end

    subgraph Strumenti
        C --> C1[Testo: I Requisiti];
        C --> C2[Diagramma UML: Il Disegno Tecnico];
        C --> C3[Codice Python: L'Implementazione];
    end

    C1 -- Traduzione --> C2;
    C2 -- Traduzione --> C3;

    B3 -- Rappresentati in --> C2;
    B4 -- Rappresentati in --> C2;

    style A fill:#345,stroke:#fff,stroke-width:2px,color:#fff