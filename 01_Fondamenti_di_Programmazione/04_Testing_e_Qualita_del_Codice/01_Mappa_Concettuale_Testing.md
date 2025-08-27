# Mappa Concettuale: Testing e Qualità del Codice

Questa mappa riassume i concetti chiave che affronteremo in questo modulo, introducendo il testing automatico come pratica fondamentale per uno sviluppatore professionista.

```mermaid
graph TD
    A[Testing del Codice] --> B[Perché Scrivere Test?];
    A --> C[Unit Test];
    A --> D[Pytest: Il Nostro Strumento];

    B --> B1[Limiti del Testing Manuale con print];
    B --> B2[Vantaggi del Testing Automatico];
    B2 --> B2a[Prevenzione delle Regressioni];
    B2 --> B2b[Documentazione Vivente];
    B2 --> B2c[Migliore Progettazione];

    C --> C1[Testare Piccole Unità Isolate];
    C1 --> C1a[Una Funzione è un'Unità Perfetta];

    D --> D1[Installazione e Configurazione];
    D --> D2[Convenzioni di Pytest];
    D --> D3[L'istruzione 'assert'];
    D --> D4[Eseguire i Test];

```