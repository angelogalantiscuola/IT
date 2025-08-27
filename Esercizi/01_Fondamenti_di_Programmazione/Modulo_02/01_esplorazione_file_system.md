# Esercizio 01: Esplorazione del File System con la Shell

**Obiettivo:**
Padroneggiare i comandi essenziali della shell Bash per la navigazione e la manipolazione di file e cartelle. Questo esercizio ti aiuterà a muoverti con sicurezza nel tuo computer usando solo la riga di comando.

**Istruzioni:**
Apri il tuo terminale (Git Bash su Windows, Terminale su macOS/Linux) e segui questi passaggi uno alla volta, premendo Invio dopo ogni comando.

1.  **Vai alla tua cartella Home:**
    Il comando `cd` senza argomenti ti porta sempre alla tua cartella utente principale.
    ```bash
    cd
    ```

2.  **Crea una cartella per i tuoi progetti:**
    Usa `mkdir` (make directory) per creare una nuova cartella.
    ```bash
    mkdir progetti_scolastici
    ```

3.  **Entra nella nuova cartella:**
    Usa `cd` per cambiare la tua posizione attuale.
    ```bash
    cd progetti_scolastici
    ```

4.  **Verifica dove ti trovi:**
    Usa `pwd` (print working directory) per confermare di essere nel percorso corretto.
    ```bash
    pwd
    ```

5.  **Crea due sottocartelle per le materie:**
    ```bash
    mkdir informatica
    mkdir italiano
    ```

6.  **Crea dei file vuoti:**
    Usa `touch` per creare dei file di appunti.
    ```bash
    touch informatica/appunti_python.txt
    touch italiano/riassunto_promessi_sposi.txt
    ```

7.  **Elenca tutto il contenuto:**
    Usa `ls` con l'opzione `-R` (ricorsiva) per vedere la struttura completa di file e cartelle che hai creato.
    ```bash
    ls -R
    ```

8.  **Pulisci tutto:**
    Torna indietro alla cartella genitore con `cd ..` e poi usa `rm` con l'opzione `-r` (ricorsiva) per cancellare la cartella `progetti_scolastici` e tutto il suo contenuto. **Attenzione: questo comando è definitivo!**
    ```bash
    cd ..
    rm -r progetti_scolastici
    ```

**Domanda di verifica:**
Qual è la differenza tra il comando `rm nome_file.txt` e `rm -r nome_cartella`?