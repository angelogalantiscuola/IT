# Piano di Lavoro: Modulo 04 - Testing e Qualità del Codice

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Completamento con successo dei Moduli 01, 02 e 03.
*   Piena padronanza della scrittura di funzioni con parametri e valori di ritorno.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Spiegare l'importanza del testing automatico rispetto a quello manuale.
*   Comprendere il concetto di "unit test".
*   Installare e configurare `pytest` in un ambiente virtuale.
*   Scrivere semplici unit test per verificare il corretto funzionamento di funzioni pure (input -> output).
*   Utilizzare l'istruzione `assert` per validare i risultati attesi.
*   Eseguire i test da terminale e interpretarne l'output (successo o fallimento).

## 2. Contenuti Teorici
Le lezioni di riferimento per questo modulo si concentreranno sull'introdurre il concetto di testing e fornire gli strumenti pratici per implementarlo.

*   **Lezione 01:** `04_Testing_e_Qualita_del_Codice/01_Mappa_Concettuale_Testing.md`
    *   *Argomento:* Visione d'insieme dei concetti del modulo.
*   **Lezione 02:** `04_Testing_e_Qualita_del_Codice/02_Perche_Scrivere_Test.md`
    *   *Argomenti:* I limiti del testing manuale (`print`), i vantaggi del testing automatico (affidabilità, prevenzione delle regressioni), introduzione alla "piramide del testing" e focus sugli unit test.
*   **Lezione 03:** `04_Testing_e_Qualita_del_Codice/03_Il_Tuo_Primo_Unit_Test_con_Pytest.md`
    *   *Argomenti:* Introduzione a `pytest` come standard de facto. Installazione con `pip`. Convenzioni di `pytest` (nomi dei file `test_*.py`, nomi delle funzioni `test_...`). Scrittura del primo test con `assert`.

## 3. Attività Pratiche / Esercitazioni
Le attività pratiche saranno mirate a sviluppare l'abilità di scrivere test per codice esistente. Questo rinforza la capacità di analisi e la comprensione della logica delle funzioni. Gli esercizi si focalizzeranno su:
*   Scrivere test per funzioni matematiche semplici (es. somma, fattoriale).
*   Testare funzioni che manipolano stringhe (es. maiuscole, concatenazione).
*   Verificare il comportamento di funzioni con diversi input, inclusi i "casi limite" (es. input vuoti, zeri).
*   Eseguire i test da terminale e correggere le funzioni originali in caso di fallimento del test.

## 4. Metodologie di Valutazione
*   Correzione degli esercizi di testing, valutando la capacità dello studente di identificare i casi di test significativi per una data funzione.
*   Una verifica pratica in cui viene fornito un piccolo modulo con alcune funzioni e si chiede di scrivere la suite di test corrispondente.
*   Inclusione del testing come requisito per la valutazione del progetto finale dell'anno.

## 5. Strumenti Necessari
*   Tutti gli strumenti configurati nel Modulo 02 (Python, VS Code, Git, venv).
*   La libreria `pytest` da installare tramite `pip` nell'ambiente virtuale del progetto.