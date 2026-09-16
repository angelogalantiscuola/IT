# Oltre il JSON: Verso i Database Relazionali e gli ORM (Teoria e Visione)

Nella lezione precedente abbiamo reso il nostro gioco persistente salvando l'intero stato (Eroe, Zaino, Oggetti) in un file `salvataggio.json`.

Per un'applicazione locale o un videogioco a giocatore singolo, il formato JSON è una soluzione eccellente, rapida ed elegante.

Ma cosa succede quando dobbiamo progettare sistemi aziendali, piattaforme e-commerce o applicazioni web con migliaia di utenti simultanei?

---

## 1. I Limiti dei File Piatti (Perché il JSON non basta più?)

Immagina di gestire un sistema come *Spotify*, *Amazon* o un gioco multiplayer online:

1. **Concorrenza (Accesso simultaneo):** Se due utenti provano a scrivere sullo stesso file JSON nello stesso millisecondo, il file si corrompe irrimediabilmente.
2. **Efficienza della Memoria:** Se abbiamo 5 milioni di prodotti, per cercarne uno in un file JSON dovremmo caricare un file da 2 Gigabyte interamente nella memoria RAM, saturando il server.
3. **Integrità Referenziale:** Un file JSON non impedisce a qualcuno di cancellare un autore lasciando 50 post "orfani" nel file.

Per risolvere questi problemi critici, l'informatica si affida ai **Database Relazionali (RDBMS)** come PostgreSQL, MySQL o SQLite.

---

## 2. Il Disallineamento Oggetto-Relazionale (*Impedance Mismatch*)

C'è però una sfida affascinante che ogni ingegnere del software deve conoscere:

* **Nel Codice Python (OOP):** I dati vivono come una **rete di Oggetti connessi** che contengono dati e metodi (`eroe.inventario.oggetti_contenuti`).
* **Nel Database Relazionale:** I dati vivono come **Tabelle piatte e separate** collegate da codici numerici (le Foreign Key).

Questa differenza strutturale si chiama **Disallineamento Oggetto-Relazionale (Object-Relational Impedance Mismatch)**.

```
       MONDO DEGLI OGGETTI (RAM)                     MONDO DEI DATABASE (DISCO)
┌──────────────────────────────────────┐       ┌──────────────────────────────────────┐
│  Oggetti vivi con Metodi             │       │  Tabelle Piatte senza Metodi         │
│  Riferimenti diretti tra istanze     │  VS   │  Righe e Colonne collegate da FK     │
│  Polimorfismo ed Ereditarietà        │       │  Algebra Relazionale                 │
└──────────────────────────────────────┘       └──────────────────────────────────────┘
```

---

## 3. Che cos'è un ORM (Object-Relational Mapping)?

Negli anni passati, per salvare gli oggetti nel database, gli sviluppatori dovevano scrivere centinaia di righe di codice per convertire manualmente ogni singolo attributo in una stringa SQL (`INSERT INTO...`) e viceversa.

Oggi questo lavoro ripetitivo viene affidato a uno strumento speciale chiamato **ORM (Object-Relational Mapper)**.

Un **ORM** è una libreria intelligente (come *SQLAlchemy* o *SQLModel* in Python, *Hibernate* in Java, *Entity Framework* in C#) che:
1. **Legge la classe `@dataclass`:** capisce da sola quali colonne creare nel database.
2. **Mappa le relazioni:** traduce automaticamente `eroe.inventario` nella corretta Foreign Key sul disco.
3. **Elimina il codice noioso:** permette di salvare un intero oggetto con un semplice comando (es. `db.save(eroe)`).

---

## 4. 🌉 Il Ponte verso il 5° Anno

Hai notato come tutti i pezzi del puzzle si stanno incastrando?

* In **4ª** abbiamo imparato a progettare il **Modello di Dominio**: sappiamo disegnare i diagrammi ER (le tabelle) e le classi UML (gli oggetti).
* In **5ª** partiremo esattamente da qui:
  1. Impareremo il linguaggio **SQL** per interrogare e gestire i database a livello professionale.
  2. Costruiremo il nostro primo **Server Web (Backend Flask / API)**.
  3. Collegheremo il Web e il Database creando un'applicazione completa da pubblicare online sul Cloud!