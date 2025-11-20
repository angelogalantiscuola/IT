# Lezione 1: Introduzione all'ORM con Peewee

Nell'ultimo capitolo abbiamo fatto un grande passo avanti nell'organizzazione del nostro codice con i Blueprints. Tuttavia, all'interno delle nostre funzioni, continuiamo a "sporcare" il nostro codice Python con stringhe di testo in un altro linguaggio: SQL.

```python
# Esempio dal nostro codice attuale
user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
```

Questo approccio presenta diversi problemi:
1.  **Scomodo e Verboso:** Dobbiamo gestire manualmente la connessione, l'esecuzione, il recupero dei dati e la chiusura.
2.  **Rischio di Errori:** Un semplice errore di battitura nella stringa SQL non viene rilevato dall'editor e causa un errore solo a runtime.
3.  **Incoerenza Concettuale:** La nostra applicazione è scritta in Python, un linguaggio orientato agli oggetti, ma quando interagiamo con il database siamo costretti a pensare in termini di tabelle, righe e colonne.

Per risolvere questi problemi, introdurremo un **Object-Relational Mapper (ORM)**.

### 1. Cos'è un Object-Relational Mapper (ORM)?

Un ORM è una libreria che funge da "traduttore" automatico tra il mondo degli **oggetti** (nel nostro codice Python) e il mondo delle **tabelle** (nel nostro database relazionale).

L'ORM ci permette di:
*   **Definire** la struttura di una tabella del database usando una **classe Python**.
*   **Interagire** con le righe di quella tabella come se fossero **oggetti** (istanze di quella classe).
*   **Eseguire** operazioni CRUD (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) chiamando semplici **metodi** su questi oggetti, senza scrivere una sola riga di SQL.

**Vantaggi principali:**
*   **Codice più Pulito e "Pythonico":** Lavoriamo solo con oggetti e metodi, rendendo il codice più leggibile e coerente.
*   **Maggiore Produttività:** Scriviamo meno codice e più velocemente.
*   **Sicurezza Integrata:** Gli ORM generano automaticamente query parametrizzate, eliminando quasi del tutto il rischio di SQL Injection.
*   **Portabilità:** In teoria, potremmo cambiare il database sottostante (da SQLite a MariaDB, per esempio) con modifiche minime al nostro codice Python.

### 2. Introduzione a Peewee: L'ORM Semplice ed Elegante

Useremo **Peewee**, un ORM leggero e facile da imparare, perfetto per il nostro progetto.

**1. Installazione**
Assicurati che il tuo ambiente virtuale sia attivo nella cartella `flask_2` e installa Peewee:
```bash
pip install peewee
```

**2. Definire i Modelli**
Il primo passo è smettere di pensare allo `schema.sql`. La "verità" sul nostro database sarà ora definita direttamente nel codice Python attraverso i **modelli**.

Creiamo un nuovo file, `app/models.py`, che conterrà le classi che mappano le nostre tabelle.

```python
# app/models.py
import peewee as pw
import datetime

# Per ora, definiamo un'istanza del database. Nella prossima lezione la collegheremo a Flask.
# Questo crea un "proxy" che verrà configurato in seguito.
db = pw.Proxy()

# Definiamo una classe Base Model che specifica il database da usare.
# Tutte le nostre classi modello erediteranno da questa.
class BaseModel(pw.Model):
    class Meta:
        database = db

# Il modello per la tabella 'users'
class User(BaseModel):
    id = pw.AutoField(primary_key=True) # Corrisponde a INTEGER PRIMARY KEY AUTOINCREMENT
    username = pw.CharField(unique=True, null=False)
    password = pw.CharField(null=False) # L'hash della password

    def __repr__(self):
        return f"<User {self.username}>"

# Il modello per la tabella 'posts'
class Post(BaseModel):
    id = pw.AutoField(primary_key=True)
    # ForeignKeyField crea la relazione 1-a-N e la chiave esterna
    # backref='posts' ci permette di accedere ai post di un utente con user.posts
    author = pw.ForeignKeyField(User, backref='posts', null=False)
    created = pw.TimestampField(default=datetime.datetime.now)
    title = pw.CharField(null=False)
    content = pw.TextField(null=False)

    def __repr__(self):
        return f"<Post '{self.title}'>"
```
**Analizziamo il codice:**
*   `pw.CharField`, `pw.AutoField`, `pw.TimestampField`, `pw.TextField`: sono **tipi di campo** che Peewee "tradurrà" nei tipi di colonna corretti per SQLite (es. `TEXT`, `INTEGER`, `TIMESTAMP`).
*   `unique=True`, `null=False`, `primary_key=True`: sono **vincoli** che Peewee applicherà alle colonne.
*   `ForeignKeyField(User, backref='posts', null=False)`: Questo è il pezzo più importante. Dice a Peewee che la colonna `author` nella tabella `Post` è una **chiave esterna** che si riferisce all'ID della tabella `User`.

**Cosa abbiamo ottenuto?**
Abbiamo appena definito l'intera struttura del nostro database usando solo classi Python. Il file `schema.sql` non è più necessario!

### 3. Un Assaggio delle Operazioni con i Modelli

Nella prossima lezione integreremo questi modelli nella nostra app Flask. Ma per capire la potenza di questo approccio, ecco un'anteprima di come cambierà il nostro codice.

**Per trovare un utente:**
*   **Prima:** `user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()`
*   **Dopo:** `user = User.get_or_none(User.username == username)`

**Per creare un post:**
*   **Prima:** `db.execute('INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)', (title, content, author_id))`
*   **Dopo:** `Post.create(title=title, content=content, author=author_id)`

**Per ottenere tutti i post di un utente:**
*   **Prima:** `posts = db.execute('SELECT * FROM posts WHERE author_id = ?', (user_id,))`
*   **Dopo:** `posts = user.posts` (grazie al `backref` che abbiamo definito!)

Il codice diventa più leggibile, più sicuro e ci permette di lavorare con i dati in un modo molto più naturale e orientato agli oggetti. Nella prossima lezione, vedremo come integrare questo nuovo sistema nella nostra Application Factory.