# Piano di Lavoro: Modulo 01 - Fondamenti e Progettazione di Database Relazionali

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Piena padronanza dei concetti di Programmazione Orientata agli Oggetti (classi, oggetti, relazioni) del quarto anno.
*   Capacità di analizzare un problema e scomporlo in entità logiche.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Spiegare il ruolo e le funzioni principali di un Sistema di Gestione di Database (DBMS).
*   Comprendere e applicare i concetti del modello relazionale: entità, attributi, chiavi primarie ed esterne, e vincoli di integrità.
*   Analizzare un insieme di requisiti testuali e tradurli in un modello di dati formale attraverso un Diagramma Entità-Relazione (ER).
*   Applicare i principi della normalizzazione (fino alla Terza Forma Normale) per progettare uno schema di database efficiente e privo di ridondanze.
*   Tradurre un diagramma ER in codice SQL DDL (`CREATE TABLE`) per creare la struttura fisica del database.
*   Scrivere query SQL DML per manipolare i dati (CRUD: `INSERT`, `SELECT`, `UPDATE`, `DELETE`).
*   Eseguire interrogazioni complesse sui dati combinando più tabelle con le `JOIN`.
*   Comprendere i principi fondamentali della sicurezza dei database e il rischio di attacchi come la SQL Injection.

## 2. Contenuti Teorici
Le lezioni di questo modulo costruiscono una solida base teorica e pratica per tutto ciò che riguarda i dati. Il percorso logico è il seguente:

1.  **Introduzione**:
    *   `02_Fondamenti_di_Database.md`: Cos'è un database e perché è fondamentale.
    *   `03_DBMS.md`: Il ruolo e le responsabilità del DBMS (ACID, concorrenza, sicurezza).

2.  **Progettazione del Database (Design-First)**:
    *   `04_Progettazione_del_Database.md`: Panoramica delle fasi di progettazione.
    *   `05_Analisi_dei_Requisiti.md`: Come raccogliere e analizzare le necessità.
    *   `06_Diagrammi_ER.md`: Modellazione concettuale con i diagrammi Entità-Relazione.
    *   `07_Normalizzazione.md`: Eliminare le ridondanze e migliorare l'integrità.
    *   `06a_Da_ER_a_SQL_La_Guida_Pratica.md`: Dallo schema ER allo schema relazionale.

3.  **Il Modello Relazionale**:
    *   `08_Modello_Relazionale.md`: Tabelle, tuple e attributi.
    *   `09_Chiavi_Primaria_Esterna.md`: Le colonne che creano le relazioni.
    *   `10_Vincoli_di_Integrita.md`: Le regole che garantiscono la coerenza dei dati.

4.  **Interrogazione e Manipolazione (SQL)**:
    *   `11_SQL.md`: Il linguaggio per parlare con i database (DDL, DML, `SELECT`, `WHERE`, `GROUP BY`, `JOIN`).
    *   `12_SQL_in_Python.md`: Come eseguire query SQL da un'applicazione Python.

5.  **Sicurezza**:
    *   `14_Nozioni_di_Sicurezza.md`: Panoramica delle principali minacce e contromisure.
    *   `15_Gestione_Utenti_Permessi.md`: Controllare chi può fare cosa.
    *   `16_SQL_Injection.md`: Conoscere e prevenire una delle vulnerabilità più critiche.

## 3. Attività Pratiche / Esercitazioni

*   **Laboratorio di Progettazione**: Agli studenti verranno forniti scenari testuali (es. "un sistema per una biblioteca", "una semplice app di social network") e dovranno produrre i diagrammi ER corrispondenti.
*   **Laboratorio SQL**: Utilizzando un database pre-popolato (come `music-store.sql`), gli studenti dovranno scrivere una serie di query di difficoltà crescente per estrarre informazioni specifiche, consolidando la loro comprensione di `SELECT`, `WHERE`, `JOIN` e `GROUP BY`.
*   **Mini-Progetto**: Progettare (ER), creare (SQL DDL) e popolare (SQL `INSERT`) un piccolo database per un'applicazione a scelta (es. gestione voti scolastici, collezione di videogiochi).

## 4. Metodologie di Valutazione

*   Correzione e valutazione dei diagrammi ER prodotti.
*   Verifica pratica di SQL: data una base di dati, lo studente deve scrivere query per rispondere a una serie di domande.
*   Valutazione del mini-progetto completo, sia per la qualità del design che per la correttezza dell'implementazione SQL.

## 5. Strumenti Necessari

*   Un RDBMS installato localmente (es. **MariaDB** o PostgreSQL).
*   Un client per database, preferibilmente l'estensione **SQLTools per VS Code** per mantenere un ambiente di sviluppo integrato.
*   Un editor di testo con supporto Mermaid per la creazione dei diagrammi ER.
