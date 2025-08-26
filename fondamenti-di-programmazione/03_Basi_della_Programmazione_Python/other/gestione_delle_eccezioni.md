## Gestione delle eccezioni in Python <!-- omit in toc -->

- [Introduzione alle eccezioni](#introduzione-alle-eccezioni)
- [Struttura di base: try-except](#struttura-di-base-try-except)
- [Catturare eccezioni specifiche](#catturare-eccezioni-specifiche)
- [L'istruzione else](#listruzione-else)
- [L'istruzione finally](#listruzione-finally)
- [Sollevare eccezioni](#sollevare-eccezioni)
- [Creare eccezioni personalizzate](#creare-eccezioni-personalizzate)
- [Best practices nella gestione delle eccezioni](#best-practices-nella-gestione-delle-eccezioni)
- [Eccezioni comuni in Python](#eccezioni-comuni-in-python)

La gestione delle eccezioni è una parte fondamentale della programmazione in Python. Permette di gestire errori e situazioni impreviste in modo elegante, migliorando la robustezza e l'affidabilità del codice.

> Durante la fase di sviluppo, può essere utile non utilizzare blocchi `try`-`except` per vedere immediatamente gli errori e capire dove si verificano. Tuttavia, una volta che il codice è stabile, è buona pratica aggiungere blocchi `try`-`except` per gestire le eccezioni e migliorare la robustezza del codice.


### Introduzione alle eccezioni

Un'eccezione in Python è un evento che si verifica durante l'esecuzione di un programma che interrompe il normale flusso delle istruzioni. Quando si verifica un errore, Python genera un'eccezione.

> **Definizione**: Un'eccezione è un oggetto che rappresenta un errore o una condizione anomala che si verifica durante l'esecuzione di un programma.

Le eccezioni in Python hanno diversi vantaggi:
1. Separano il codice di gestione degli errori dal flusso normale del programma
2. Raggruppano e differenziano i tipi di errori
3. Propagano gli errori attraverso lo stack di chiamate

### Struttura di base: try-except

La struttura base per la gestione delle eccezioni in Python è il blocco `try-except`:

```python
try:
    # Codice che potrebbe generare un'eccezione
    risultato = 10 / 0
except ZeroDivisionError:
    # Codice da eseguire se si verifica un'eccezione
    print("Errore: Divisione per zero!")
```

In questo esempio:
- Il blocco `try` contiene il codice che potrebbe generare un'eccezione.
- Il blocco `except` specifica come gestire l'eccezione se si verifica.

### Catturare eccezioni specifiche

È possibile catturare eccezioni specifiche o multiple:

```python
try:
    numero = int(input("Inserisci un numero: "))
    risultato = 10 / numero
except ValueError:
    print("Errore: Input non valido. Inserisci un numero.")
except ZeroDivisionError:
    print("Errore: Non puoi dividere per zero.")
except (TypeError, OverflowError):
    print("Errore: Problema con il tipo o la dimensione del numero.")
except Exception as e:
    print(f"Si è verificato un errore imprevisto: {e}")
```

Questo approccio permette di gestire diversi tipi di errori in modo specifico.

### L'istruzione else

L'istruzione `else` può essere usata per eseguire codice quando non si verificano eccezioni:

```python
try:
    numero = int(input("Inserisci un numero: "))
    risultato = 10 / numero
except ValueError:
    print("Input non valido.")
except ZeroDivisionError:
    print("Non puoi dividere per zero.")
else:
    print(f"Il risultato è: {risultato}")
```

Il blocco `else` viene eseguito solo se non si verificano eccezioni nel blocco `try`.

### L'istruzione finally

L'istruzione `finally` definisce un blocco di codice che viene eseguito sempre, indipendentemente dal fatto che si verifichi o meno un'eccezione:

```python
try:
    file = open("esempio.txt", "r")
    contenuto = file.read()
except FileNotFoundError:
    print("Il file non è stato trovato.")
finally:
    file.close()  # Questo viene eseguito sempre
```

Il blocco `finally` è utile per le operazioni di pulizia, come la chiusura di file o connessioni di rete.

### Sollevare eccezioni

È possibile sollevare eccezioni manualmente usando l'istruzione `raise`:

```python
def dividi(a, b):
    if b == 0:
        raise ValueError("Il divisore non può essere zero")
    return a / b

try:
    risultato = dividi(10, 0)
except ValueError as e:
    print(f"Errore: {e}")
```

Questo permette di generare eccezioni in situazioni specifiche definite dal programmatore.

### Creare eccezioni personalizzate

È possibile creare eccezioni personalizzate ereditando dalla classe `Exception`:

```python
class ValoreNegativoError(Exception):
    """Eccezione sollevata per valori negativi non ammessi."""
    pass

def radice_quadrata(numero):
    if numero < 0:
        raise ValoreNegativoError("Non è possibile calcolare la radice quadrata di un numero negativo")
    return numero ** 0.5

try:
    print(radice_quadrata(-4))
except ValoreNegativoError as e:
    print(f"Errore: {e}")
```

Le eccezioni personalizzate sono utili per gestire errori specifici dell'applicazione.

### Best practices nella gestione delle eccezioni

1. **Sii specifico**: Cattura eccezioni specifiche anziché usare un generico `except:`.
2. **Non ignorare le eccezioni**: Evita di usare `pass` in un blocco `except` senza una buona ragione.
3. **Usa finally per la pulizia**: Utilizza `finally` per le operazioni di pulizia che devono essere eseguite sempre.
4. **Logga le eccezioni**: Registra le eccezioni per il debugging e il monitoraggio.
5. **Rilancia quando appropriato**: Se non puoi gestire un'eccezione, considerare di rilanciarla.

### Eccezioni comuni in Python

Alcune eccezioni comuni in Python includono:

| Eccezione           | Descrizione                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| `ValueError`        | Sollevata quando una funzione riceve un argomento del tipo corretto ma con un valore inappropriato |
| `TypeError`         | Sollevata quando un'operazione o funzione viene applicata a un oggetto del tipo sbagliato          |
| `IndexError`        | Sollevata quando si tenta di accedere a un indice inesistente di una sequenza                      |
| `KeyError`          | Sollevata quando si tenta di accedere a una chiave inesistente in un dizionario                    |
| `FileNotFoundError` | Sollevata quando si tenta di aprire un file che non esiste                                         |
| `ZeroDivisionError` | Sollevata quando si tenta di dividere per zero                                                     |

> **Nota**: La gestione delle eccezioni è un'arte che si perfeziona con la pratica. È importante trovare il giusto equilibrio tra la robustezza del codice e la leggibilità.

La gestione efficace delle eccezioni è fondamentale per scrivere codice Python robusto e affidabile. Permette di anticipare e gestire errori in modo elegante, migliorando la qualità e la manutenibilità del software.