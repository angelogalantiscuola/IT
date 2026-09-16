# Piano di Lavoro: Modulo 05 - Progetto Finale (Approccio Design-First)

## 1. Obiettivi di Apprendimento

### Prerequisiti
- Moduli da 00 a 04 completati (C4 Model, User Stories, modellazione ER e UML, sequenza, dataclass, relazioni 1:1, 1:N, N:N, ereditarietà, persistenza JSON e Pytest).

### Competenze in Uscita
Al termine di questo modulo conclusivo, lo studente sarà in grado di:
- Gestire un progetto software complesso dall'analisi dei requisiti al rilascio collaudato.
- Documentare l'architettura macro con il **C4 Model** (Livello 1 e 2).
- Formalizzare le specifiche con **User Stories** e criteri di accettazione rigorosi.
- Progettare la struttura statica dei dati producendo in parallelo il **Diagramma ER** e il **Diagramma delle Classi UML**.
- Modellare la dinamica temporale producendo un **Diagramma di Sequenza per ciascuna User Story**.
- Ricavare i metodi operativi dalle frecce di sequenza senza ambiguità.
- Implementare il backend in Python moderno con `@dataclass`, relazioni tra oggetti e serializzazione **JSON**.
- Collaudare l'intero sistema con una suite di test **Pytest** che copre ogni User Story.
- Garantire la qualità del codice tramite **Ruff**.

---

## 2. Articolazione del Modulo

- **Lezione 01:** `01_Mappa_Concettuale_Modulo_05.md`
- **Lezione 02:** `02_Progetto_Faro_Fase_1_Requisiti_e_C4.md` (Requisiti, C4 Context L1, C4 Container L2, 4 User Stories).
- **Lezione 03:** `03_Progetto_Faro_Fase_2_Modellazione_ER_UML.md` (Diagramma ER completo con PK/FK + Class Diagram UML).
- **Lezione 04:** `04_Progetto_Faro_Fase_3_Tutte_le_Sequenze.md` (Tutti i 4 Diagrammi di Sequenza con nascita dei metodi).
- **Lezione 05:** `05_Progetto_Faro_Fase_4_Codice_e_Pytest.md` (Codice Python completo, modulo persistenza JSON e suite Pytest).
- **Lezione 06:** `06_Il_Tuo_Progetto_Tracce_e_Checklist.md` (La checklist di consegna, le 3 tracce assegnabili e la rubrica di valutazione).

---

## 3. Metodologie di Valutazione
- Valutazione della coerenza tra le User Stories, i Diagrammi di Sequenza, i metodi delle classi e i test di collaudo.
- Esecuzione di `pytest` (100% superati) e analisi statica con `ruff check .`.