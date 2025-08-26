# La Shell e i Comandi Bash

## 1. Cos'è una Shell?

La **shell** è un'interfaccia a riga di comando che permette di interagire con il sistema operativo. Invece di usare mouse e finestre (GUI - Interfaccia Grafica), si usano comandi testuali. È uno strumento potente e veloce per gestire file, eseguire programmi e automatizzare compiti.

Esistono diverse shell, le più comuni sono:
-   **Bash** (Bourne Again Shell): Lo standard su Linux e macOS. È quella che useremo.
-   **PowerShell**: La shell moderna di Windows.

## 2. Comandi Essenziali di Bash

Ecco i comandi fondamentali per muoversi e operare nel sistema.

### Navigazione nel File System

-   **`pwd`** (Print Working Directory): Mostra il percorso della cartella in cui ti trovi.
    ```bash
    pwd
    # Output: /home/utente/documenti
    ```
-   **`ls`** (List): Elenca i file e le cartelle nella directory corrente.
    ```bash
    ls -la # Mostra una lista dettagliata, inclusi i file nascosti
    ```
-   **`cd`** (Change Directory): Cambia la cartella corrente.
    ```bash
    cd /percorso/altra/cartella # Va a un percorso assoluto
    cd ..                     # Sale alla cartella genitore
    ```

### Gestione di File e Cartelle

-   **`mkdir`** (Make Directory): Crea una nuova cartella.
    ```bash
    mkdir nuova_cartella
    ```
-   **`touch`**: Crea un file vuoto.
    ```bash
    touch mio_file.txt
    ```
-   **`cp`** (Copy): Copia un file o una cartella.
    ```bash
    cp file_originale.txt file_copiato.txt
    ```
-   **`mv`** (Move): Sposta o rinomina un file/cartella.
    ```bash
    mv vecchio_nome.txt nuovo_nome.txt # Rinomina
    mv file.txt ./un_altra_cartella/   # Sposta
    ```
-   **`rm`** (Remove): Elimina un file. **Attenzione: l'eliminazione è permanente!**
    ```bash
    rm file_da_cancellare.txt
    rm -r cartella_da_cancellare # L'opzione -r cancella le cartelle e il loro contenuto
    ```

### Visualizzazione di File

-   **`cat`** (Concatenate): Mostra l'intero contenuto di un file.
    ```bash
    cat file.txt
    ```
-   **`less`**: Mostra il contenuto di un file una pagina alla volta (utile per file lunghi). Premi `q` per uscire.
    ```bash
    less file_molto_lungo.log
    ```

### Ottenere Aiuto

-   **`man`** (Manual): Mostra la pagina di manuale per un comando, spiegandone l'uso e le opzioni.
    ```bash
    man ls
    ```