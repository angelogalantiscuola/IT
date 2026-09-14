# I 4 Pattern Fondamentali sulle Liste

Nel lavoro quotidiano di manipolazione dati, il 90% delle operazioni si riconduce a quattro schemi logici ricorrenti (*pattern*). Imparare a riconoscerli permette di risolvere qualsiasi problema in modo rapido e ordinato.

Prendiamo come riferimento questo catalogo per tutti gli esempi:

```python
prodotti: list[dict] = [
    {"id": 101, "nome": "Laptop", "prezzo": 1200.0, "categoria": "Informatica"},
    {"id": 102, "nome": "Tastiera", "prezzo": 80.0, "categoria": "Informatica"},
    {"id": 103, "nome": "Manuale Python", "prezzo": 35.0, "categoria": "Libri"},
    {"id": 104, "nome": "Scrivania", "prezzo": 220.0, "categoria": "Arredamento"},
]
```

---

## 1. Pattern di Ricerca (Find)
* **Obiettivo:** Trovare il **singolo elemento** che soddisfa un criterio univoco (es. cercare per ID).

```python
def trova_prodotto_per_id(prodotti: list[dict], id_cercato: int) -> dict | None:
    """Restituisce il prodotto cercato oppure None se non trovato."""
    for p in prodotti:
        if p["id"] == id_cercato:
            return p  # Trovato! Usciamo subito dalla funzione
    return None


# Esempio
risultato = trova_prodotto_per_id(prodotti, 103)
print(risultato)  # {'id': 103, 'nome': 'Manuale Python', ...}
```

---

## 2. Pattern di Filtraggio (Filter)
* **Obiettivo:** Creare una **nuova lista** contenente solo gli elementi che soddisfano una data condizione (senza alterare la lista originale).

```python
def filtra_per_categoria(prodotti: list[dict], categoria: str) -> list[dict]:
    """Estrae solo i prodotti appartenenti alla categoria indicata."""
    selezionati: list[dict] = []
    for p in prodotti:
        if p["categoria"].lower() == categoria.lower():
            selezionati.append(p)
    return selezionati


# Esempio
libri = filtra_per_categoria(prodotti, "Libri")
print(libri)  # [{'id': 103, 'nome': 'Manuale Python', ...}]
```

---

## 3. Pattern di Trasformazione (Mapping)
* **Obiettivo:** Creare una nuova lista trasformando o estraendo una proprietà specifica da ciascun elemento.

```python
def estrai_nomi_prodotti(prodotti: list[dict]) -> list[str]:
    """Restituisce una lista di sole stringhe con i nomi dei prodotti."""
    nomi: list[str] = []
    for p in prodotti:
        nomi.append(p["nome"])
    return nomi


# Esempio
lista_nomi = estrai_nomi_prodotti(prodotti)
print(lista_nomi)  # ['Laptop', 'Tastiera', 'Manuale Python', 'Scrivania']
```

---

## 4. Pattern di Aggregazione (Reduce)
* **Obiettivo:** Elaborare l'intera lista per calcolare un **singolo valore di sintesi** (totale, media, conteggio, massimo).

```python
def calcola_valore_magazzino(prodotti: list[dict]) -> float:
    """Calcola la somma complessiva dei prezzi di tutti i prodotti."""
    totale: float = 0.0
    for p in prodotti:
        totale += p["prezzo"]
    return totale


# Esempio
valore_totale = calcola_valore_magazzino(prodotti)
print(f"Valore complessivo magazzino: {valore_totale:.2f}€")  # 1535.00€
```

---

## 🎯 Sintesi dei 4 Pattern:
1. **Ricerca:** Da lista $\longrightarrow$ a un singolo elemento (o `None`).
2. **Filtraggio:** Da lista $\longrightarrow$ a una sotto-lista con meno elementi.
3. **Mappatura:** Da lista di record $\longrightarrow$ a una nuova lista della stessa lunghezza con dati trasformati.
4. **Aggregazione:** Da lista $\longrightarrow$ a un singolo valore scalare (numero o testo).