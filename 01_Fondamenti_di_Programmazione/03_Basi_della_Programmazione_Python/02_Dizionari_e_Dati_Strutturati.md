# Dizionari e Dati Strutturati

Nel Modulo 01 abbiamo visto le **liste**, ideali per collezioni di elementi ordinati. Ma quando dobbiamo descrivere una "cosa" reale (uno studente, un prodotto, un'automobile), ci servono etichette con nome per ogni caratteristica.

Per questo usiamo i **Dizionari**.

---

## 1. Cos'è un Dizionario?

Un dizionario è una collezione di coppie **chiave: valore** racchiusa tra parentesi graffe `{}`.

* **Chiave (Key):** L'etichetta identificativa (quasi sempre una stringa).
* **Valore (Value):** Il dato associato a quell'etichetta (può essere di qualsiasi tipo: numero, testo, booleano o persino un'altra lista!).

```python
# Definizione di un dizionario che descrive uno studente
studente: dict[str, any] = {
    "nome": "Alice",
    "cognome": "Rossi",
    "eta": 17,
    "media": 8.2,
    "is_ripetente": False,
    "materie_preferite": ["Informatica", "Matematica"],
}

# 1. Leggere un valore tramite la sua chiave
print(f"Nome studente: {studente['nome']}")
print(f"Prima materia preferita: {studente['materie_preferite'][0]}")

# 2. Modificare o aggiungere una nuova coppia chiave-valore
studente["media"] = 8.5  # Modifica valore esistente
studente["classe"] = "3^A Info"  # Aggiunge una nuova chiave
```

---

## 2. Operazioni Comuni sui Dizionari

```python
studente = {"nome": "Mario", "eta": 16, "citta": "Milano"}

# Verificare se una chiave esiste prima di usarla (evita KeyError!)
if "email" in studente:
    print(studente["email"])
else:
    print("Email non presente.")

# Metodo .get(): restituisce un valore di default se la chiave non esiste
email = studente.get("email", "Nessuna email registrata")
print(email)

# Scorrere chiavi e valori con .items()
for chiave, valore in studente.items():
    print(f"- {chiave}: {valore}")
```

---

## 3. La Struttura Regina: Lista di Dizionari (Tabelle di Dati)

Nel mondo reale i dati arrivano quasi sempre sotto forma di **tabelle**: ogni riga è un record (dizionario) e l'intera tabella è una lista.

```python
# Un catalogo prodotti (Lista di Dizionari)
catalogo: list[dict] = [
    {"id": 101, "nome": "Tastiera Meccanica", "prezzo": 75.0, "disponibile": True},
    {"id": 102, "nome": "Mouse Wireless", "prezzo": 25.50, "disponibile": False},
    {"id": 103, "nome": "Monitor 24 pollici", "prezzo": 140.0, "disponibile": True},
]

# Scorrere la tabella ed elaborare i singoli record
for prodotto in catalogo:
    if prodotto["disponibile"]:
        print(f"Articolo: {prodotto['nome']} -> Prezzo: {prodotto['prezzo']:.2f}€")
```

---

## 4. Riepilogo: Lista vs Dizionario

| Struttura | Sintassi | Come si accede? | Quando si usa? |
| :--- | :--- | :--- | :--- |
| **Lista** | `[1, 2, 3]` | Tramite posizione/indice numerico (`lista[0]`) | Per elenchi ordinati di elementi simili (voti, nomi, temperature). |
| **Dizionario** | `{"k": "v"}` | Tramite nome della chiave (`dizionario["k"]`) | Per descrivere un'entità con proprietà nominate (un utente, un post, un articolo). |
| **Lista di Diz.** | `[{...}, {...}]` | Tramite indice e poi chiave (`catalogo[0]["nome"]`) | Per interi database o tabelle di record. |