# Introduzione alla Programmazione e Modelli Mentali

## 1. Che cos'è un Programma?

Un programma è una sequenza di istruzioni chiare e non ambigue che trasformano dei **dati in ingresso (Input)** in **risultati desiderati (Output)**.

Tutto ciò che fa un computer si riduce a tre azioni fondamentali:
1. **Ricordare informazioni** (usando le Variabili e le Liste).
2. **Prendere decisioni** (usando la Selezione `if/else`).
3. **Ripetere compiti** (usando i Cicli `for` e `while`).

---

## 2. Memorizzare i Dati: Variabili e Type Hinting

Una variabile è come una scatola con un'etichetta in cui possiamo conservare un valore.

Python è un linguaggio a **tipizzazione dinamica** (capisce da solo il tipo di dato), ma per scrivere codice chiaro, professionale e privo di errori usiamo il **Type Hinting** (suggerimento di tipo), indicando `: tipo` dopo il nome della variabile.

### a) I Tipi Primitivi Fondamentali

```python
nome: str = "Alice"  # str (stringa): testo racchiuso tra virgolette
eta: int = 16  # int (intero): numeri senza virgola
media_voti: float = 7.5  # float (decimale): numeri con la virgola (punto!)
is_iscritto: bool = True  # bool (booleano): solo due valori possibili (True o False)
```

