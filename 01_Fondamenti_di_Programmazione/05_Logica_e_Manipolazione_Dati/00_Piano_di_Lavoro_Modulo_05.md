# Piano di Lavoro: Modulo 05 - Logica e Manipolazione Dati

## 1. Obiettivi di Apprendimento

### Prerequisiti
- Moduli da 01 a 04 completati (variabili, cicli, liste, dizionari, funzioni a contratto, gestione file ed eccezioni, test con pytest).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
- Analizzare un problema di analisi dati del mondo reale e scomporlo in un'architettura a funzioni modulari.
- Scegliere la struttura dati più appropriata per ogni fase dell'elaborazione.
- Implementare i **4 Pattern Fondamentali sulle Liste**:
  - **Ricerca:** Individuare un record specifico in base a un criterio.
  - **Filtraggio:** Estrarre un sottoinsieme di dati senza alterare la collezione di partenza.
  - **Trasformazione (Mapping):** Creare una nuova lista trasformando o estraendo proprietà dai singoli record.
  - **Aggregazione (Reducing):** Calcolare metriche di sintesi (somme, medie, valori massimi e minimi).
- Implementare i **Pattern Avanzati con i Dizionari**:
  - **Conteggio delle frequenze:** Calcolare statistiche sulle occorrenze di categorie.
  - **Raggruppamento (Grouping):** Organizzare record sparsi in categorie tematiche.
  - **Indicizzazione rapida:** Creare dizionari indice per ricerche immediate $O(1)$ tramite ID.
- Realizzare una **Pipeline completa su Dati Reali**: lettura da file CSV/JSON $\to$ pulizia e validazione $\to$ elaborazione modulare $\to$ report finale formattato.

---

## 2. Contenuti Teorici e Metodologici

- **Lezione 01:** `01_Mappa_Concettuale_Logica.md`
- **Lezione 02:** `02_Dall_Idea_al_Codice_Problem_Solving.md` (Metodo: capire, scegliere le strutture, pianificare, codificare).
- **Lezione 03:** `03_Pattern_Comuni_su_Liste.md` (I 4 pattern: ricerca, filtro, trasformazione, aggregazione).
- **Lezione 04:** `04_Pattern_Comuni_su_Dizionari.md` (Frequenze, raggruppamento per categoria e indicizzazione).
- **Lezione 05:** `05_Lavorare_con_Dati_Strutturati.md` (La pipeline completa: da file CSV a report finale).

---

## 3. Metodologie di Valutazione
- Valutazione della qualità della scomposizione: assenza di codice monolitico e uso di funzioni specializzate con contratti chiari.
- Verifica del rispetto dei dati originali (nessun side-effect indesiderato sulle strutture in ingresso).
- Realizzazione del **Mini-Progetto di Sintesi di 3ª**: script modulare che carica un dataset reale, risponde a 3-4 quesiti di business tramite i pattern e produce un report pulito.