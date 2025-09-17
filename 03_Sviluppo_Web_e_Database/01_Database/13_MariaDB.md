# Guida a MariaDB

MariaDB è un sistema di gestione di database relazionali (RDBMS) open source, creato dagli sviluppatori originali di MySQL. È altamente compatibile con MySQL, quindi la maggior parte degli strumenti e dei comandi funziona in modo identico.

## Installazione (su Ubuntu/Debian)

1.  **Aggiorna i pacchetti:**
    ```bash
    sudo apt update
    ```
2.  **Installa il server MariaDB:**
    ```bash
    sudo apt install mariadb-server
    ```
3.  **Esegui lo script di sicurezza:**
    ```bash
    sudo mysql_secure_installation
    ```
    Questo script ti guiderà nella configurazione della password di root e nella rimozione di alcune impostazioni predefinite insicure.

## Connessione da Terminale

Per connetterti al server MariaDB dalla riga di comando, usa il client `mysql`:

```bash
sudo mysql -u root -p
```

Ti verrà chiesta la password di root che hai impostato durante l'installazione.

Una volta dentro, puoi eseguire comandi SQL. Ecco alcuni comandi utili:

- `SHOW DATABASES;`: Elenca tutti i database presenti sul server.
- `CREATE DATABASE nome_database;`: Crea un nuovo database.
- `USE nome_database;`: Seleziona un database su cui lavorare.
- `SHOW TABLES;`: Mostra le tabelle nel database corrente.
- `DESCRIBE nome_tabella;`: Mostra la struttura di una tabella.
- `EXIT;`: Esce dal client.

## Creazione di un Utente Dedicato

È una buona pratica non usare l'utente `root` per le applicazioni. Creiamo un utente specifico.

1.  **Accedi come `root`:**
    ```bash
    sudo mysql -u root -p
    ```
2.  **Crea l'utente e imposta la password:**
    ```sql
    CREATE USER 'nome_utente'@'localhost' IDENTIFIED BY 'una_password_sicura';
    ```
3.  **Crea un database per l'utente:**
    ```sql
    CREATE DATABASE db_per_utente;
    ```
4.  **Assegna i privilegi all'utente su quel database:**
    ```sql
    GRANT ALL PRIVILEGES ON db_per_utente.* TO 'nome_utente'@'localhost';
    ```
5.  **Applica le modifiche:**
    `sql
    FLUSH PRIVILEGES;
    EXIT;
    `
    Ora puoi connetterti direttamente con il nuovo utente:

```bash
mysql -u nome_utente -p
```

## Importare un Database da un File

Se hai un file `.sql` (un "dump" del database), puoi importarlo direttamente da terminale (non dentro il client `mysql`).

```bash
mysql -u nome_utente -p nome_database < percorso/del/tuo/file.sql
```

Questo comando eseguirà tutte le istruzioni SQL contenute nel file all'interno del database specificato.