> **Perché usiamo il Type Hinting se non è obbligatorio?**
> 1. Rende il codice auto-esplicativo per chi lo legge (e per l'IA).
> 2. VS Code e gli strumenti di qualità (come Ruff) possono segnalarci subito gli errori se proviamo a usare un numero come testo.

---

## 3. La Scatola a Scomparti: Le Liste

Spesso non dobbiamo salvare un singolo dato, ma un **insieme di elementi**. Invece di creare tante variabili separate (`voto1`, `voto2`, `voto3`...), usiamo una **lista** racchiusa tra parentesi quadre `[]`.

```python
# Una lista di voti (interi)
voti: list[int] = [8, 7, 9, 6]

# Accedere a uno scomparto (l'indice parte SEMPRE da 0)
primo_voto = voti[0]  # Vale 8
secondo_voto = voti[1]  # Vale 7

# Aggiungere un nuovo elemento in coda
voti.append(10)  # Ora voti è [8, 7, 9, 6, 10]
```

### 💡 Nota importante: Tipi diversi nella stessa lista
In Python le liste sono flessibili: possono contenere **elementi di tipo diverso** all'interno della stessa lista:

```python
# Una lista eterogenea (contiene stringa, intero, decimale e booleano)
scheda_studente = ["Alice", 16, 7.5, True]
```

* **Regola pratica:** Anche se Python lo consente, di solito è una buona abitudine creare liste con elementi dello **stesso tipo** (es. tutti numeri o tutti testi) quando dobbiamo scorrerle ed elaborarle con un ciclo.

---

## 4. Comunicare con l'Esterno (I/O)

### a) Input: Ricevere Dati dall'Utente
L'istruzione `input()` mette in pausa il programma e aspetta che l'utente scriva qualcosa. Restituisce **sempre una stringa (testo)**.

Se ci serve un numero per fare calcoli, dobbiamo fare il **casting** (conversione esplicita):

```python
eta_testo: str = input("Quanti anni hai? ")
eta: int = int(eta_testo)  # Conversione da testo a numero intero
```

### b) Output: Le f-string (Formattazione del Testo)
Per stampare a schermo testo mescolato a variabili, il modo moderno e più leggibile in Python è la **f-string** (Formatted String Literal).

Basta mettere la lettera **`f`** subito prima delle virgolette:

```python
nome: str = "Marco"
punti: int = 15
prezzo: float = 4.5

# Le parentesi graffe {} sono "finestre aperte sul codice Python":
print(f"Ciao {nome}, hai totalizzato {punti} punti!")

# Dentro le graffe puoi fare calcoli al volo:
print(f"Il doppio dei tuoi punti è: {punti * 2}")

# Puoi formattare i numeri decimali (es. :.2f = 2 cifre dopo la virgola):
print(f"Totale da pagare: {prezzo:.2f}€")  # Stampa: 4.50€
```

---

## 5. Il Controllo del Flusso

### a) Prendere Decisioni (`if / elif / else`)
Un programma spesso deve scegliere quale strada seguire. Una condizione logica e' una domanda a cui Python puo' rispondere solo `True` (vero) o `False` (falso).

`if`, `elif` e `else` formano **un'unica catena di scelta**:

- `if` pone la prima domanda.
- `elif` significa "altrimenti, se...": e' collegato all'`if` precedente e viene controllato solo se le condizioni prima di lui erano false.
- `else` significa "in tutti gli altri casi".

Python esegue **un solo blocco** della catena. Appena trova una condizione vera, esegue quel blocco e salta tutti quelli successivi.

```python
voto: int = 9

if voto >= 8:
    print("Ottimo")
elif voto >= 6:
    print("Promosso")
else:
    print("Da recuperare")
```

Con `voto = 9` viene stampato solo `Ottimo`: anche se `voto >= 6` e' vera, l'`elif` non viene piu' controllato, perche' il primo `if` ha gia' trovato il caso giusto.

### `if / elif / else` oppure due `if`?

Usa `if / elif / else` quando le alternative sono **mutuamente esclusive**: vuoi scegliere **un solo caso**.

Due `if` scritti uno dopo l'altro, invece, sono due decisioni indipendenti. Python controlla entrambe le condizioni, quindi possono essere vere ed eseguire entrambi i blocchi:

```python
voto: int = 9

if voto >= 8:
    print("Ottimo")

if voto >= 6:
    print("Promosso")
```

Con `voto = 9` questo programma stampa:

```text
Ottimo
Promosso
```

> **Regola pratica:** usa una catena `if / elif / else` per scegliere una sola risposta. Usa piu' `if` separati per controllare condizioni indipendenti che possono essere vere insieme.

### b) Scorrere le Liste con il ciclo `for`
Un ciclo serve per ripetere un'azione. In Python, il ciclo `for` scorre una lista prendendo un elemento alla volta: esegue il blocco indentato una volta per ogni elemento, poi termina quando la lista e' finita.

```python
studenti: list[str] = ["Alice", "Bob", "Carla"]

# Per ogni studente presente nella lista:
for studente in studenti:
    print(f"Benvenuto/a {studente}!")
```

Python esegue quindi il `print()` tre volte, una per ciascuno studente:

```text
Benvenuto/a Alice!
Benvenuto/a Bob!
Benvenuto/a Carla!
```

Se dobbiamo invece ripetere un'azione un numero prefissato di volte, usiamo `range()`. `range(5)` produce i numeri da `0` a `4`, cioe' cinque numeri in tutto:

```python
# Conta da 0 a 4 (5 giri)
for i in range(5):
    print(f"Giro numero {i + 1}")
```

L'`i + 1` serve soltanto per mostrare all'utente i giri da 1 a 5:

```text
Giro numero 1
Giro numero 2
Giro numero 3
Giro numero 4
Giro numero 5
```

### c) Ripetere finché una condizione è vera (`while`)
Il ciclo `while` significa "finche'": ripete il blocco indentato finche' la sua condizione e' vera. Si usa quando non conosciamo in anticipo il numero di ripetizioni.

```python
password_inserita = ""
while password_inserita != "1234":
    password_inserita = input("Inserisci il PIN: ")

print("PIN corretto, benvenuto!")
```

All'inizio `password_inserita` e' vuota, quindi e' diversa da `"1234"` e il ciclo chiede il PIN. Se l'utente inserisce un PIN errato, la condizione resta vera e il ciclo riparte. Quando inserisce `1234`, la condizione diventa falsa, il ciclo termina e viene eseguito il messaggio finale:

```text
Inserisci il PIN: 0000
Inserisci il PIN: 1234
PIN corretto, benvenuto!
```

> **Attenzione:** dentro un `while` qualcosa deve cambiare, altrimenti la condizione potrebbe restare sempre vera e il ciclo non terminerebbe mai.

