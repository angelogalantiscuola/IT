# Pattern di Manipolazione con i Dizionari

Mentre le liste sono sequenze lineari, i **dizionari** brillano quando dobbiamo contare occorrenze, raggruppare record sparsi in categorie o velocizzare le ricerche.

---

## 1. Conteggio delle Frequenze
* **Obiettivo:** Contare quante volte compare ciascun valore all'interno di una collezione.

```python
def conta_frequenze_categorie(prodotti: list[dict]) -> dict[str, int]:
    """Conta quanti prodotti ci sono per ciascuna categoria."""
    frequenze: dict[str, int] = {}

    for p in prodotti:
        cat = p["categoria"]
        if cat in frequenze:
            frequenze[cat] += 1
        else:
            frequenze[cat] = 1

    return frequenze


# Esempio
conteggi = conta_frequenze_categorie(prodotti)
print(conteggi)
# Output: {'Informatica': 2, 'Libri': 1, 'Arredamento': 1}
```

---

## 2. Raggruppamento di Dati (Grouping)
* **Obiettivo:** Trasformare una lista piatta di record in un dizionario in cui ogni chiave rappresenta una categoria e il valore è la **lista dei record** appartenenti a quella categoria.

```python
def raggruppa_per_categoria(prodotti: list[dict]) -> dict[str, list[dict]]:
    """Raggruppa i prodotti creando un dizionario di liste."""
    gruppi: dict[str, list[dict]] = {}

    for p in prodotti:
        cat = p["categoria"]
        if cat not in gruppi:
            gruppi[cat] = []  # Se è la prima volta che incontriamo la categoria, creiamo la lista vuota
        gruppi[cat].append(p)

    return gruppi


# Esempio
catalogo_raggruppato = raggruppa_per_categoria(prodotti)
print(catalogo_raggruppato["Informatica"])
# Output: [{'id': 101, 'nome': 'Laptop', ...}, {'id': 102, 'nome': 'Tastiera', ...}]
```

---

## 3. Indicizzazione per Accesso Istantaneo ($O(1)$)
* **Obiettivo:** Trasformare una lista in un dizionario indice (`id -> record`) per evitare di dover scorrere tutta la lista ogni volta con un ciclo `for`.

```python
def crea_indice_prodotti(prodotti: list[dict]) -> dict[int, dict]:
    """Crea una mappa id -> prodotto per accesso immediato."""
    indice: dict[int, dict] = {}
    for p in prodotti:
        indice[p["id"]] = p
    return indice


# Utilizzo
indice_rapido = crea_indice_prodotti(prodotti)

# Ora l'accesso all'articolo 103 è immediato, senza cicli:
prodotto_scelto = indice_rapido.get(103)
print(prodotto_scelto["nome"])  # "Manuale Python"
```