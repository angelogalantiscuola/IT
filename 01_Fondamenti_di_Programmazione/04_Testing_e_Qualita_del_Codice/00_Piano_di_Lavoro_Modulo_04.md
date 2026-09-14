# Piano di Lavoro: Modulo 04 - Testing, Verifica e Code Review

## 1. Obiettivi di Apprendimento

### Prerequisiti
- Modulo 03 completato (funzioni pure con `return`, contratti, `venv` e `pip`).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
- Comprendere i limiti del testing manuale (`print`) e i vantaggi del collaudo automatico.
- Costruire una **Matrice dei Casi di Prova** (casi normali, casi limite e casi anomali).
- Installare **`pytest`** all'interno dell'ambiente virtuale (`.venv`) del progetto.
- Scrivere unit test chiari usando l'istruzione **`assert`** e le convenzioni standard (`test_*.py`).
- Eseguire i test da terminale e interpretare il report di fallimento (*Traceback* e differenze tra valore atteso ed effettivo).
- **Code Review:** Analizzare codice prodotto da colleghi o generato da un'IA, individuando allucinazioni, errori sui valori limite o alterazioni accidentali dei dati di partenza.

---

## 2. Contenuti Teorici e Metodologici

- **Lezione 01:** `01_Mappa_Concettuale_Testing.md`
- **Lezione 02:** `02_La_Matrice_dei_Casi_di_Prova.md` (Pensiero analitico: definire input, output e casi limite prima del codice).
- **Lezione 03:** `03_Unit_Testing_con_Pytest.md` (Setup, convenzioni, scrittura dei test con `assert`, esecuzione e debug).
- **Lezione 04:** `04_Laboratorio_Code_Review.md` (Il Detective in azione: confrontare 3 implementazioni e scovare i bug nascosti).

---

## 3. Metodologie di Valutazione
- Capacità di individuare i casi limite significativi per una data funzione (es. lista vuota, valori negativi, zeri).
- Correttezza della suite di test scritta con `pytest` per verificare un modulo software.
- Esercizio di Code Review: individuare e spiegare a voce o per iscritto perché uno snippet di codice fallisce su determinati casi limite.