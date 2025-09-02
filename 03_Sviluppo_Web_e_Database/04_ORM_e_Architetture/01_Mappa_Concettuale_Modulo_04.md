# Mappa Concettuale: Architetture Robuste e ORM

Questa mappa illustra il passaggio da un'applicazione web monolitica a una struttura professionale, separando le responsabilità logiche e astraendo l'accesso al database.

```mermaid
graph TD
    A[Applicazione Monolitica<br>flask_1];
    A --> B[Necessità di Crescere<br>Manutenibilità, Scalabilità];
    B --> C[Soluzione 1: Riorganizzazione<br>del Codice];
    B --> D[Soluzione 2: Astrazione<br>del Database];

    subgraph "Architettura Modulare"
        C --> C1[Pattern: Application Factory<br><code>create_app</code>];
        C1 --> C2[Separazione delle Route<br>con <strong>Blueprints</strong>];
        C2 --> C3[Codice Organizzato per Funzione<br>auth, entries, profile];
    end

    subgraph "Object-Relational Mapping ORM"
        D --> D1[Concetto di ORM<br>Oggetti <-> Tabelle];
        D1 --> D2[Libreria <strong>SQLModel</strong>];
        D2 --> D3[Definizione dei Modelli<br><code>class UserSQLModel</code>];
        D3 --> D4[Interazione Pythonica con il DB<br><code>session.execselect...</code>];
        D4 --> D5[Gestione delle Relazioni<br><code>Relationship</code>];
    end
    
    C --> E;
    D --> E[Applicazione Professionale<br>flask_2];