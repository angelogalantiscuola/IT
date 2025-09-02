# Mappa Concettuale: Contesto e Qualità del Codice

Questa mappa mostra come, una volta costruito un sistema a oggetti, ci si assicura che funzioni correttamente (Qualità) e si definisce come può essere usato da altri (Contesto).

```mermaid
graph TD
    A[Software a Oggetti] --> B[Qualità del Codice];
    A --> C[Contesto Legale e Collaborativo];

    subgraph Qualità
        B --> B1[Testing Automatico];
        B1 --> B2["Testing degli Oggetti con <code>pytest</code>"];
        B2 --> B3["Test del Costruttore (Stato Iniziale)"];
        B2 --> B4["Test dei Metodi (Modifiche di Stato)"];
        B2 --> B5["Test delle Properties (Validazione)"];
    end

    subgraph Contesto
        C --> C1[Proprietà Intellettuale];
        C1 --> C2[Licenze Software];
        C2 --> C3["Open Source vs. Proprietario"];
        C3 --> C4["Permissive (MIT) vs. Copyleft (GPL)"];
    end

```