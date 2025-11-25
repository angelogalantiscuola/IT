# Mappa Concettuale: Architettura Web con Flask

Questa mappa illustra la struttura "professionale" che adotteremo fin dal primo giorno, separando la configurazione, la logica delle route e la visualizzazione.

```mermaid
graph TD
    A[Progetto Flask] --> B[Entry Point<br>run.py];
    A --> C[Package Applicativo<br>app/];

    subgraph "Configurazione (Lesson 1)"
        C --> C1[__init__.py];
        C1 --> C2[Function create_app<br>Application Factory];
    end

    subgraph "Logica di Routing (Lesson 2)"
        C --> D[Blueprints];
        D --> D1[main.py<br>Gestione Pagine Statiche];
        C2 -.->|Registra| D;
    end

    subgraph "Presentazione (Lesson 3)"
        C --> E[Templates HTML];
        E --> E1[base.html<br>Layout Comune];
        E --> E2[home.html<br>Contenuto Specifico];
        D1 -.->|Renderizza| E;
    end
```