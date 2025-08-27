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

## 3. Lavorare con Formati Strutturati

Oltre al testo semplice, è fondamentale saper gestire formati di dati strutturati. Vediamo degli esempi per i più comuni, usando le librerie standard di Python.

### a) JSON (JavaScript Object Notation)

Ideale per dati complessi e gerarchici (come i dizionari Python) e molto usato nelle applicazioni web.

```python
import json

# Dati di esempio: un dizionario che descrive uno studente
studente_dati = {
    "nome": "Laura Bianchi",
    "eta": 17,
    "corsi": ["Matematica", "Fisica"],
    "promosso": True
}

# Scrivere dati su un file JSON
try:
    with open("studente.json", "w", encoding="utf-8") as f:
        json.dump(studente_dati, f, indent=4) # 'indent=4' per una formattazione leggibile
    print("\nFile 'studente.json' creato con successo.")
except IOError as e:
    print(f"Errore di scrittura JSON: {e}")

# Leggere dati da un file JSON
try:
    with open("studente.json", "r", encoding="utf-8") as f:
        dati_letti = json.load(f)
        print("--- Dati letti da 'studente.json' ---")
        print(dati_letti)
        print(f"Nome letto dal file: {dati_letti['nome']}")
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Errore di lettura JSON: {e}")
```

### b) CSV (Comma-Separated Values)

Perfetto per dati tabellari, come quelli provenienti da un foglio di calcolo. Ogni riga è una lista di valori.

```python
import csv

# Dati di esempio: una lista di liste (la prima è l'intestazione)
voti_dati = [
    ["Studente", "Matematica", "Italiano"],
    ["Alice", "8", "7"],
    ["Bob", "6", "9"]
]

# Scrivere dati su un file CSV
try:
    with open("voti.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(voti_dati)
    print("\nFile 'voti.csv' creato con successo.")
except IOError as e:
    print(f"Errore di scrittura CSV: {e}")

# Leggere dati da un file CSV
try:
    with open("voti.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        print("--- Dati letti da 'voti.csv' ---")
        for riga in reader:
            print(riga)
except FileNotFoundError as e:
    print(f"Errore di lettura CSV: {e}")
```
