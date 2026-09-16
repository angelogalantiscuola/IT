# Dalla RAM al Disco: La Serializzazione in JSON

Finora tutti gli eroi che abbiamo creato (`eroe1 = Personaggio(...)`) vivevano solo nella **memoria RAM**.
Nel momento in cui lo script Python termina, il computer svuota la RAM e **tutti i progressi dell'eroe vengono cancellati**.

Per salvare lo stato degli oggetti in modo che sopravvivano alla chiusura del programma, dobbiamo effettuare la **Persistenza**.

Il modo più immediato per iniziare è salvare i nostri oggetti in formato **JSON** (che abbiamo già studiato in 3ª).

---

## 1. Da Oggetto a Dizionario: `dataclasses.asdict`

Un file JSON non sa cosa sia una classe Python. Può salvare solo tipi standard: numeri, stringhe, liste e dizionari.

Il modulo `dataclasses` include una funzione speciale chiamata **`asdict()`** che trasforma qualsiasi oggetto in un dizionario pulito in una sola riga:

```python
import json
from dataclasses import dataclass, asdict


@dataclass
class Personaggio:
    id: int
    nome: str
    livello: int = 1
    punti_vita: int = 100


# Creiamo l'oggetto
eroe = Personaggio(id=1, nome="Aragorn", livello=5, punti_vita=80)

# 1. TRASFORMAZIONE: Da Oggetto a Dizionario
dati_dizionario = asdict(eroe)
print(dati_dizionario)
# Output: {'id': 1, 'nome': 'Aragorn', 'livello': 5, 'punti_vita': 80}

# 2. SALVATAGGIO: Scrittura su file JSON
with open("salvataggio_eroe.json", "w", encoding="utf-8") as file:
    json.dump(dati_dizionario, file, indent=4)

print("Salvataggio completato su file 'salvataggio_eroe.json'!")
```

---

## 2. Da File JSON a Oggetto Vivo (Deserializzazione)

Quando riavviamo il gioco, leggiamo il file JSON e usiamo l'operatore di *unpacking* (`**`) per passare tutti i valori al costruttore del `Personaggio`:

```python
import json
from src.entita import Personaggio

# 1. LETTURA dal file JSON
with open("salvataggio_eroe.json", "r", encoding="utf-8") as file:
    dati_caricati = json.load(file)

# 2. RICOSTRUZIONE: Creiamo un nuovo Oggetto vivo dai dati letti
# '**dati_caricati' equivale a scrivere: id=1, nome="Aragorn", livello=5, punti_vita=80
eroe_ricaricato = Personaggio(**dati_caricati)

print(f"Eroe ricaricato: {eroe_ricaricato.nome} (Livello {eroe_ricaricato.livello})")
eroe_ricaricato.subisci_danno(20)
print(f"PV dopo nuovo danno: {eroe_ricaricato.punti_vita}")  # 60 PV
```

---

## 3. I Limiti dei File JSON

Salvare su file JSON è comodo per il salvataggio di una singola partita offline. Ma cosa succede se abbiamo:
* Migliaia di giocatori contemporaneamente?
* Relazioni complesse tra centinaia di tabelle collegate?
* La necessità di cercare rapidamente un utente senza dover caricare un file gigante da 2 gigabyte in memoria?

Per questi scenari professionali i file JSON non bastano: **serve un Database Relazionale**.