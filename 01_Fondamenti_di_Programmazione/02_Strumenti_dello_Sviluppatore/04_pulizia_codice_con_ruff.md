# Esercizio 04: Pulizia Automatica del Codice con Ruff

**Obiettivo:**
Imparare a usare un linter e un formatter (`Ruff`) per analizzare e migliorare la qualità del codice. Vedrai come questi strumenti possono trovare errori nascosti e rendere il codice più leggibile con un solo comando.

**Scenario:**
Hai ricevuto un file Python da un collega. Il codice sembra funzionare, ma è scritto in modo disordinato e potrebbe contenere degli errori non evidenti. Il tuo compito è usare `Ruff` per analizzarlo e sistemarlo.

---

### Parte 1: Preparazione dell'Ambiente

1.  **Crea un Progetto di Test:**
    Nel tuo terminale, crea una cartella per questo esercizio e naviga al suo interno.
    ```bash
    mkdir progetto-ruff
    cd progetto-ruff
    ```

2.  **Crea e Attiva un Ambiente Virtuale:**
    Come hai imparato nell'esercizio precedente, isoliamo sempre le dipendenze di un progetto.
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate  # Su Windows (Git Bash)
    # source .venv/bin/activate    # Su macOS/Linux
    ```

3.  **Installa Ruff:**
    Con l'ambiente virtuale attivo, installa `Ruff` usando `pip`.
    ```bash
    pip install ruff
    ```

4.  **Crea il File "Disordinato":**
    Usando VS Code, crea un nuovo file chiamato `codice_disordinato.py` all'interno della cartella `progetto-ruff`. Copia e incolla il seguente codice al suo interno. **È intenzionalmente scritto male!**

    ```python
    import os

    def calcola_somma (a,b):
      risultato=a+b
      y = 10 # Variabile non usata
      return risultato

    x=calcola_somma(5,3)
    print('Il risultato è:', x)
    ```

---

### Parte 2: Analisi e Formattazione da Terminale

Ora usiamo `Ruff` per fare il lavoro sporco.

1.  **Esegui il Linter:**
    Nel terminale (assicurati di essere ancora nella cartella `progetto-ruff` con l'ambiente attivo), esegui il comando di analisi di `Ruff`.
    ```bash
    ruff check .
    ```

2.  **Analizza l'Output:**
    Ruff ti mostrerà due errori che ha trovato nel file `codice_disordinato.py`:
    *   Un errore per l'import di `os` che non viene mai usato (`F401`).
    *   Un errore per la variabile `y` che è stata definita ma mai usata (`F841`).
    Questo è il **linter**: ti avvisa di problemi logici e di stile.

3.  **Esegui il Formatter:**
    Ora, sistemiamo automaticamente la formattazione (spazi, a capo, etc.).
    ```bash
    ruff format .
    ```

4.  **Osserva la Magia:**
    Riapri il file `codice_disordinato.py` in VS Code. Noterai che `Ruff` ha automaticamente corretto la spaziatura e l'indentazione!
    ```python
    import os

    def calcola_somma(a, b):
        risultato = a + b
        y = 10  # Variabile non usata
        return risultato

    x = calcola_somma(5, 3)
    print("Il risultato è:", x) # Ha anche cambiato gli apici!
    ```
    Questo è il **formatter**: sistema lo stile del codice.

5.  **Correggi gli Errori Rimasti:**
    Il formatter ha pulito lo stile, ma gli errori logici segnalati dal linter sono ancora lì. Modifica manualmente il file per rimuovere l'import di `os` e la riga `y = 10`.

6.  **Verifica Finale:**
    Esegui di nuovo il linter.
    ```bash
    ruff check .
    ```
    Questa volta, il comando non dovrebbe produrre alcun output. Questo significa che il tuo codice è pulito e senza errori evidenti!

---

### Parte 3 (Bonus): Integrazione con VS Code

Per un'esperienza professionale, configura VS Code per fare tutto questo automaticamente ogni volta che salvi.

1.  Assicurati di aver installato l'estensione **"Ruff"** in VS Code.
2.  Crea un file `.vscode/settings.json` nel tuo progetto e incolla questa configurazione:
    ```json
    {
        "[python]": {
            "editor.defaultFormatter": "charliermarsh.ruff",
            "editor.formatOnSave": true,
            "editor.codeActionsOnSave": {
                "source.fixAll": "explicit"
            }
        }
    }
    ```
3.  Ora prova a rovinare di nuovo la formattazione nel tuo file Python e a salvare (`Ctrl+S`). Verrà sistemato automaticamente!

**Complimenti! Ora sai come mantenere il tuo codice pulito e professionale con strumenti standard del settore.**