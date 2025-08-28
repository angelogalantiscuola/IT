# Pattern Comuni di Manipolazione delle Liste

Quando lavoriamo con i dati, ci troviamo spesso a ripetere le stesse operazioni logiche. Imparare a riconoscere e implementare questi "pattern" (schemi) ci rende programmatori più veloci ed efficaci.

Consideriamo di avere la seguente lista di dati per tutti gli esempi:
```python
prodotti = [
    {"id": 1, "nome": "Laptop", "prezzo": 1200, "categoria": "Elettronica"},
    {"id": 2, "nome": "Tastiera", "prezzo": 80, "categoria": "Elettronica"},
    {"id": 3, "nome": "Libro Python", "prezzo": 35, "categoria": "Libri"},
    {"id": 4, "nome": "Scrivania", "prezzo": 200, "categoria": "Arredamento"},
]
```

### 1. Ricerca (Trovare un elemento)
**Obiettivo:** Trovare un elemento specifico che soddisfa una condizione.

**Problema:** Trovare il prodotto con `id` uguale a 3.

```python
prodotto_cercato = None
for prodotto in prodotti:
    if prodotto["id"] == 3:
        prodotto_cercato = prodotto
        break # Trovato! Inutile continuare il ciclo.

print(prodotto_cercato)
# Output: {'id': 3, 'nome': 'Libro Python', 'prezzo': 35, 'categoria': 'Libri'}
```

### 2. Filtraggio (Selezionare un sottoinsieme)
**Obiettivo:** Creare una nuova lista contenente solo gli elementi che soddisfano una condizione.

**Problema:** Trovare tutti i prodotti della categoria "Elettronica".

```python
prodotti_elettronici = [] # Inizializza una lista vuota
for prodotto in prodotti:
    if prodotto["categoria"] == "Elettronica":
        prodotti_elettronici.append(prodotto)

print(prodotti_elettronici)
# Output: [{'id': 1, ...}, {'id': 2, ...}]
```

### 3. Trasformazione (Mapping)
**Obiettivo:** Creare una nuova lista trasformando ogni elemento della lista originale.

**Problema:** Creare una lista contenente solo i nomi di tutti i prodotti.

```python
nomi_prodotti = []
for prodotto in prodotti:
    nomi_prodotti.append(prodotto["nome"])

print(nomi_prodotti)
# Output: ['Laptop', 'Tastiera', 'Libro Python', 'Scrivania']
```

### 4. Aggregazione (Reducing)
**Obiettivo:** Calcolare un singolo valore riassuntivo a partire da un'intera lista.

**Problema:** Calcolare il prezzo totale di tutti i prodotti in magazzino.

```python
prezzo_totale = 0
for prodotto in prodotti:
    prezzo_totale += prodotto["prezzo"]

print(f"Il valore totale del magazzino è: {prezzo_totale}€")
# Output: Il valore totale del magazzino è: 1515€

# Si può anche fare in modo più "Pythonico" usando la trasformazione
# e la funzione sum()
prezzi = [prodotto["prezzo"] for prodotto in prodotti] # Questo si chiama "list comprehension"
prezzo_totale_pythonico = sum(prezzi)
print(f"Valore totale (modo Pythonico): {prezzo_totale_pythonico}€")
```
Questi quattro pattern sono i mattoni fondamentali per quasi ogni operazione di analisi e manipolazione dei dati.