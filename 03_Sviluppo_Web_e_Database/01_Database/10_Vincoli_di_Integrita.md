## Vincoli di Integrità <!-- omit in toc -->

- [Tipi di Vincoli di Integrità](#tipi-di-vincoli-di-integrità)

I **vincoli di integrità** sono regole che vengono applicate alle colonne di una tabella per garantire l'accuratezza, la coerenza e la validità dei dati. Sono un meccanismo fondamentale con cui il DBMS protegge l'integrità del database.

### Tipi di Vincoli di Integrità

Oltre ai vincoli di **chiave primaria** e **chiave esterna** già visti, esistono altri vincoli importanti:

1.  **Vincolo di Unicità (`UNIQUE`)**

    - **Scopo**: Assicura che tutti i valori in una colonna (o in un insieme di colonne) siano unici.
    - _Esempio_: In una tabella `Utenti`, l'indirizzo `email` deve essere unico per ogni utente, ma potrebbe non essere la chiave primaria.

2.  **Vincolo di Non Nullità (`NOT NULL`)**

    - **Scopo**: Assicura che una colonna non possa contenere valori `NULL`. Ogni riga deve obbligatoriamente avere un valore per quella colonna.
    - _Esempio_: In una tabella `Studenti`, le colonne `Nome` e `Cognome` non possono essere lasciate vuote.

3.  **Vincolo di Default (`DEFAULT`)**

    - **Scopo**: Fornisce un valore predefinito per una colonna quando nessun valore viene specificato durante l'inserimento di una nuova riga.
    - _Esempio_: In una tabella `Ordini`, la colonna `data_ordine` può avere come valore di default la data e l'ora correnti.

4.  **Vincolo di Controllo (`CHECK`)**
    - **Scopo**: Assicura che tutti i valori in una colonna soddisfino una specifica condizione booleana.
    - _Esempio_: In una tabella `Prodotti`, si può definire un vincolo `CHECK (prezzo > 0)` per assicurarsi che il prezzo sia sempre un numero positivo. Oppure, in una tabella `Studenti`, `CHECK (eta >= 18)`.

Questi vincoli vengono definiti durante la creazione della tabella con il comando `CREATE TABLE` in SQL.
