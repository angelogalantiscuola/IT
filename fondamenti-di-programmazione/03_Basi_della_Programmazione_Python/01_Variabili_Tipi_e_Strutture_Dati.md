# Variabili, Tipi e Strutture Dati

## 1. Le Variabili: Contenitori di Dati

Una **variabile** è un contenitore a cui diamo un nome per memorizzare un dato. È uno dei concetti più fondamentali della programmazione.

```python
nome_studente = "Alice"
eta = 17
media_voti = 8.5
ha_finito_i_compiti = True
```

## 2. Type Hinting: Dare un'Etichetta al Contenuto

Python è un linguaggio a *tipizzazione dinamica*, il che significa che non siamo obbligati a dichiarare il tipo di dato che una variabile conterrà. Tuttavia, è una buona pratica usare il **Type Hinting** (suggerimento di tipo) per rendere il codice più chiaro e meno soggetto a errori.

Il Type Hinting si scrive con i due punti (`:`) dopo il nome della variabile, seguito dal tipo.

```python
nome_studente: str = "Alice"          # str: stringa, per il testo
eta: int = 17                         # int: intero, per i numeri senza virgola
media_voti: float = 8.5               # float: per i numeri con la virgola
ha_finito_i_compiti: bool = True      # bool: booleano (True o False)
```
**Nota**: Il Type Hinting è solo un suggerimento per chi legge il codice e per gli strumenti di analisi; Python non impedirà di assegnare un valore di tipo diverso, ma ci aiuta a scrivere codice più corretto.

## 3. Strutture Dati: Contenitori Complessi

Spesso abbiamo bisogno di raggruppare più dati insieme. Per questo usiamo le strutture dati.

### a) Liste

Una **lista** è una collezione ordinata e modificabile di elementi. È perfetta per contenere una sequenza di valori dello stesso tipo.

```python
# Una lista di voti (interi)
voti: list[int] = [8, 7, 9, 6]

# Accedere a un elemento (l'indice parte da 0)
primo_voto = voti[0]  # Contiene 8

# Aggiungere un elemento
voti.append(9)

print(voti) # Output: [8, 7, 9, 6, 9]   
```

### b) Tuple

Una **tupla** è una collezione ordinata ma **immutabile**. Una volta creata, non può essere modificata. È utile per dati che non devono cambiare, come le coordinate.

```python
coordinate: tuple[int, int] = (10, 20)

x = coordinate[0] # Contiene 10
# coordinate.append(30) # Questo darebbe errore!
```

### c) Dizionari

Un **dizionario** è una collezione non ordinata di coppie **chiave-valore**. È perfetto per associare informazioni.

```python
# Un dizionario che descrive uno studente
studente: dict[str, any] = {
    "nome": "Bob",
    "eta": 18,
    "promosso": True
}

# Accedere a un valore tramite la sua chiave
nome_studente = studente["nome"] # Contiene "Bob"

# Aggiungere una nuova coppia
studente["materia_preferita"] = "Matematica"

print(studente)
```
*`any` nel Type Hinting significa che il valore può essere di qualsiasi tipo.*