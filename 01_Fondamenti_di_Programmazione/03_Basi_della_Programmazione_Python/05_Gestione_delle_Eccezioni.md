# Gestione delle Eccezioni

## 1. Cos'è un'Eccezione?

Un'**eccezione** è un errore che si verifica durante l'esecuzione di un programma e che ne interrompe il normale flusso. Se non viene gestita, l'eccezione causa l'arresto anomalo (crash) del programma con un messaggio di errore.

*   **Analogia**: Stai seguendo una ricetta e ti accorgi che manca un ingrediente fondamentale (es. le uova). Non puoi continuare. Questo "imprevisto" è un'eccezione. Invece di fermarti, puoi avere un piano B: "se mancano le uova, usa le banane". Questo è "gestire l'eccezione".

## 2. Il Blocco `try...except`

Per gestire le eccezioni, Python usa il blocco `try...except`.

-   **`try`**: In questo blocco inseriamo il codice "rischioso", quello che potrebbe generare un'eccezione.
-   **`except`**: In questo blocco inseriamo il codice da eseguire *solo se* si verifica un'eccezione nel blocco `try`.

**Esempio Pratico:**
```python
try:
    # Codice che potrebbe causare un errore
    eta_str = input("Inserisci la tua età: ")
    eta = int(eta_str) # Questa riga può fallire se l'input non è un numero
    print(f"Tra un anno avrai {eta + 1} anni.")

except ValueError:
    # Codice da eseguire se si verifica un ValueError
    print("Errore: devi inserire un numero valido, non del testo!")
```

Senza `try...except`, se l'utente scrivesse "dieci" invece di "10", il programma si arresterebbe. Con questo blocco, invece, il programma mostra un messaggio di errore amichevole e termina in modo controllato.

## 3. Gestire Tipi Diversi di Eccezioni

Puoi gestire diversi tipi di errori in modo specifico, aggiungendo più blocchi `except`.

```python
try:
    numeratore = int(input("Inserisci il numeratore: "))
    denominatore = int(input("Inserisci il denominatore: "))
    risultato = numeratore / denominatore
    print(f"Il risultato è {risultato}")

except ValueError:
    print("Errore: devi inserire numeri validi.")

except ZeroDivisionError:
    print("Errore: è impossibile dividere per zero.")
```

## 4. Il Blocco `finally`

Il blocco **`finally`** contiene codice che viene eseguito **sempre**, indipendentemente dal fatto che si sia verificata un'eccezione o meno. È fondamentale per le operazioni di "pulizia", come chiudere una connessione o un file.

```python
file = None # Inizializziamo la variabile
try:
    file = open("dati.txt", "r")
    contenuto = file.read()
    print(contenuto)
except FileNotFoundError:
    print("Il file non esiste.")
finally:
    if file:
        file.close() # Questa operazione viene eseguita sempre
        print("File chiuso correttamente.")
```