import sqlite3


def crea_tabella():
    with sqlite3.connect("persone.db") as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS Persona (
                nome TEXT,
                eta INTEGER,
                citta TEXT
            )
        """)
        conn.commit()


def inserisci_dati():
    with sqlite3.connect("persone.db") as conn:
        c = conn.cursor()
        persone = [("Mario", 30, "Roma"), ("Luigi", 25, "Milano"), ("Anna", 22, "Roma")]
        c.executemany("INSERT INTO Persona (nome, eta, citta) VALUES (?, ?, ?)", persone)
        conn.commit()


def tutte_le_persone():
    with sqlite3.connect("persone.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Persona")
        persone = c.fetchall()
        for persona in persone:
            print(persona)


# Creazione del database e della tabella
crea_tabella()

# Inserimento dei dati di esempio
inserisci_dati()

# Esempio di utilizzo
tutte_le_persone()
