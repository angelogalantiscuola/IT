## SQL Injection e Sicurezza nelle Query <!-- omit in toc -->

- [Che Cos'è la SQL Injection?](#che-cosè-la-sql-injection)
  - [Esempio di SQL Injection](#esempio-di-sql-injection)
- [Tipi di SQL Injection](#tipi-di-sql-injection)
  - [Iniezione Basata su Errori](#iniezione-basata-su-errori)
  - [Iniezione Blind (Blind SQL Injection)](#iniezione-blind-blind-sql-injection)
  - [Iniezione Basata su Time Delay](#iniezione-basata-su-time-delay)
- [Come Prevenire la SQL Injection](#come-prevenire-la-sql-injection)
  - [Utilizzo di Query Parametrizzate](#utilizzo-di-query-parametrizzate)
  - [Escaping degli Input](#escaping-degli-input)
  - [Limitare i Permessi del Database](#limitare-i-permessi-del-database)
  - [Validazione degli Input](#validazione-degli-input)
  - [Uso di ORM (Object-Relational Mapping)](#uso-di-orm-object-relational-mapping)
- [Esempi di Prevenzione](#esempi-di-prevenzione)
  - [Validazione dell'Input in Python](#validazione-dellinput-in-python)
  - [Uso di un ORM in Django](#uso-di-un-orm-in-django)

La **SQL Injection** è una delle vulnerabilità più pericolose e diffuse nei sistemi che utilizzano database relazionali. Si verifica quando un utente malintenzionato riesce a iniettare comandi SQL malevoli all'interno di una query tramite input non adeguatamente validato. In questa lezione, esploreremo cosa sia la SQL Injection, come funziona e, soprattutto, come prevenire questo tipo di attacco attraverso pratiche di sicurezza nelle query.

### Che Cos'è la SQL Injection?

La SQL Injection è un attacco in cui un hacker inserisce del codice SQL all'interno di un input che viene successivamente eseguito dal database. Ciò avviene perché le query SQL inviate al database non sono state progettate per distinguere correttamente tra dati legittimi e codice malevolo.

#### Esempio di SQL Injection
Supponiamo di avere una query SQL che cerca un utente in base al nome inserito in un modulo di login:

```sql
SELECT * FROM utenti WHERE nome = 'utente_inserito';
```

Se l'input non viene validato correttamente, un utente malintenzionato potrebbe inserire il seguente testo nel campo del nome:

```sql
' OR '1'='1
```

La query risultante sarà:

```sql
SELECT * FROM utenti WHERE nome = '' OR '1'='1';
```

Questa query è sempre vera, poiché l'espressione `'1'='1'` è sempre valida. Di conseguenza, l'attaccante potrebbe ottenere l'accesso a tutti i record della tabella "utenti" o addirittura compromettere l'intero sistema.

### Tipi di SQL Injection

Esistono diversi tipi di SQL Injection, ognuno con diverse modalità operative:

#### Iniezione Basata su Errori
In questo tipo di attacco, un hacker sfrutta i messaggi di errore restituiti dal database per ottenere informazioni sensibili. Questi messaggi possono contenere dettagli come nomi di tabelle, colonne o strutture di query.

#### Iniezione Blind (Blind SQL Injection)
In un attacco **blind**, il sistema non restituisce direttamente i risultati delle query o messaggi di errore, ma l'attaccante può inferire il funzionamento del database attraverso osservazioni indirette, come cambiamenti nel comportamento dell'applicazione (ad esempio, se una pagina carica più lentamente o restituisce un messaggio diverso a seguito dell'iniezione).

#### Iniezione Basata su Time Delay
L'attaccante esegue una query che forza il database a ritardare la risposta, in modo da poter rilevare se l'iniezione è andata a buon fine. Questo tipo di attacco si utilizza spesso in combinazione con la **Blind SQL Injection**.

### Come Prevenire la SQL Injection

La prevenzione della SQL Injection richiede l'implementazione di diverse tecniche di sicurezza, che rendono difficile o impossibile l'inserimento di codice SQL non autorizzato nelle query.

#### Utilizzo di Query Parametrizzate
Il metodo più efficace per prevenire la SQL Injection è l'uso di **query parametrizzate** o **prepared statements**. Questo approccio assicura che i valori forniti dall'utente vengano trattati come dati e non come codice SQL.

Esempio in Python con una query parametrizzata usando `sqlite3`:

```python
query = "SELECT * FROM utenti WHERE nome = ?"
cur.execute(query, (utente_inserito,))
```

In questo caso, il parametro `utente_inserito` viene passato separatamente dal comando SQL, garantendo che non possa alterare la struttura della query.

#### Escaping degli Input
Se per qualche motivo non è possibile usare query parametrizzate, un'alternativa è quella di **escapare** tutti i caratteri pericolosi. In questo modo, i caratteri speciali (come i singoli apici) vengono convertiti in una forma che non viene interpretata come parte del codice SQL.

Tuttavia, questa tecnica non è sempre affidabile, ed è quindi preferibile utilizzare query parametrizzate ogni volta che è possibile.

#### Limitare i Permessi del Database
Un'altra misura di sicurezza è limitare i permessi degli utenti del database. Ad esempio, un utente che accede ai dati tramite un'applicazione web dovrebbe avere solo i permessi necessari per leggere o modificare i dati. Non dovrebbe mai avere permessi amministrativi come **DROP**, **ALTER** o **GRANT**.

> _Nota: La gestione dettagliata dei permessi è trattata nella lezione “Gestione degli Utenti e Permessi”._

#### Validazione degli Input
Validare correttamente tutti gli input è fondamentale. Bisogna assicurarsi che i dati forniti dagli utenti siano conformi al tipo previsto (ad esempio, numeri, stringhe, date, ecc.) e che rispettino i limiti di lunghezza e formato. È anche utile rifiutare o gestire in modo sicuro input contenenti caratteri speciali che potrebbero alterare le query SQL.

#### Uso di ORM (Object-Relational Mapping)
Gli ORM (Object-Relational Mapping) forniscono un'astrazione sopra il livello SQL e riducono il rischio di SQL Injection automatizzando la costruzione di query in modo sicuro. Tuttavia, è importante comprendere che l'uso di un ORM non garantisce automaticamente la sicurezza, e devono comunque essere applicate le buone pratiche di sicurezza.

> _Nota: Gli ORM e il loro utilizzo vengono trattati nella lezione “ORM: Object-Relational Mapping”._

### Esempi di Prevenzione

#### Validazione dell'Input in Python
In Python, possiamo usare funzioni di validazione per assicurare che l'input dell'utente sia valido prima di eseguire una query:

```python
def valida_nome(nome):
    if len(nome) > 50 or not nome.isalnum():
        raise ValueError("Nome non valido")
    return nome

nome_valido = valida_nome(utente_inserito)
```

#### Uso di un ORM in Django
Django è un framework web che include un ORM per la gestione sicura delle query SQL. Quando si utilizza l'ORM di Django, le query vengono automaticamente parametrizzate.

Esempio di una query sicura in Django:

```python
utenti = Utente.objects.filter(nome=utente_inserito)
```

L'ORM di Django genera query SQL in modo sicuro, prevenendo automaticamente la SQL Injection.
