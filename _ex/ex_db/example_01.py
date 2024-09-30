import sqlite3

conn = sqlite3.connect("miodatabase.db")  # Connessione al database SQLite

cursor = conn.cursor()  # Creazione di un cursore

# Creazione di una tabella
query = "CREATE TABLE IF NOT EXISTS persone (id INTEGER PRIMARY KEY, nome TEXT, cognome TEXT)"
cursor.execute(query)  # Esecuzione di una query di cre

# Inserimento di un record
query = "INSERT INTO persone (nome, cognome) VALUES ('Mario', 'Rossi')"
cursor.execute(query)  # Esecuzione di una query di inserimento
# Inserimento di molti record
query = "INSERT INTO persone (nome, cognome) VALUES (?, ?)"
values = [
    ("Luca", "Bianchi"),
    ("Paolo", "Verdi"),
]  # I Valori da inserire si potrebbero anche leggere da un file JSON
cursor.executemany(
    query, values
)  # Esecuzione di una query di inserimento di molti record

query = "SELECT * FROM persone"  # Query di selezione
cursor.execute(query)  # Esecuzione di una query di selezione


rows = cursor.fetchall()  # Recupero dei risultati

for row in rows:  # Iterazione sui risultati
    print(row)
