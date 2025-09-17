## SQL Injection <!-- omit in toc -->

- [Cos'è la SQL Injection?](#cosè-la-sql-injection)
- [Come Funziona un Attacco](#come-funziona-un-attacco)
- [Prevenzione: La Regola d'Oro](#prevenzione-la-regola-doro)

La **SQL Injection** è una delle vulnerabilità di sicurezza più diffuse e pericolose nelle applicazioni web. Si verifica quando un utente malintenzionato riesce a "iniettare" e a far eseguire comandi SQL malevoli attraverso un campo di input di un'applicazione.

### Cos'è la SQL Injection?

L'attacco sfrutta una gestione non sicura dell'input dell'utente. Se un'applicazione costruisce le sue query SQL concatenando direttamente le stringhe provenienti dall'utente, un utente può inserire del testo che altera la logica originale della query.

### Come Funziona un Attacco

Immaginiamo una query per un form di login, costruita in modo **insicuro**:

```python
# CODICE VULNERABILE - DA NON USARE MAI!
username = request.form['username'] # L'utente inserisce: 'admin'
password = request.form['password'] # L'utente inserisce: 'password' OR '1'='1'

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
# La query risultante diventa:
# SELECT * FROM users WHERE username = 'admin' AND password = 'password' OR '1'='1'
```

La condizione `'1'='1'` è sempre vera, quindi la clausola `WHERE` diventa `... WHERE (condizione_originale) OR TRUE`. Questo fa sì che la query restituisca sempre almeno una riga (probabilmente il primo utente della tabella, che spesso è l'amministratore), bypassando il controllo della password e garantendo l'accesso all'attaccante.

### Prevenzione: La Regola d'Oro

La prevenzione si basa su un unico, fondamentale principio: **separare sempre il codice (la query SQL) dai dati (l'input dell'utente)**.

Questo si ottiene utilizzando le **query parametrizzate** (o _prepared statements_), come già visto nella lezione `12_SQL_in_Python.md`.

Quando si usa una query parametrizzata:

1.  Si invia al database il "template" della query con dei segnaposto (es. `?` o `%s`).
2.  Il database analizza, compila e ottimizza la struttura della query.
3.  Separatamente, si inviano i valori forniti dall'utente.

Il database tratterà questi valori **sempre e solo come dati**, mai come parte eseguibile della query. Anche se un utente inserisse del codice SQL, questo verrebbe interpretato come una semplice stringa da cercare e non verrebbe mai eseguito.

**L'uso di un ORM (Object-Relational Mapper), che vedremo più avanti, è un altro metodo potentissimo per prevenire la SQL injection, poiché genera query parametrizzate per design.**
