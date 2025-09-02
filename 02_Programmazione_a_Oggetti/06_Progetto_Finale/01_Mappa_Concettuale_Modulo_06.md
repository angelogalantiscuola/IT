# Mappa Concettuale: Il Ciclo di Vita del Progetto Finale

Questa mappa illustra le fasi che trasformeranno i requisiti del progetto in un'applicazione software completa e funzionante, enfatizzando l'approccio "Design-First".

```mermaid
graph TD
    A[Requisiti del Progetto RPG] --> B[Fase 1: Progettazione];
    B --> C[Fase 2: Implementazione];
    C --> D[Fase 3: Qualità e Verifica];
    D --> E[Prodotto Finale];

    subgraph Progettazione
        B --> B1[Analisi dei Requisiti];
        B1 --> B2[Creazione del Diagramma Classi UML];
        B2 --> B3(<strong>Consegna 1: Il Progetto</strong>);
    end

    subgraph Implementazione
        C --> C1[Scrittura delle Classi Python];
        C1 --> C2[Implementazione delle Relazioni];
        C2 --> C3[Sviluppo della Logica del Gioco];
    end

    subgraph Qualità
        D --> D1[Testing del Codice];
        D1 --> D2[Debug e Correzione Bug];
    end

    E --> F{Presentazione e Valutazione};

```