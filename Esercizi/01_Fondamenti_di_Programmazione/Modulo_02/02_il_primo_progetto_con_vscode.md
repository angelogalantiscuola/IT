# Esercizio 02: Il Tuo Primo Progetto su GitHub con VS Code

**Obiettivo:**
Imparare il flusso di lavoro completo per creare un progetto da zero: creare un repository su GitHub, clonarlo sul tuo computer, modificarlo e caricare le modifiche, il tutto utilizzando l'interfaccia grafica di Visual Studio Code.

---

### Parte 1: Creare il Repository su GitHub

In questa parte, creeremo il "contenitore" online per il nostro progetto.

1.  **Accedi a GitHub:**
    Vai su [https://github.com](https://github.com) ed effettua l'accesso con il tuo account.

2.  **Crea un Nuovo Repository:**
    In alto a destra, clicca sul pulsante `+` e seleziona `New repository`.

3.  **Compila i Dettagli:**
    *   **Repository name:** Scegli un nome semplice, senza spazi (es. `primo-progetto-git`).
    *   **Description (optional):** Aggiungi una breve descrizione (es. "Il mio primo progetto per imparare a usare Git e VS Code").
    *   **Public/Private:** Seleziona `Public`.
    *   **IMPORTANTE:** Per ora, **non** spuntare le caselle "Add a README file", "Add .gitignore" o "Choose a license". Inizieremo con un repository completamente vuoto.

4.  **Crea il Repository:**
    Clicca sul pulsante verde `Create repository`.

5.  **Copia l'URL per Clonare:**
    Nella pagina successiva, vedrai una sezione "Quick setup". Assicurati che sia selezionato **HTTPS** e copia l'URL che ti viene mostrato (finisce con `.git`). Ci servirà tra un attimo.

---

### Parte 2: Lavorare sul Progetto con VS Code

Ora che il tuo "contenitore" vuoto è pronto su GitHub, andiamo a riempirlo usando VS Code.

1.  **Apri VS Code e Clona il Progetto:**
    *   Apri Visual Studio Code.
    *   Apri la "Palette dei Comandi" con la scorciatoia `Ctrl+Shift+P` (o `F1`).
    *   Inizia a scrivere `Git: Clone` e seleziona l'opzione quando appare.
    *   Incolla l'URL HTTPS che hai copiato da GitHub e premi Invio.
    *   VS Code ti chiederà in quale cartella sul tuo computer vuoi salvare il progetto. Scegline una (es. `Documenti`).

2.  **Apri la Cartella del Progetto:**
    Dopo il download, VS Code ti chiederà se vuoi aprire il repository clonato. Clicca su `Open`.

3.  **Crea un Nuovo File:**
    Nella barra laterale sinistra ("Explorer"), crea un nuovo file. Chiamalo `profilo.txt`.

4.  **Aggiungi del Contenuto:**
    Apri il file `profilo.txt` e scrivi qualche riga su di te, ad esempio:
    ```
    Nome: Mario Rossi
    Scuola: ITIS Marconi
    Obiettivo: Diventare un programmatore!
    ```
    Salva il file (`Ctrl+S`).

5.  **Vai alla Vista "Source Control":**
    Nella barra delle attività a sinistra, clicca sull'icona di "Source Control" (quella a forma di diagramma con tre cerchi).

6.  **Prepara la Modifica (Stage):**
    Vedrai il file `profilo.txt` elencato sotto la sezione "Changes". Questo significa che Git ha rilevato una modifica.
    *   Passa il mouse sul nome del file e clicca sull'icona `+` (Stage Changes).
    *   Il file si sposterà nella sezione "Staged Changes". "Staging" significa preparare una "fotografia" delle modifiche che vuoi salvare.

7.  **Salva la Modifica (Commit):**
    *   Nella casella di testo in alto ("Message"), scrivi un messaggio breve ma descrittivo che spieghi cosa hai fatto. Ad esempio: `Crea file profilo con informazioni base`.
    *   Clicca sull'icona a forma di spunta (✓) sopra la casella di testo per eseguire il "Commit". Hai appena salvato la tua "fotografia" sul tuo computer locale.

8.  **Carica le Modifiche su GitHub (Push):**
    Ora devi sincronizzare il tuo salvataggio locale con il server di GitHub.
    *   Cerca il pulsante blu `Sync Changes` in basso a sinistra nella barra di stato blu, oppure clicca sui tre puntini (`...`) in alto nella vista "Source Control" e seleziona `Push`.
    *   VS Code potrebbe chiederti le credenziali di GitHub la prima volta.

**Verifica Finale:**
Torna alla pagina del tuo repository su GitHub nel browser e aggiornala. Vedrai apparire il tuo file `profilo.txt` con il contenuto che hai scritto.

**Complimenti! Hai completato il tuo primo ciclo di sviluppo professionale con Git e VS Code!**