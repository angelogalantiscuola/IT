# Mappa Concettuale: Logica di Programmazione e Manipolazione Dati

Questa mappa delinea il percorso che seguiremo per imparare a "pensare da programmatori", trasformando problemi reali in soluzioni software attraverso la manipolazione efficace dei dati.

```mermaid
graph TD
    A[Problem<br>Solving] --> B[Scomporre<br>il Problema];
    A --> C[Scegliere la<br>Struttura Dati];
    C --> C1[Lista];
    C --> C2[Dizionario];

    B --> D[Pattern di<br>Manipolazione Dati];

    D --> E[Pattern<br>su Liste];
    E --> E1[Ricerca];
    E --> E2[Filtraggio];
    E --> E3[Trasformazione<br>Mapping];
    E --> E4[Aggregazione<br>Reducing];

    D --> F[Pattern<br>su Dizionari];
    F --> F1[Conteggio<br>Frequenze];
    F --> F2[Raggruppamento<br>Dati];
    F --> F3[Indicizzazione];

    D --> G[Applicazione su<br>Dati Reali];
    G --> G1[Lettura da File<br>CSV/JSON];
    G --> G2[Creazione di<br>Report];
```