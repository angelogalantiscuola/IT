# Pattern Comuni di Manipolazione con i Dizionari

Le liste sono ottime per contenere collezioni di dati, ma i dizionari brillano quando dobbiamo organizzarli, contarli o accedervi in modo più strutturato.

### 1. Conteggio delle Frequenze
**Obiettivo:** Contare quante volte ogni elemento appare in una collezione.

**Problema:** Data una lista di voti, contare quanti studenti hanno preso ciascun voto.

```python
voti = [8, 7, 8, 9, 7, 10, 6, 8]

frequenze_voti = {} # Inizializza un dizionario vuoto
for voto in voti:
    if voto in frequenze_voti:
        frequenze_voti[voto] += 1
    else:
        frequenze_voti[voto] = 1

print(frequenze_voti)
# Output: {8: 3, 7: 2, 9: 1, 10: 1, 6: 1}
# Si legge: "3 studenti hanno preso 8, 2 studenti hanno preso 7, ..."
```

### 2. Raggruppamento di Dati
**Obiettivo:** Organizzare una lista di elementi in gruppi basati su una proprietà comune. Questo è uno dei pattern più potenti.

**Problema:** Data la lista di prodotti, raggrupparli per categoria.

```python
prodotti = [
    {"id": 1, "nome": "Laptop", "prezzo": 1200, "categoria": "Elettronica"},
    {"id": 2, "nome": "Tastiera", "prezzo": 80, "categoria": "Elettronica"},
    {"id": 3, "nome": "Libro Python", "prezzo": 35, "categoria": "Libri"},
    {"id": 4, "nome": "Scrivania", "prezzo": 200, "categoria": "Arredamento"},
]

prodotti_per_categoria = {}
for prodotto in prodotti:
    categoria = prodotto["categoria"]
    if categoria not in prodotti_per_categoria:
        # Se è la prima volta che vediamo questa categoria,
        # creiamo una nuova lista vuota per essa.
        prodotti_per_categoria[categoria] = []
    
    # Aggiungiamo il prodotto corrente alla lista della sua categoria.
    prodotti_per_categoria[categoria].append(prodotto)

# Per una stampa più leggibile, usiamo il modulo pprint
import pprint
pprint.pprint(prodotti_per_categoria)
# Output:
# {'Arredamento': [{'id': 4, ...}],
#  'Elettronica': [{'id': 1, ...}, {'id': 2, ...}],
#  'Libri': [{'id': 3, ...}]}
```

### 3. Indicizzazione (per Ricerche Veloci)
**Obiettivo:** Trasformare una lista di dati in un dizionario per poter accedere a un elemento istantaneamente tramite un suo identificatore univoco (ID), invece di dover ciclare ogni volta l'intera lista.

**Problema:** Data la lista di prodotti, creare una struttura che permetta di trovare un prodotto dato il suo `id` in modo immediato.

```python
# La nostra lista originale
prodotti_lista = [
    {"id": "A101", "nome": "Laptop", "prezzo": 1200},
    {"id": "B205", "nome": "Tastiera", "prezzo": 80},
    {"id": "C310", "nome": "Libro Python", "prezzo": 35},
]

# Creiamo un "indice" usando un dizionario
prodotti_indicizzati = {}
for prodotto in prodotti_lista:
    prodotti_indicizzati[prodotto["id"]] = prodotto

# Ora la ricerca è istantanea, senza bisogno di un ciclo 'for'!
id_da_cercare = "B205"
prodotto_cercato = prodotti_indicizzati[id_da_cercare]

print(prodotto_cercato)
# Output: {'id': 'B205', 'nome': 'Tastiera', 'prezzo': 80}
```
Questo approccio è molto più efficiente della ricerca lineare su una lista, specialmente quando la collezione di dati è molto grande.