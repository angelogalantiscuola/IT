# Esercizio 03: Creare e Attivare un Ambiente Virtuale

**Obiettivo:**
Imparare a creare un ambiente virtuale isolato per un progetto Python usando il modulo `venv`. Questa è una pratica fondamentale per ogni sviluppatore Python.

**Scenario:**
Stai per iniziare un nuovo progetto Python chiamato "calcolatrice". Per mantenerlo pulito e ordinato, creerai un ambiente virtuale dedicato.

**Istruzioni:**

1.  **Crea la Cartella del Progetto:**
    In una posizione a tua scelta (es. la cartella `Documenti`), crea la cartella per il nuovo progetto e naviga al suo interno.
    ```bash
    mkdir calcolatrice
    cd calcolatrice
    ```

2.  **Crea l'Ambiente Virtuale:**
    Usa il modulo `venv` di Python per creare un ambiente virtuale. La convenzione è chiamare la cartella dell'ambiente `.venv`.
    ```bash
    python -m venv .venv
    ```
    Dopo qualche secondo, se usi il comando `ls -a`, vedrai una nuova cartella nascosta `.venv`.

3.  **Attiva l'Ambiente Virtuale:**
    Questo è il passo più importante. Il comando cambia a seconda del tuo sistema operativo.

    *   **Su Windows (usando Git Bash):**
        ```bash
        source .venv/Scripts/activate
        ```
    *   **Su macOS o Linux:**
        ```bash
        source .venv/bin/activate
        ```

4.  **Osserva il Prompt del Terminale:**
    Se l'attivazione ha avuto successo, vedrai `(.venv)` apparire all'inizio del prompt del tuo terminale. Questo ti conferma che sei "dentro" l'ambiente isolato.

    Esempio: `(.venv) utente@computer:~/Documenti/calcolatrice$`

5.  **Disattiva l'Ambiente:**
    Quando hai finito di lavorare, puoi uscire dall'ambiente virtuale con un semplice comando.
    ```bash
    deactivate
    ```
    Osserva come `(.venv)` scompare dal prompt.

**Consiglio:**
Prendi l'abitudine di eseguire sempre i passaggi 1, 2 e 3 ogni volta che inizi un nuovo progetto Python. Ricorda di attivare l'ambiente virtuale (passo 3) ogni volta che apri un terminale per lavorare su quel progetto.