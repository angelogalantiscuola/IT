# Ambienti Virtuali: Introduzione

## 1. Perché Isolare i Progetti?

Quando lavori a un progetto software, userai del codice scritto da te e del codice scritto da altri (chiamato **librerie** o **dipendenze**). Con il tempo, ti capiterà di lavorare su più progetti contemporaneamente.

Il problema è che progetti diversi potrebbero aver bisogno di "attrezzi" (librerie) diversi o di versioni diverse dello stesso attrezzo. Se installi tutto nello stesso posto (a livello di sistema), i progetti inizieranno a interferire tra loro, creando conflitti e bug difficili da risolvere.

## 2. La Soluzione: Una "Scatola" per Ogni Progetto

Un **ambiente virtuale** è la soluzione a questo problema. È come creare una "scatola degli attrezzi" separata e isolata per ogni progetto su cui lavori.

*   **Analogia**: Immagina di avere una scatola di LEGO per costruire un castello e un'altra per costruire un'astronave. Non mescoleresti mai i pezzi, giusto? Ogni progetto ha la sua scatola con solo i pezzi che gli servono.

Un ambiente virtuale è una cartella che contiene:
-   Una copia dell'interprete Python.
-   Tutte le librerie necessarie **solo per quel progetto**.

Questo garantisce che i tuoi progetti siano ordinati, indipendenti e riproducibili su qualsiasi computer.

## 3. Come Creare e Attivare un Ambiente

Python include uno strumento chiamato `venv` per creare ambienti virtuali.

### a) Creazione

1.  Apri il terminale e naviga nella cartella del tuo progetto.
2.  Esegui il comando per creare l'ambiente (la convenzione è chiamarlo `.venv`).
    ```bash
    python -m venv .venv
    ```
    Questo creerà una nuova cartella `.venv` nel tuo progetto.

### b) Attivazione

Prima di poterlo usare, l'ambiente deve essere "attivato".

*   **Su Windows (Bash/WSL o Git Bash):**
    ```bash
    source .venv/Scripts/activate
    ```
*   **Su macOS e Linux:**
    ```bash
    source .venv/bin/activate
    ```

Una volta attivato, vedrai `(.venv)` all'inizio del prompt del terminale. Questo ti conferma che sei dentro la "scatola" isolata del tuo progetto.

### c) Disattivazione

Quando hai finito, per uscire dall'ambiente, digita:
```bash
deactivate
```

**Nota**: Approfondiremo come installare e gestire le librerie con `pip` in una lezione successiva, dopo aver preso confidenza con le basi di Python. Per ora, è importante abituarsi a creare e attivare un ambiente virtuale per ogni nuovo progetto.