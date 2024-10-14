# MariaDB

MariaDB è un sistema di gestione di database relazionali (**RDBMS**) open source, derivato da MySQL. È stato creato dagli sviluppatori originali di MySQL dopo che Oracle Corporation ha acquisito MySQL. MariaDB è progettato per essere altamente compatibile con MySQL, il che significa che la maggior parte delle applicazioni e degli strumenti che funzionano con MySQL possono essere utilizzati anche con MariaDB senza modifiche significative.

## Caratteristiche principali di MariaDB:
- **Open Source**: MariaDB è distribuito sotto la licenza GPL, il che significa che è gratuito e il suo codice sorgente è disponibile per chiunque voglia esaminarlo o modificarlo.
- **Compatibilità con MySQL**: MariaDB è compatibile con MySQL a livello di protocollo e di API, il che facilita la migrazione da MySQL a MariaDB.
- **Prestazioni migliorate**: MariaDB include diverse ottimizzazioni delle prestazioni rispetto a MySQL, come l'ottimizzazione delle query e l'uso di motori di archiviazione avanzati.

In sintesi, MariaDB è una scelta popolare per chi cerca un sistema di gestione di database relazionali open source, compatibile con MySQL, ma con miglioramenti in termini di prestazioni, sicurezza e funzionalità.

## Installazione di MariaDB

Per installare MariaDB su Ubuntu tramite terminale, segui questi passaggi:

1. **Aggiorna l'elenco dei pacchetti:**
   ```bash
   sudo apt update
   ```

2. **Installa il server MariaDB:**
   ```bash
   sudo apt install mariadb-server
   ```

3. **Avvia il servizio MariaDB:**
   ```bash
   sudo service mariadb start
   ```

4. **Abilita MariaDB per l'avvio automatico all'avvio del sistema:**
   ```bash
   sudo systemctl enable mariadb
   ```

5. **Esegui lo script di sicurezza per configurare MariaDB:**
   ```bash
   sudo mysql_secure_installation
   ```
   Segui le istruzioni per impostare la password di root e configurare altre opzioni di sicurezza.

6. **Verifica che MariaDB sia in esecuzione:**
   ```bash
   sudo service mariadb status
   ```

## Connessione a MariaDB

Per connettersi a un database MariaDB, è possibile utilizzare diversi strumenti e metodi. Di seguito sono riportati alcuni dei metodi più comuni:

### Utilizzo del Client MySQL da Linea di Comando

Esegui il comando per connetterti al server MariaDB:
```bash
mysql -u [nome_utente] -p -h [host] -P [porta]
```

Sostituisci [nome_utente] con il nome utente del database, [host] con l'indirizzo del server (ad esempio, localhost), e [porta] con il numero di porta (di solito 3306).

```bash
mysql -u x -p -h localhost -P 3306
```

Dopo esserti connesso al server MariaDB, puoi elencare tutti i database disponibili utilizzando il seguente comando SQL: `SHOW DATABASES;`.

### Utilizzo dell'estensione SQLTools per connettersi a MariaDB

SQLTools è un'estensione di Visual Studio Code che consente di connettersi e interagire con vari database, tra cui MariaDB. Ecco come configurare e utilizzare SQLTools per connettersi a un database MariaDB:

1. **Installa l'estensione SQLTools:**
   - Apri Visual Studio Code.
   - Vai su `Estensioni` (icona del quadrato con i lati aperti) o premi `Ctrl+Shift+X`.
   - Cerca `SQLTools` e clicca su `Installa`.

2. **Installa il driver SQLTools per MySQL/MariaDB:**
   - Dopo aver installato SQLTools, cerca e installa l'estensione `SQLTools MySQL/MariaDB` driver.

3. **Configura la connessione a MariaDB:**
   - Vai su `Visualizza` > `Comando Paletta` o premi `Ctrl+Shift+P`.
   - Digita `SQLTools: New Connection` e seleziona l'opzione.
   - Compila i campi richiesti nella finestra di configurazione della connessione:
     - **Driver**: Seleziona `MySQL/MariaDB`.
     - **Name**: Dai un nome alla connessione.
     - **Server/Host**: Inserisci l'indirizzo del server (ad esempio, `localhost`).
     - **Port**: Inserisci il numero di porta (di solito `3306`).
     - **Database**: Inserisci il nome del database a cui vuoi connetterti (puoi lasciarlo vuoto per elencare tutti i database).
     - **Username**: Inserisci il nome utente del database.
     - **Password**: Inserisci la password del database.

4. **Salva e testa la connessione:**
   - Clicca su `Save` per salvare la configurazione della connessione.
   - Dopo aver salvato, la connessione dovrebbe apparire nel pannello SQLTools.
   - Clicca con il tasto destro sulla connessione e seleziona `Connect` per connetterti al database.

5. **Esegui query SQL:**
   - Una volta connesso, puoi aprire un nuovo file SQL (`.sql`) e scrivere le tue query.
   - Seleziona la query che vuoi eseguire e premi `Ctrl+E` per eseguirla.
   - I risultati della query verranno visualizzati nel pannello dei risultati di SQLTools.

Con questi passaggi, dovresti essere in grado di connetterti a un database MariaDB utilizzando l'estensione SQLTools in Visual Studio Code.

## temp
https://sqlzoo.net/wiki/SQLZOO:About