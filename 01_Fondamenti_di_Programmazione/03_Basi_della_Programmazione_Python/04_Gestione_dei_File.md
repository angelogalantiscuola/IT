# Gestione dei File

I programmi spesso hanno bisogno di leggere dati da file o salvare risultati su disco. Python rende queste operazioni molto semplici.

## 1. Percorsi Assoluti e Relativi

Per trovare un file, il sistema operativo ha bisogno del suo **percorso** (path).

*   **Percorso Assoluto**: È l'indirizzo completo del file, partendo dalla radice del file system. Non dipende dalla posizione del nostro script.
    *   *Esempio Windows*: `C:\Utenti\Mario\Documenti\note.txt`
    *   *Esempio Linux/macOS*: `/home/mario/documenti/note.txt`

*   **Percorso Relativo**: È l'indirizzo del file in relazione alla posizione attuale del nostro script. È più flessibile e portabile.
    *   `note.txt`: Il file si trova nella stessa cartella dello script.
    *   `dati/report.csv`: Il file si trova nella sottocartella `dati`.
    *   `../immagini/logo.png`: Il file si trova nella cartella `immagini`, che è allo stesso livello della cartella genitore (`..`).

## 2. Leggere e Scrivere File di Testo

L'istruzione `with open(...) as ...` è il modo più sicuro per lavorare con i file, perché garantisce che il file venga chiuso automaticamente anche in caso di errori.

### a) Scrivere su un File

-   **Modalità `'w'` (write)**: Crea un nuovo file o **sovrascrive** un file esistente.

    ```python
    testo_da_scrivere: str = "Questa è la prima riga.\nQuesta è la seconda riga.\n"

    try:
        with open("appunti.txt", "w", encoding="utf-8") as file:
            file.write(testo_da_scrivere)
        print("File 'appunti.txt' scritto con successo.")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")
    ```
    *`encoding="utf-8"` è una buona pratica per garantire la compatibilità con caratteri speciali (es. lettere accentate).*

-   **Modalità `'a'` (append)**: Aggiunge contenuto alla fine di un file esistente, senza cancellare il contenuto precedente.

    ```python
    with open("appunti.txt", "a", encoding="utf-8") as file:
        file.write("Questa riga viene aggiunta alla fine.\n")
    ```

### b) Leggere da un File

-   **Modalità `'r'` (read)**: Apre un file per la lettura.

    ```python
    try:
        with open("appunti.txt", "r", encoding="utf-8") as file:
            # Leggere l'intero contenuto in una singola stringa
            contenuto_completo = file.read()
            print("--- Contenuto completo ---")
            print(contenuto_completo)

        with open("appunti.txt", "r", encoding="utf-8") as file:
            # Leggere il file riga per riga (metodo consigliato per file grandi)
            print("\n--- Lettura riga per riga ---")
            for riga in file:
                print(riga.strip()) # .strip() rimuove spazi e a-capo extra
    except FileNotFoundError:
        print("Errore: il file 'appunti.txt' non è stato trovato.")
    except IOError as e:
        print(f"Errore durante la lettura del file: {e}")
    ```

## 3. Formati di File Comuni

Oltre ai file di testo semplice (`.txt`), incontrerai spesso altri formati:
*   **CSV (Comma-Separated Values)**: Dati tabellari, dove le colonne sono separate da virgole. Ottimo per esportare dati da fogli di calcolo.
*   **JSON (JavaScript Object Notation)**: Strutturato in coppie chiave-valore, ideale per dati complessi e per la comunicazione tra applicazioni web.
*   **XML (eXtensible Markup Language)**: Simile a HTML, usa dei tag per descrivere la struttura dei dati. È più verboso di JSON.