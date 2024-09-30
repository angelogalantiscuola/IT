## Comandi Bash  <!-- omit in toc -->

- [Comando man](#comando-man)
  - [Sintassi](#sintassi)
- [Principali comandi di Bash](#principali-comandi-di-bash)


### Comando man

Il comando `man` (abbreviazione di "manual") è utilizzato per visualizzare le pagine di manuale dei comandi disponibili nel sistema. Queste pagine forniscono una descrizione dettagliata del comando, delle sue opzioni e degli esempi di utilizzo.

#### Sintassi
```bash
man comando
```

Ad esempio, eseguendo `man ls`, puoi ottenere tutte le informazioni necessarie per utilizzare il comando `ls` in modo efficace, comprese le opzioni disponibili e gli esempi di utilizzo.

```bash
man ls
```

Questo comando aprirà la pagina di manuale per `ls`, dove potrai navigare utilizzando i tasti freccia per scorrere verso l'alto e verso il basso, e premere `q` per uscire dal manuale.

### Principali comandi di Bash

- **`ls`**: Elenca i file e le directory nel directory corrente.
  ```bash
  ls
  ```

- **`cd`**: Cambia la directory corrente.
  ```bash
  cd /percorso/della/directory
  ```

- **`pwd`**: Mostra il percorso della directory corrente.
  ```bash
  pwd
  ```

- **`cp`**: Copia file o directory.
  ```bash
  cp origine destinazione
  ```

- **`mv`**: Sposta o rinomina file o directory.
  ```bash
  mv origine destinazione
  ```

- **`rm`**: Rimuove file o directory.
  ```bash
  rm file
  rm -r directory  # Per rimuovere una directory e il suo contenuto
  ```

- **`mkdir`**: Crea una nuova directory.
  ```bash
  mkdir nuova_directory
  ```

- **`rmdir`**: Rimuove una directory vuota.
  ```bash
  rmdir directory_vuota
  ```

- **`touch`**: Crea un nuovo file vuoto o aggiorna il timestamp di un file esistente.
  ```bash
  touch nuovo_file
  ```

- **`cat`**: Visualizza il contenuto di un file.
  ```bash
  cat file
  ```

- **`echo`: Stampa un messaggio a schermo o in un file.
  ```bash
  echo "Hello, World!"
  echo "Hello, World!" > file  # Scrive nel file
  ```

- **`grep`**: Cerca testo all'interno di file.
  ```bash
  grep "testo_da_cercare" file
  ```

- **`find`**: Cerca file e directory.
  ```bash
  find /percorso -name "nome_file"
  ```

- **`chmod`**: Cambia i permessi di file o directory.
  ```bash
  chmod 755 file
  ```

- **`chown`**: Cambia il proprietario di file o directory.
  ```bash
  chown utente:gruppo file
  ```

- **`ps`**: Mostra i processi in esecuzione.
  ```bash
  ps aux
  ```

- **`kill`**: Termina un processo.
  ```bash
  kill PID
  ```

Questi comandi sono fondamentali per la gestione del sistema e l'automazione di compiti in un ambiente Bash.