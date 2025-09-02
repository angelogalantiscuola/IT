# Mappa Concettuale: Deployment e Progetto Finale

Questa mappa rappresenta il culmine del percorso di studi, illustrando il ciclo di vita completo di un progetto software: dall'ideazione alla pubblicazione nel mondo reale.

```mermaid
graph TD
    A[Requisiti del<br>Progetto Finale] --> B[Fase 1: Progettazione  Design ];
    B --> C[Fase 2: Sviluppo  Development ];
    C --> D[Fase 3: Qualità  Testing ];
    D --> E[Fase 4: Rilascio  Deployment ];
    E --> F[Applicazione Web<br><strong>Live!</strong>];

    subgraph "Il Progetto su Carta"
        B --> B1[Analisi dei Requisiti];
        B1 --> B2[Diagramma ER<br> Modello Dati ];
        B1 --> B3[Diagramma Classi UML<br> Modello Oggetti ];
    end

    subgraph "Il Codice"
        C --> C1[Implementazione<br>Flask & SQLModel];
        C1 --> C2[Architettura<br>con Blueprints];
    end

    subgraph "La Rete di Sicurezza"
        D --> D1[Scrittura Test<br>con <code>pytest-flask</code>];
        D1 --> D2[Unit & Integration Tests];
    end

    subgraph "Dal Locale al Globale"
        E --> E1[Configurazione per Produzione<br> Variabili d'Ambiente, Gunicorn ];
        E1 --> E2[Piattaforma PaaS<br> es. Render ];
        E2 --> E3[Collegamento a GitHub<br>e Deploy Automatico];
    end

    style F fill:#2ecc71,stroke:#fff,stroke-width:2px,color:#fff