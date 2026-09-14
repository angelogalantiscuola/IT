# Piano di Lavoro: Modulo 03 - Dati, Funzioni, Contratti e Modularità

## 1. Obiettivi di Apprendimento

### Prerequisiti
- Modulo 01 (variabili, if, for su liste, while) e Modulo 02 (Git, VS Code, Ruff).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
- Modellare entità complesse tramite **dizionari** e dataset tabellari tramite **liste di dizionari**.
- Progettare funzioni come **contratti software** (Type Hints, docstring, parametri, valori di ritorno puri).
- Applicare la **scomposizione Top-Down a 3 strati** (separare I/O utente, logica di calcolo pura e orchestrazione nel `main`).
- Comprendere la **mutabilità** in memoria ed evitare modifiche accidentali ai dati di partenza (*side-effects*).
- Gestire errori e imprevisti in modo controllato tramite blocchi `try...except...finally`.
- Salvare e leggere dati strutturati su file **JSON** e **CSV**.
- Organizzare il codice in **moduli** e **package**, installare librerie con **`pip`** e gestire l'ambiente isolato con **`venv`**.

---

## 2. Contenuti Teorici e Metodologici

- **Lezione 01:** `01_Mappa_Concettuale_Modulo_03.md`
- **Lezione 02:** `02_Dizionari_e_Dati_Strutturati.md` (Dizionari, Liste di Dizionari, Type Hinting).
- **Lezione 03:** `03_Funzioni_e_Contratti_Software.md` (Firme, Docstring, Return vs Print, Top-Down).
- **Lezione 04:** `04_Metodo_di_Scomposizione_TopDown.md` (Metodologia a 3 strati: I/O, Cervello, Main).
- **Lezione 05:** `05_Mutabilita_e_Dati_Protetti.md` (Modifiche in-place, copie, rispetto dei dati originali).
- **Lezione 06:** `06_Gestione_delle_Eccezioni.md` (Try / Except / Finally).
- **Lezione 07:** `07_Gestione_dei_File.md` (Persistenza su JSON e CSV).
- **Lezione 08:** `08_Moduli_Package_Pip_e_Virtualenv.md` (Moduli, Package `__init__.py`, Pip e Venv).

---

## 3. Metodologie di Valutazione
- Valutazione della scomposizione: dato un problema reale, verificare la corretta separazione tra funzioni di I/O e funzioni di logica pura.
- Analisi del codice: assenza di `print` dentro le funzioni di calcolo e rispetto della mutabilità dei dati.
- Creazione e attivazione corretta di un ambiente virtuale `venv` con installazione di pacchetti via `pip`.