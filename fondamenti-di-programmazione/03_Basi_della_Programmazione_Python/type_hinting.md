## Type Hinting in Python <!-- omit in toc -->

- [Introduzione](#introduzione)
- [Sintassi di Base](#sintassi-di-base)
- [Type Hinting per Funzioni](#type-hinting-per-funzioni)
- [Type Hinting per Variabili](#type-hinting-per-variabili)
- [Type Hinting per Classi](#type-hinting-per-classi)
- [Utilizzo di Tipi Complessi](#utilizzo-di-tipi-complessi)

### Introduzione

Il type hinting in Python è una funzionalità che permette di specificare i tipi delle variabili, dei parametri delle funzioni e dei valori di ritorno. Questo aiuta a migliorare la leggibilità del codice e a prevenire errori.

### Sintassi di Base

La sintassi di base per il type hinting utilizza i due punti `:` per specificare il tipo di una variabile o di un parametro, e la freccia `->` per specificare il tipo di ritorno di una funzione.

### Type Hinting per Funzioni

Ecco un esempio di come utilizzare il type hinting per una funzione:

```python
def somma(a: int, b: int) -> int:
    return a + b
```

In questo esempio, `a` e `b` sono dichiarati come interi (`int`), e la funzione `somma` restituisce un intero (`int`).

### Type Hinting per Variabili

Puoi anche utilizzare il type hinting per le variabili:

```python
nome: str = "Alice"
eta: int = 30
```

In questo esempio, `nome` è dichiarato come stringa (`str`) e `eta` come intero (`int`).

### Type Hinting per Classi

Il type hinting può essere utilizzato anche all'interno delle classi:

```python
class Studente:
    def __init__(self, nome: str, eta: int, matricola: str) -> None:
        self.nome: str = nome
        self.eta: int = eta
        self.matricola: str = matricola

    def descrizione(self) -> str:
        return f"{self.nome}, {self.eta} anni, matricola {self.matricola}"
```

In questo esempio, i parametri del costruttore e gli attributi della classe `Studente` sono annotati con i rispettivi tipi.

### Utilizzo di Tipi Complessi

Python supporta anche il type hinting per tipi complessi come liste, dizionari e tuple.

```python
numeri: list[int] = [1, 2, 3]
dati: dict[str, int] = {"uno": 1, "due": 2}
coordinate: tuple[int, int] = (10, 20)
```

In questo esempio, `numeri` è una lista di interi, `dati` è un dizionario con chiavi stringa e valori interi, e `coordinate` è una tupla di due interi.
