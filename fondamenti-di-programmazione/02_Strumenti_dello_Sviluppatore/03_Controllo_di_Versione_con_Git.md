# Controllo di Versione con Git e GitHub

## 1. A Cosa Serve il Controllo di Versione?

Il **controllo di versione** è un sistema che tiene traccia delle modifiche apportate ai file nel tempo. Permette di:
-   **Salvare "fotografie"** del progetto in momenti specifici.
-   **Tornare a versioni precedenti** se qualcosa va storto.
-   **Collaborare** con altre persone sullo stesso progetto senza creare conflitti.
-   Capire **chi ha modificato cosa e quando**.

**Git** è il software di controllo di versione più usato al mondo. **GitHub** è una piattaforma online che ospita i repository Git e facilita la collaborazione.

## 2. Il Repository: L'Archivio del Tuo Progetto

Un **repository** (o "repo") è semplicemente una cartella che contiene tutti i file del tuo progetto, insieme alla cronologia completa di tutte le modifiche.

### Creare un Repository su GitHub

1.  Vai su [GitHub](https://github.com) e accedi.
2.  Clicca su `+` in alto a destra e seleziona `New repository`.
3.  Dai un nome al repository, scegli se renderlo pubblico o privato e clicca su `Create repository`.

### Clonare un Repository Esistente

"Clonare" significa creare una copia locale di un repository che esiste su GitHub.

1.  Sulla pagina del repository su GitHub, clicca su `Code` e copia l'URL (HTTPS).
2.  In VSCode, apri la Palette dei Comandi (`Ctrl+Shift+P` o `F1`).
3.  Digita `Git: Clone` e premi Invio.
4.  Incolla l'URL e scegli una cartella sul tuo computer dove salvare il progetto.

## 3. Il Flusso di Lavoro Fondamentale

Il ciclo di lavoro con Git consiste nel salvare le modifiche (commit) e sincronizzarle con il repository remoto (push/pull).

### a) Fare un Commit: Salvare una "Fotografia" delle Modifiche

Un **commit** è un salvataggio permanente delle modifiche nel tuo repository locale.

1.  **Modifica i file**: Lavora sul tuo codice come faresti normalmente.
2.  **Visualizza le modifiche**: Vai alla scheda `Source Control` (`Ctrl+Shift+G`) in VSCode. Vedrai una lista dei file che hai modificato.
3.  **Stage (Prepara) le modifiche**: Clicca sul `+` accanto ai file che vuoi includere nel salvataggio. Questo li sposta nell'area di "staging".
4.  **Scrivi un messaggio di commit**: Nella casella di testo in alto, scrivi un messaggio breve ma descrittivo che spieghi cosa hai fatto (es. "Aggiunta funzione di login").
5.  **Esegui il commit**: Clicca sul segno di spunta (✓) per salvare le modifiche nel tuo repository locale.

### b) Sincronizzare con GitHub: Push e Pull

Una volta che hai salvato le modifiche localmente, devi sincronizzarle con GitHub.

*   **Push**: Invia i tuoi commit locali al repository remoto su GitHub. È come caricare i tuoi salvataggi.
    *   **Come fare**: Nella scheda `Source Control`, clicca sui tre puntini (`...`) e seleziona `Push`.

*   **Pull**: Scarica i commit che altri hanno caricato sul repository remoto. È come aggiornare il tuo progetto con le modifiche fatte dai tuoi collaboratori.
    *   **Come fare**: Clicca sui tre puntini (`...`) e seleziona `Pull`.

> **Buona pratica**: Esegui sempre un `pull` prima di iniziare a lavorare per assicurarti di avere la versione più aggiornata del progetto.

### Il Tasto "Sync Changes"

VSCode offre un comodo pulsante "Sync Changes" (Sincronizza Modifiche) nella barra di stato in basso a sinistra. Questo comando esegue prima un `pull` e poi un `push`, mantenendo il tuo repository locale e quello remoto perfettamente allineati.

