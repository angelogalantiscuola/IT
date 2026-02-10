**Python, tipizzazione e Type Hinting**

- Python è un linguaggio a "tipizzazione dinamica": cosa significa questo concetto rispetto a linguaggi a tipizzazione statica?
- Cosa sono i "Type Hints" e qual è il loro scopo principale, dato che l'interprete Python non li rende obbligatori per l'esecuzione del codice?

**.gitignore e Ambiente Virtuale**
- A cosa serve l'ambiente virtuale (`venv`) in Python?
- Perché generiamo il file `requirements.txt` per il deployment?
- Qual è lo scopo del file `.gitignore` e quali file critici non dovrebbero mai finire su GitHub?

**Modello ER e Database**
- Quali sono i componenti fondamentali di un diagramma ER?
- Spiega i tipi di cardinalità (1:1, 1:N, N:N) e fornisci un esempio per ciascuno.
- Come si traduce una relazione "Molti a Molti" dal modello ER al codice SQL (Tabella di Raccordo)?
- In cosa consiste la Normalizzazione e quali problemi risolve (anomalie)?
- Qual è la differenza tra Prima, Seconda e Terza Forma Normale?
- Definizione e ruolo della Chiave Primaria e della Chiave Esterna.

**SQL e Interazione con Python**
- Qual è la differenza tra DDL (`CREATE`, `DROP`) e DML (`INSERT`, `SELECT`)?
- A cosa servono le clausole `GROUP BY` e `HAVING`?
- Spiega la differenza tra `JOIN` e `LEFT JOIN`.
- Cos'è la SQL Injection?
- A cosa servono i file `.sqlite` e la cartella `instance` in Flask?

**Architettura Web e Flask**
- A cosa serve il file `__init__.py` all'interno della cartella `app`?
- Cosa sono i **Blueprint** e qual è il loro vantaggio rispetto a un file unico?
- Cos'è il **Repository Pattern** e perché separiamo le query SQL dalle route di Flask?
- Come funziona il motore di template **Jinja2** e il concetto di ereditarietà (`{% extends %}`)?

**HTTP, API e Sicurezza**
- Descrivi il ciclo Request/Response e il ruolo dello Status Code.
- Qual è la differenza tra i metodi HTTP `GET` e `POST`?
- Cosa significa che il protocollo HTTP è "Stateless" e come le **Sessioni** risolvono questo problema?
- Perché è necessario fare l'hashing delle password (`generate_password_hash`) prima di salvarle nel DB?
- Cos'è un server WSGI (es. Gunicorn) e perché è necessario per il deployment (invece di `flask run`)?
- A cosa servono le Variabili d'Ambiente (`.env`) e perché non bisogna committare la `SECRET_KEY`?

**DB e DBMS**
- Qual è la differenza sostanziale tra un Database (i dati) e un DBMS (il software)?
- Quali sono le funzioni principali di un DBMS (es. controllo concorrenza, gestione transazioni)?

**Relazionale vs NoSQL**
- Come sono organizzati i dati in un database relazionale rispetto a uno NoSQL?
- In quali contesti si preferisce un database NoSQL rispetto a uno relazionale?

**ACID**
- Cosa significa l'acronimo ACID nel contesto delle transazioni?
- Spiega brevemente le proprietà di Atomicità e Durabilità.

**Analisi dei Requisiti**
- Qual è l'obiettivo principale dell'analisi dei requisiti nella progettazione "Design-First"?

**Vincoli di Integrità**
- Cosa sono i vincoli di integrità e perché garantiscono la qualità dei dati?
- Oltre alla Chiave Primaria ed Esterna, a cosa servono i vincoli `UNIQUE`, `NOT NULL` e `CHECK`?

**Sicurezza (Autenticazione, Autorizzazione, Audit)**
- Qual è la differenza tecnica tra Autenticazione (chi sei) e Autorizzazione (cosa puoi fare)?
- In cosa consiste l'Audit di un database e perché è utile per la sicurezza?

**API e REST**
- Cos'è un'API e come funziona l'analogia del "Ristorante" (Cliente, Cameriere, Cucina)?
- Quali sono i principi fondamentali dello stile architetturale REST (es. Stateless, Risorse)?

**Endpoint**
- Cos'è un Endpoint e da quali due elementi è composto?
- Fai un esempio di due endpoint diversi che usano lo stesso URL ma metodi HTTP differenti.

**Deployment**
- Qual è la differenza tra l'ambiente di Sviluppo e quello di Produzione?
- Perché in produzione è necessario usare un server WSGI come Gunicorn?
- Perché i dati su piattaforme gratuite come Render (con SQLite) sono considerati "effimeri"?
