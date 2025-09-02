# Piano di Lavoro: Modulo 05 - Contesto e Qualità del Codice

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Capacità di progettare e implementare un sistema di classi interconnesse.
*   Conoscenza di base di `pytest` dal corso del terzo anno.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Scrivere unit test con `pytest` per verificare il comportamento di classi e oggetti.
*   Testare lo stato di un oggetto dopo l'inizializzazione.
*   Testare che i metodi di un oggetto modifichino correttamente il suo stato.
*   Testare che i setter con logica di validazione si comportino come previsto.
*   Spiegare lo scopo di una licenza software e distinguere tra software libero e proprietario.
*   Riconoscere le caratteristiche delle principali licenze open-source (MIT, GPL).

## 2. Contenuti Teorici
Questo modulo unisce pratica di testing e cultura informatica.

*   **Lezione 01:** `02_Testare_gli_Oggetti.md`
    *   **Argomenti:** Riepilogo di `pytest`. Come si applica il testing alla OOP: testare il costruttore, testare i metodi che modificano lo stato, testare le properties e i loro vincoli.
*   **Lezione 02:** `03_Le_Licenze_Software.md`
    *   **Argomenti:** Il concetto di proprietà intellettuale nel software. Differenza tra licenze permissive (MIT) e copyleft (GPL). L'importanza di scegliere una licenza per i propri progetti.

## 3. Attività Pratiche / Esercitazioni

*   **Laboratorio di Testing su OOP:** Applicheremo i principi del testing direttamente alle classi del nostro RPG (`Personaggio`, `Nemico`, `Inventario`) sviluppate nei moduli precedenti.
*   **Esercizio Individuale:** `Esercizi/07_Testiamo_il_nostro_Eroe.md`. Gli studenti scriveranno una suite di test completa per la loro classe `Personaggio`, coprendo i vari aspetti del suo comportamento.
*   **Ricerca e Discussione:** "Se doveste pubblicare il vostro gioco come progetto open-source, quale licenza scegliereste e perché?".

## 4. Metodologie di Valutazione

*   **Correzione Esercizi:** L'esercizio di testing verrà valutato per la completezza dei casi di test identificati e la corretta implementazione degli `assert`.
*   **Partecipazione alla Discussione:** La partecipazione attiva alla discussione sulle licenze software sarà considerata parte della valutazione formativa.

## 5. Strumenti Necessari

*   `pytest` installato nell'ambiente virtuale del progetto.