## Gestione degli Utenti e dei Permessi <!-- omit in toc -->

- [Utenti e Ruoli](#utenti-e-ruoli)
- [Comandi SQL per la Gestione dei Permessi (DCL)](#comandi-sql-per-la-gestione-dei-permessi-dcl)

Una gestione efficace degli accessi è una delle misure di sicurezza più importanti. L'idea è di applicare il **Principio del Minimo Privilegio**: concedere a ogni utente solo le autorizzazioni strettamente necessarie.

### Utenti e Ruoli

- **Utente**: Un account specifico che può connettersi al server del database. È una buona pratica creare un utente dedicato per ogni applicazione, evitando di usare l'utente `root`.
- **Ruolo**: Un insieme predefinito di permessi che può essere assegnato a più utenti. Gestire i permessi tramite ruoli (es. `sviluppatore`, `analista_dati`) semplifica l'amministrazione in sistemi complessi.

### Comandi SQL per la Gestione dei Permessi (DCL)

Il **Data Control Language (DCL)** è il sottolinguaggio di SQL che si occupa di gestire i permessi.

- **`GRANT`**: Concede uno o più permessi a un utente o a un ruolo.

  - **Permessi Comuni**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `ALL PRIVILEGES`.
  - **Sintassi**: `GRANT <permesso> ON <database>.<tabella> TO '<utente>'@'localhost';`

  _Esempio: Concedere solo il permesso di lettura sulla tabella Studenti._

  ```sql
  GRANT SELECT ON scuola.Studenti TO 'reporter'@'localhost';
  ```

  _Esempio: Concedere tutti i permessi su un intero database._

  ```sql
  GRANT ALL PRIVILEGES ON scuola.* TO 'sviluppatore'@'localhost';
  ```

- **`REVOKE`**: Revoca un permesso precedentemente concesso.

  - **Sintassi**: `REVOKE <permesso> ON <database>.<tabella> FROM '<utente>'@'localhost';`

  _Esempio: Revocare il permesso di cancellazione._

  ```sql
  REVOKE DELETE ON scuola.Studenti FROM 'sviluppatore'@'localhost';
  ```

- **`FLUSH PRIVILEGES;`**: Comando da eseguire dopo aver modificato i permessi per assicurarsi che il server ricarichi le tabelle dei grant e applichi le modifiche.
