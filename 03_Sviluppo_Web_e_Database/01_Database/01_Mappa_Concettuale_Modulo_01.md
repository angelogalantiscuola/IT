# Mappa Concettuale: Fondamenti e Progettazione di Database Relazionali

Questa mappa illustra il percorso logico del modulo, partendo dai concetti teorici fino alla progettazione e all'interazione pratica con un database.

```mermaid
graph TD
    A[Database Relazionali] --> B[Perché e Come?];
    A --> C[Progettazione];
    A --> D[Interazione e Sicurezza];

    subgraph "Teoria di Base"
        B --> B1[Concetti Fondamentali<br>DB, DBMS];
        B --> B2[Modello Relazionale<br>Tabelle, Chiavi, Vincoli];
    end

    subgraph "Dal Requisito allo Schema"
        C --> C1[Analisi dei Requisiti];
        C1 --> C2[Diagramma Entità-Relazione];
        C2 --> C3[Normalizzazione<br>1NF, 2NF, 3NF];
        C3 --> C4[Schema Logico];
    end

    subgraph "Dal Progetto al Codice"
        D --> D1[SQL DDL<br>CREATE TABLE];
        D1 --> D2[SQL DML<br>CRUD & SELECT];
        D2 --> D3[JOIN<br>Combinare Dati];
        D3 --> D4[Principi di Sicurezza<br>Utenti, Permessi, SQL Injection];
    end

    C4 -.-> D1;