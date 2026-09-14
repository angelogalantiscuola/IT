# Mutabilità e Dati Protetti: Evitare le Modifiche Accidentali

Uno dei problemi più insidiosi nella programmazione è la modifica involontaria dei dati di partenza. Capire come Python gestisce le variabili in memoria è essenziale per scrivere codice pulito.

---

## 1. Tipi Immutabili vs Tipi Mutabili

In Python gli oggetti si dividono in due grandi categorie:

```
┌──────────────────────────────────────────────────────────────┐
│ 1. TIPI IMMUTABILI (int, float, str, bool, tuple)            │
│    - Il loro valore NON può essere modificato dopo la nascita│
│    - Ogni operazione crea una NUOVA copia                    │
├──────────────────────────────────────────────────────────────┤
│ 2. TIPI MUTABILI (list, dict, set)                           │
│    - Il loro contenuto può essere modificato sul posto       │
│    - Più variabili possono puntare alla STESSA scatola!      │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. La Trappola della "Scatola Condivisa"

Guarda cosa succede con le liste se non si fa attenzione:

```python
lista_a = [1, 2, 3]
lista_b = lista_a  # ATTENZIONE: non stiamo creando una nuova lista!

lista_b.append(99)

print(lista_a)  # Stampa: [1, 2, 3, 99] !!
```

* **Cosa è successo?** `lista_a` e `lista_b` sono solo due etichette attaccate alla **stessa scatola in memoria**. Modificando `lista_b`, abbiamo alterato anche `lista_a`.

---

## 3. Le Funzioni e i Dati Originali (Side Effects)

Quando passi una lista a una funzione, la funzione riceve la scatola originale. Se la funzione modifica la lista al suo interno, **i dati cambiano anche fuori!**

### ❌ Esempio Scorretto (Funzione che sporca i dati originali):
```python
def rimuovi_negativi_sbagliato(numeri: list[int]) -> list[int]:
    for n in numeri:
        if n < 0:
            numeri.remove(n)  # MODIFICA IN-PLACE: rovina la lista di partenza!
    return numeri


voti_originali = [8, -2, 7, -1, 10]
puliti = rimuovi_negativi_sbagliato(voti_originali)

print(voti_originali)  # I dati originali sono stati alterati per sbaglio!
```

---

### ✅ Esempio Corretto (Funzione Pulita che protegge i dati):
La funzione crea e restituisce una **nuova lista**, lasciando quella originale intatta:

```python
def rimuovi_negativi_corretto(numeri: list[int]) -> list[int]:
    risultato: list[int] = []
    for n in numeri:
        if n >= 0:
            risultato.append(n)  # Aggiunge solo alla NUOVA lista
    return risultato


voti_originali = [8, -2, 7, -1, 10]
puliti = rimuovi_negativi_corretto(voti_originali)

print(voti_originali)  # [8, -2, 7, -1, 10] -> I dati originali sono salvi!
print(puliti)  # [8, 7, 10]         -> Risultato corretto
```

---

## 4. Come Creare una Copia Esplicita

Se vuoi manipolare una lista senza rischiare di toccare l'originale, usa il metodo `.copy()`:

```python
lista_originale = [10, 20, 30]
copia_sicura = lista_originale.copy()

copia_sicura.append(999)
print(lista_originale)  # [10, 20, 30] (Intatta)
print(copia_sicura)  # [10, 20, 30, 999]
```

---

## 🎯 Regola del Detective:
> *"Una funzione di elaborazione dati deve comportarsi da ospite educato: usa le informazioni che riceve per calcolare il risultato, ma non rompe né sposta gli oggetti nella casa del proprietario (i dati originali)."*