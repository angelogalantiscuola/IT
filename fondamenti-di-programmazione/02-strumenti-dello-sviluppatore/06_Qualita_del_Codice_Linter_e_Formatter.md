# Qualità del Codice: Linter e Formatter

Scrivere codice che funziona è solo metà del lavoro. Scrivere codice **pulito, leggibile e coerente** è fondamentale per poterci lavorare in futuro e per collaborare con altri. Due strumenti essenziali ci aiutano in questo: i linter e i formatter.

## 1. Il Linter: Il Correttore Ortografico del Codice

Un **linter** è uno strumento che analizza il codice sorgente per trovare errori di programmazione, bug, errori stilistici e costrutti sospetti.

*   **Analogia**: Pensa al linter come al correttore ortografico e grammaticale di un editor di testo. Ti sottolinea in rosso gli errori di battitura o le frasi costruite male.

Un linter può segnalare:
-   Variabili definite ma mai utilizzate.
-   Errori di sintassi comuni.
-   Violazioni delle convenzioni di stile (es. nomi di variabili non standard).
-   Potenziali bug logici.

## 2. Il Formatter: L'Ordinatore Automatico

Un **formatter** è uno strumento che riscrive automaticamente il tuo codice per assicurarsi che segua delle regole di stile precise e coerenti. Si occupa di spazi, a capo, parentesi e indentazione.

*   **Analogia**: Pensa al formatter come a una funzione di "giustifica testo" che sistema automaticamente i margini e l'interlinea di un documento per renderlo uniforme e professionale.

L'uso di un formatter elimina le discussioni sullo stile e garantisce che tutto il codice del progetto abbia lo stesso aspetto, indipendentemente da chi lo ha scritto.

## 3. Ruff: Il Coltello Svizzero per il Codice Python

**Ruff** è uno strumento moderno ed estremamente veloce che funge sia da **linter** che da **formatter** per Python. È diventato lo standard de facto in molti progetti professionali.

### a) Installazione

Con l'ambiente virtuale attivo, installiamo Ruff:
```bash
pip install ruff
```

### b) Come Usarlo

Ruff si usa da terminale.

*   **Per controllare il codice (linting)**:
    ```bash
    # Analizza tutti i file nella cartella corrente e sottocartelle
    ruff check .
    ```
    Ruff ti mostrerà una lista di errori e suggerimenti.

*   **Per formattare il codice**:
    ```bash
    # Formatta automaticamente tutti i file
    ruff format .
    ```

### c) Integrazione con VSCode

La vera potenza di Ruff si ottiene integrandolo in VSCode.

1.  Installa l'estensione **"Ruff"** dal marketplace di VSCode.
2.  Configura VSCode per formattare il codice automaticamente al salvataggio. Vai nelle impostazioni (`settings.json`) e aggiungi:
    ```json
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit"
        }
    }
    ```

Con questa configurazione, ogni volta che salvi un file Python, Ruff lo pulirà e lo formatterà automaticamente, aiutandoti a scrivere codice di alta qualità fin dal primo giorno.