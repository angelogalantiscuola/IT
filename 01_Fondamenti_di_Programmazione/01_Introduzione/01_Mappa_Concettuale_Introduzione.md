# Mappa Concettuale: Fondamenti e Modelli Mentali

```mermaid
flowchart LR
    subgraph S1 ["1. Memoria e Dati"]
        direction TB
        V_PRIM["Variabili: int, float, str, bool"] --> RULES["Regole Nomi: snake_case, no spazi o accenti"]
        RULES --> TYPE["Type Hinting esplicito"]
        TYPE --> LIST_B["Liste a scomparti indicizzati"]
    end

    subgraph S2 ["2. Struttura e Controllo del Flusso"]
        direction TB
        INDENT["Indentazione a 4 spazi: definisce i blocchi"] --> COND["Decisioni: if / elif / else"]
        COND --> FOR_L["Ciclo for su collezioni"]
        FOR_L --> WHILE_L["Ciclo while condizionale"]
    end

    subgraph S3 ["3. Modello I-E-O"]
        direction TB
        INP["Input utente con casting"] --> ELAB["Elaborazione & Trasformazione"]
        ELAB --> OUT["Output formattato con f-string"]
    end

    subgraph S4 ["4. Documentazione e Ricerca"]
        direction TB
        DOCS["W3Schools Python: guida a comandi e metodi"]
    end

    S1 --> S2 --> S3
    S4 -.-> S1
    S4 -.-> S2
```