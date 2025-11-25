import sqlite3
import os

# Definiamo dove creare il file del database (nella cartella instance)
if not os.path.exists('instance'):
    os.makedirs('instance')

db_path = os.path.join('instance', 'blog.sqlite')

# Ci connettiamo (se il file non esiste, lo crea)
connection = sqlite3.connect(db_path)

# Leggiamo lo schema SQL
with open('app/schema.sql') as f:
    connection.executescript(f.read())

print("Database creato con successo in:", db_path)
connection.close()